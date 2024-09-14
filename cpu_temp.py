from flask import Flask, render_template, send_file, jsonify
import io
import psutil
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
import pandas as pd



app = Flask(__name__)

@app.route('/index')
def index():
    cpu_usage = int(psutil.cpu_percent(interval=1))
    disk_usage = int(psutil.disk_usage('/').percent)
    memory_usage = int(psutil.virtual_memory().percent)
    return render_template(
        "index.html",
        cpu=cpu_usage,
        disk=disk_usage,
        memoria=memory_usage
    )







# Template Routes
@app.route('/tem')
def temperature():
    return render_template("temperatura.html")

@app.route('/disk')
def disk():
    return render_template("disco.html")






# Helper function to generate and return a plot
def generate_plot(x, y, x_label, y_label, title):
    fig, ax = plt.subplots(figsize=(20, 10))
    sns.lineplot(x=x, y=y, ax=ax)
    ax.set_xlabel(x_label)
    ax.set_ylabel(y_label)
    ax.set_title(title)
    
    canvas = FigureCanvas(fig)
    img = io.BytesIO()
    fig.savefig(img, format='png')
    img.seek(0)
    plt.close(fig)
    
    return img

# CPU Temperature Plot
@app.route('/CPU')
def cpu_temperature():
    try:
        cpu_usages = []
        temperatures = []

        for _ in range(60):
            CPU = psutil.cpu_percent(interval=1)
            temps = psutil.sensors_temperatures()
            
            if not temps:
                return jsonify({"error": "Temperature sensor data not available"}), 500
            
            temp_key = next(iter(temps))
            if not temps[temp_key]:
                return jsonify({"error": "No temperature data available"}), 500
            
            cpu_temp = temps[temp_key][0].current
            
            cpu_usages.append(CPU)
            temperatures.append(cpu_temp)

        img = generate_plot(range(len(temperatures)), temperatures, 'Time (s)', 'Temperature (°C)', 'CPU Temperature Over Time')
        return send_file(img, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    




# Disk and Memory Usage Plot
@app.route('/DISCO')
def disk_usage():
    try:
        disk_usages = []
        memory_usages = []

        for _ in range(60):
            disk_usage = psutil.disk_usage('/').percent
            memory_usage = psutil.virtual_memory().percent
            
            disk_usages.append(disk_usage)
            memory_usages.append(memory_usage)
        
        fig, ax1 = plt.subplots(figsize=(20, 10))

        # Plot Disk Usage
        ax1.bar(range(len(disk_usages)), disk_usages, color='blue', label='Disk Usage')
        ax1.set_xlabel('Time (s)')
        ax1.set_ylabel('Disk Usage (%)', color='blue')
        ax1.tick_params(axis='y', labelcolor='blue')
        
        # Create a second y-axis to plot Memory Usage
        ax2 = ax1.twinx()
        ax2.bar(range(len(memory_usages)), memory_usages, color='red', label='Memory Usage')
        ax2.set_ylabel('Memory Usage (%)', color='red')
        ax2.tick_params(axis='y', labelcolor='red')
        
        # Add titles and legends
        ax1.set_title('Disk and Memory Usage Over Time')
        fig.tight_layout()  # Adjust layout to prevent overlap

        canvas = FigureCanvas(fig)
        img = io.BytesIO()
        fig.savefig(img, format='png')
        img.seek(0)
        plt.close(fig)

        return send_file(img, mimetype='image/png')

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
