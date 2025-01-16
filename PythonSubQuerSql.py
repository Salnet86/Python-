import mysql.connector

# Connessione al database
conn = mysql.connector.connect(
    host="localhost",    # Modifica con il tuo host
    user="root",         # Modifica con il tuo username
    password="password", # Modifica con la tua password
    database="azienda"   # Modifica con il nome del tuo database
)

cursor = conn.cursor()

# Esegui la query con la subquery
query = """
SELECT utenti, saldi
FROM dipendenti d
WHERE saldi > (
    SELECT SUM(saldi)
    FROM dipendenti
    WHERE id_dipartimento = d.id_dipartimento
);
"""

# Esegui la query
cursor.execute(query)

# Recupera e stampa i risultati
results = cursor.fetchall()
for row in results:
    print(f"Utente: {row[0]}, Saldo: {row[1]}")

# Chiudi la connessione
cursor.close()
conn.close()
