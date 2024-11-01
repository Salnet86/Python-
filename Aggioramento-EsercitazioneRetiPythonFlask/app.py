import pandas as pnd
import mysql.connector
from flask import Flask, Response, request, render_template, redirect, url_for
import matplotlib.pyplot as plt
import io
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas

app = Flask(__name__)

def get_db_connection():
    try:
        return mysql.connector.connect(
            host='',
            user='',
            password='',
            database=''
        )
    except mysql.connector.Error as err:
        print(f"Error: {err}")
        return None

@app.route('/index')
def homeindex():
    return render_template('insert.html')

@app.route('/TP')
def temp_md():
    return render_template('Record.html')

@app.route('/temp', methods=['GET', 'POST'])
def temp():
    if request.method == 'POST':
        temp = request.form['temperatura']
        umid = request.form['umidita']

        insert_st = "INSERT INTO TM (temperatura, umidita) VALUES (%s, %s)"
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(insert_st, (temp, umid))
                conn.commit()
            finally:
                cursor.close()
                conn.close()
        return render_template('insert.html')

@app.route('/temp_delete', methods=['POST'])
def tempdelete():
    if request.method == 'POST':
        id_to_delete = request.form.get('id')
        delete_st = "DELETE FROM TM WHERE id = %s"
        conn = get_db_connection()
        if conn:
            try:
                cursor = conn.cursor()
                cursor.execute(delete_st, (id_to_delete,))
                conn.commit()
            finally:
                cursor.close()
                conn.close()
        return redirect(url_for('temRecord'))

@app.route('/TP_record')
def temRecord():
    conn = get_db_connection()
    if conn:
        try:
            cursor = conn.cursor()
            query = "SELECT id, temperatura, umidita FROM TM;"
            cursor.execute(query)
            data = cursor.fetchall()
        finally:
            cursor.close()
            conn.close()
        return render_template("Record.html", data=data)
    return "Database connection error", 500

@app.route('/show')
def show_tem():
    conn = get_db_connection()
    if conn:
        df = pnd.read_sql("SELECT id, temperatura, umidita FROM TM", conn)

        # Creare una figura con due subplot
        fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8))

        # Grafico della temperatura
        ax1.bar(df['id'], df['temperatura'], color='lime')
        ax1.set_title('Temperature')
        ax1.set_xlabel('ID')
        ax1.set_ylabel('Temperature (°C)')

        # Grafico dell'umidità
        ax2.bar(df['id'], df['umidita'], color='blue')
        ax2.set_title('Humidity')
        ax2.set_xlabel('ID')
        ax2.set_ylabel('Humidity (%)')

        # Salva l'immagine in un buffer
        img = io.BytesIO()
        FigureCanvas(fig).print_png(img)
        img.seek(0)
        plt.close(fig)

        conn.close()
        return Response(img.getvalue(), mimetype='image/png')
    return "Database connection error", 500

if __name__ == '__main__':
    app.run(debug=True)







