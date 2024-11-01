#--------------------------------------------------------------
# Importa le librerie necessarie da Flask e altre
from flask import Flask, Response, render_template, jsonify
import io  # Per gestire i flussi di input/output
import psutil  # Per monitorare l'utilizzo delle risorse di sistema
import matplotlib.pyplot as plt  # Per creare grafici
import seaborn as sns  # Per migliorare la visualizzazione dei dati

# Crea un'istanza dell'applicazione Flask
app = Flask(__name__)

# Definisce la route per la pagina principale
@app.route('/index')
def index():
    try:
        # Raccoglie i dati di utilizzo della CPU, disco e memoria
        cpu_usage = int(psutil.cpu_percent(interval=1))
        disk_usage = int(psutil.disk_usage('/').percent)
        memory_usage = int(psutil.virtual_memory().percent)

    except Exception as e:
        # In caso di errore, restituisce un messaggio di errore
        return jsonify({"error": str(e)}), 500

    # Restituisce il template index.html con i dati raccolti
    return render_template(
        "index.html",
        cpu=cpu_usage,
        disk=disk_usage,
        memoria=memory_usage,
    )





# Definisce la route per la pagina della temperatura CPU
@app.route("/cpu")
def CPU_temp():
    return render_template("temperatura.html")

# Definisce la route per raccogliere dati di temperatura e utilizzo della CPU
@app.route('/tem')
def temperatura():
    cpu_usages = []  # Lista per memorizzare i dati di utilizzo della CPU
    temperatures = []  # Lista per memorizzare i dati di temperatura

    # Raccoglie dati di utilizzo della CPU e temperatura
    for _ in range(20):
        cpu_usages.append(psutil.cpu_percent(interval=1))  # Aggiunge l'utilizzo della CPU



    # Crea il grafico
    plt.figure(figsize=(20, 5))  # Imposta la dimensione della figura
    sns.lineplot(x=range(len(cpu_usages)), y=cpu_usages, label='Utilizzo CPU')  # Grafico dell'utilizzo CPU
    plt.xlabel('Tempo')  # Etichetta dell'asse x
    plt.ylabel('Valore')  # Etichetta dell'asse y
    plt.title('Utilizzo CPU')  # Titolo del grafico
    plt.legend()  # Aggiunge la legenda
    plt.grid(True)  # Abilita la griglia

    # Salva il grafico in un oggetto BytesIO e restituisce l'immagine
    img = io.BytesIO()  # Crea un oggetto BytesIO
    plt.savefig(img, format='png')  # Salva il grafico come immagine PNG
    img.seek(0)  # Riporta il cursore all'inizio del flusso
    plt.close()  # Chiude la figura per liberare memoria

    return Response(img, mimetype='image/png')  # Restituisce l'immagine come risposta

    # Avvia l'applicazione se questo file è eseguito come script principale
if __name__ == '__main__':
    app.run(debug=True)  # Esegue l'app in modalità debug


