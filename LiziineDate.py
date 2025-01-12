# 1. Lavorare con le date in Python (usando il modulo datetime)
import datetime

# Data odierna
oggi = datetime.date.today()
print("Oggi:", oggi)

# Data specifica (anno, mese, giorno)
data_specifica = datetime.date(2025, 1, 12)
print("Data specifica:", data_specifica)

# Estrazione di anno, mese, giorno
anno = oggi.year
mese = oggi.month
giorno = oggi.day
print(f"Anno: {anno}, Mese: {mese}, Giorno: {giorno}")

# Data e ora correnti
ora_corrente = datetime.datetime.now()
print("Data e ora correnti:", ora_corrente)

# Formattare la data (data in formato 'giorno/mese/anno')
data_formattata = oggi.strftime("%d/%m/%Y")
print("Data formattata:", data_formattata)

# Giorno della settimana
giorno_settimana = oggi.strftime("%A")  # Nome del giorno della settimana
print("Giorno della settimana:", giorno_settimana)

# Aggiungere giorni alla data (usando timedelta)
due_giorni = datetime.timedelta(days=2)
data_piu_due_giorni = oggi + due_giorni
print("Data dopo 2 giorni:", data_piu_due_giorni)

# Sottrarre giorni dalla data
data_meno_due_giorni = oggi - due_giorni
print("Data prima di 2 giorni:", data_meno_due_giorni)


# 2. Lavorare con le ore e i minuti
# Ora attuale
ora_attuale = datetime.datetime.now().time()
print("Ora attuale:", ora_attuale)

# Aggiungere ore e minuti
due_ore = datetime.timedelta(hours=2)
ora_piu_due_ore = datetime.datetime.now() + due_ore
print("Ora dopo 2 ore:", ora_piu_due_ore.time())

# 3. Operazioni con giorni
# Giorno successivo
giorno_successivo = oggi + datetime.timedelta(days=1)
print("Giorno successivo:", giorno_successivo)

# Giorno precedente
giorno_precedente = oggi - datetime.timedelta(days=1)
print("Giorno precedente:", giorno_precedente)


# 4. Numeri formattati (usando il metodo format e f-string)
numero = 1234567.8910

# Formattazione con numero di decimali
print("\nNumeri formattati con 2 decimali:")
print(f"{numero:.2f}")  # 2 decimali

# Formattazione con separatori di migliaia
print("\nNumeri formattati con separatori di migliaia:")
print(f"{numero:,}")  # Separatore di migliaia (es. 1,234,567.89)

# Formattazione come percentuale
percentuale = 0.12345
print("\nPercentuale formattata:")
print(f"{percentuale:.2%}")  # 12.35%

# Formattazione con larghezza e riempimento (usando f-string)
print("\nFormattazione con larghezza e riempimento:")
print(f"{numero:10.2f}")  # Larghezza 10, 2 decimali
print(f"{numero:010.2f}")  # Larghezza 10, 2 decimali con riempimento con zeri

# 5. Uso della libreria locale per formattare numeri in base alla lingua
import locale

# Impostare la lingua italiana per la localizzazione
locale.setlocale(locale.LC_ALL, 'it_IT.UTF-8')

# Formattazione di numeri secondo la lingua italiana (con separatore delle migliaia)
print("\nFormattazione secondo la lingua italiana:")
print(locale.format_string("%0.2f", numero, grouping=True))  # Formattazione italiana

# 6. Calcolare la differenza tra due date (giorni di differenza)
data1 = datetime.date(2025, 1, 1)
data2 = datetime.date(2025, 1, 12)
differenza = data2 - data1
print("\nDifferenza tra le date:", differenza.days, "giorni")

# 7. Giorno della settimana per una data specifica
data_specifica2 = datetime.date(2025, 1, 12)
giorno_della_settimana = data_specifica2.strftime("%A")
print("\nGiorno della settimana per la data 12 gennaio 2025:", giorno_della_settimana)

# 8. Eseguire calcoli con il tempo (ore, minuti, secondi)
tempo_iniziale = datetime.datetime.now()
# Simuliamo un'attività che dura 1 ora, 30 minuti e 45 secondi
tempo_attività = datetime.timedelta(hours=1, minutes=30, seconds=45)
tempo_finale = tempo_iniziale + tempo_attività
print("\nOra finale dopo 1 ora, 30 minuti e 45 secondi:", tempo_finale.strftime("%H:%M:%S"))

# 9. Sommare e sottrarre tempo usando timedelta
print("\nAggiungere 10 giorni al 12 gennaio 2025:")
nuova_data = data_specifica2 + datetime.timedelta(days=10)
print("Nuova data:", nuova_data)

print("\nSottrarre 5 giorni dal 12 gennaio 2025:")
data_sottratta = data_specifica2 - datetime.timedelta(days=5)
print("Data sottratta:", data_sottratta)
