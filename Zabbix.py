import requests
import json
import sys
import logging
import datetime
from datetime import datetime, timedelta
import pandas as pd
from pyzabbix.api import ZabbixAPI
from ZabbixAPI_py import Zabbix

# --- Configurazione Iniziale ---
ZABBIX_API_URL = "https://URL_ZABBIX/zabbix/api_jsonrpc.php"
UNAME = "Admin"
PWORD = "password"

# Login tramite requests
r = requests.post(ZABBIX_API_URL, json={
    "jsonrpc": "2.0",
    "method": "user.login", 
    "params": {
        "user": UNAME, "password": PWORD
    },
    "id": 1
})

print(json.dumps(r.json(), indent=4, sort_keys=True))
AUTHTOKEN = r.json()["result"]

# Retrieve a list of problems
print("\nRetrieve a list of problems")
r = requests.post(ZABBIX_API_URL, json={
    "jsonrpc": "2.0",
    "method": "problem.get", 
    "params": {
        "output": "extend", 
        "selectAcknowledges": "extend", 
        "recent": "true",
        "sortfield": ["eventid"], 
        "sortorder": "DESC"
    },
    "id": 2,
    "auth": AUTHTOKEN
})
print(json.dumps(r.json(), indent=4, sort_keys=True))

# Logout user
print("\nLogout user")
r = requests.post(ZABBIX_API_URL, json={
    "jsonrpc": "2.0",
    "method": "user.logout",
    "params": {}, 
    "id": 2,
    "auth": AUTHTOKEN
})
print(json.dumps(r.json(), indent=4, sort_keys=True))

# --- Utilizzo libreria pyzabbix ---
# Create ZabbixAPI class instance
zapi = ZabbixAPI(url='https://URL_ZABBIX/zabbix/', user='Admin', password='zabbix')

# Get all monitored hosts
result1 = zapi.host.get(monitored_hosts=1, output='extend')

# Get all disabled hosts
result2 = zapi.do_request('host.get', { 
    'filter': {'status': 1},
    'output': 'extend'
})

# Filter results
hostnames1 = [host['host'] for host in result1]
hostnames2 = [host['host'] for host in result2['result']]

# Logout from Zabbix
zapi.user.logout()

# --- Esempio con Context Manager ---
with ZabbixAPI(url='https://URL_ZABBIX/zabbix/', user='Admin', password='zabbix') as zapi:
    result1 = zapi.host.get(monitored_hosts=1, output='extend')

# --- Logging e Debugging ---
logger = logging.getLogger("pyzabbix")
logger.setLevel(logging.DEBUG)
handler = logging.StreamHandler(sys.stdout)
logger.addHandler(handler)

zapi = ZabbixAPI(url='http://URL_ZABBIX', user='Admin', password='zabbix')

# --- Funzione estrazione metriche ---
def getMetricData(config, parameters, hosts, startTime, endTime):
    """Get metric data from Zabbix API"""
    logger.info("Begin to connect to zabbix:{} User/Pwd:{}/{}".format(
        str(config['ZABBIX_URL']), str(config['ZABBIX_USER']), str(config['ZABBIX_PASSWORD'])))
    
    zapi = ZabbixAPI(url=config['ZABBIX_URL'], user=config['ZABBIX_USER'], password=config['ZABBIX_PASSWORD'])
    logger.info("Get connection from zabbix success")
    
    hosts_ids = []
    hosts_res = zapi.do_request('host.get', { 
        'filter': {"host": hosts}, 
        "sortfield": "name",
        'output': 'extend'
    })
    for item in hosts_res['result']:
        host_id = item['hostid']
        hosts_ids.append(host_id)

# --- Analisi Trend e Dataframe ---
for host in hosts:
    cpu_item = zapi.item.get(hostids=host['hostid'], search={'name': 'CPU Busy'})
    if len(cpu_item) == 0:
        continue

    cpu_trend = zapi.trend.get(itemids=cpu_item[0]['itemid'], limit=168, output=["clock", "value_avg", "value_max"])
    if len(cpu_trend) == 0:
        continue

    df = pd.DataFrame(cpu_trend)
    cpu_avg_max = df['value_max'].astype(float).mean()
    cpu_max_avg = df['value_avg'].astype(float).max()
    cpu_avg_std = df['value_avg'].astype(float).std()
    cpu_up_var = (cpu_max_avg + cpu_avg_std) * 1.25

    if cpu_avg_max > 50:
        print(host['name']+','+str(cpu_max_avg)+','+str(cpu_avg_max)+','+str(cpu_avg_std)+','+str(cpu_up_var))

# --- Sezione specifica URL Server ---
ZABBIX_SERVER = 'https://URL_ZABBIX'
zapi = ZabbixAPI(ZABBIX_SERVER)
zapi.login(UNAME, PWORD)

hosts = zapi.host.get(monitored_hosts=1, output='extend')
hosts = [{k:r[k] for k in ["host", "hostid"]} for r in hosts]
for host in hosts:
    print(host["host"])
    # Utilizzo della funzione get_metric
    data = get_metric(host["hostid"], "Total CPU Utilization", (2019,5,1), (2019,5,27))

def get_metric(host_id, metric, dfrom, dto):
    dfrom = int(datetime(*dfrom).timestamp())
    dto = int(datetime(*dto).timestamp())
    hostitems = zapi.item.get(filter={"hostid": host_id, "name": metric})
    t_metric = [item for item in hostitems if metric == item["name"] and item["hostid"] == host_id]

    data = {"values": [], "timestamps": []}
    if len(t_metric):
        item = t_metric.pop()
        history = zapi.history.get(
            hostids=[host_id], 
            itemids=[item["itemid"]], 
            time_from=dfrom, 
            time_till=dto, 
            output='extend', 
            history=item["value_type"]
        )
        if len(history) == 0:
            return data
        df = pd.DataFrame(history)
        df = df[["clock", "value"]]
        df["value"] = df["value"].astype(float)
        df["clock"] = df["clock"].astype(int) * 1000
        return {"values": df["value"].tolist(), "timestamps": df["clock"].tolist()}
    return data

# --- Monitoraggio Problemi Recenti ---
zabbix = Zabbix('URL_HOST')
zabbix.login('id','password')

tenMin = datetime.today() - timedelta(minutes=10)
for x in zabbix.problem(method='get'):
    eventTime = datetime.fromtimestamp(int(x['clock']))
    if tenMin < eventTime:
        msg = str(eventTime) + x['name']
        print(msg)