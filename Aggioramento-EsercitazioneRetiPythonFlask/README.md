Statistiche di Sistema
Uso CPU: 29%
Uso Disco: 58%
Uso Memoria: 84%
Autori del software
AUTORE 1 BREZZA SALVATORE
AUTORE 2 MARIA
manuale software
Flask: Per creare l'applicazione web.
Response, render_template, jsonify: Funzioni per gestire le risposte e i template.
io: Per gestire i flussi di dati in memoria.
psutil: Per ottenere informazioni sul sistema (uso della CPU, disco e memoria).
matplotlib e seaborn: Per creare grafici.
Creazione dell'applicazione:
Viene creata un'istanza di Flask chiamata app.
Rotta /index:
Raccoglie l'uso della CPU, del disco e della memoria.
Se c'è un errore durante la raccolta dei dati, restituisce un errore 500 in formato JSON.
Se i dati vengono raccolti correttamente, il template index.html viene renderizzato con i dati delle statistiche.
Rotta /cpu_temperatura:
Rende il template temperatura.html, che mostra un'intestazione per la temperatura della CPU.
Rotta /tem:
Raccoglie i dati di utilizzo della CPU e la temperatura per un periodo di tempo.
Crea un grafico utilizzando matplotlib e seaborn per visualizzare l'uso della CPU e la temperatura nel tempo.
Il grafico viene salvato in un oggetto BytesIO e restituito come immagine PNG.
Esecuzione dell'app:
