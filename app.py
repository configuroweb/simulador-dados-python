from flask import Flask, render_template_string, request, send_from_directory
import random
import os

app = Flask(__name__)

# Asegúrate de que las imágenes estén en un directorio accesible
app.config["DADOS_FOLDER"] = "static/dados"

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Simulador de Dados</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            min-height: 100vh;
            margin: 0;
            background-color: #f0f0f0;
        }
        h1 {
            color: #333;
        }
        button {
            background-color: #4CAF50; /* Green */
            border: none;
            color: white;
            padding: 15px 32px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 16px;
            margin: 4px 2px;
            cursor: pointer;
        }
        img {
            max-width: 100%; /* Hace que la imagen no sea más ancha que su contenedor */
            height: auto; /* Mantiene la proporción de la imagen al escalar */
            margin-top: 20px; /* Añade un poco de espacio arriba de la imagen */
        }
    </style>
</head>
<body>
    <h1>Simulador de Dados</h1>
    {% if resultado %}
        <h2>Resultado: {{ resultado }}</h2>
        <img src="{{ url_for('static', filename='dados/dado_' ~ resultado ~ '.png') }}" alt="Resultado del Dado">
    {% endif %}
    <form action="/" method="post">
        <button type="submit">Lanzar Dado</button>
    </form>
</body>
</html>
"""


@app.route("/", methods=["GET", "POST"])
def home():
    resultado = None
    if request.method == "POST":
        resultado = random.randint(1, 6)
    return render_template_string(HTML_TEMPLATE, resultado=resultado)


# Ruta para servir las imágenes de los dados
@app.route("/static/dados/<path:filename>")
def send_dado(filename):
    return send_from_directory(app.config["DADOS_FOLDER"], filename)


if __name__ == "__main__":
    app.run(debug=True)
