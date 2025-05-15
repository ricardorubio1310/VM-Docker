from flask import Flask, render_template_string, jsonify
import time

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>Benchmark Simple</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>
</head>
<body class="bg-light">
    <div class="container mt-5 text-center">
        <h1>Aplicación Benchmark Simple</h1>
        <p class="lead">Página para test de respuesta rápida</p>
        <div>
            <button id="pingBtn" class="btn btn-primary mb-3">Enviar Ping</button>
            <p>Respuestas recibidas: <span id="counter">0</span></p>
            <p>Última latencia: <span id="latency">-</span> ms</p>
        </div>
    </div>
    <script>
        let counter = 0;
        document.getElementById('pingBtn').onclick = async () => {
            const start = performance.now();
            const resp = await fetch('/ping');
            if (resp.ok) {
                const end = performance.now();
                counter++;
                document.getElementById('counter').textContent = counter;
                document.getElementById('latency').textContent = (end - start).toFixed(2);
            } else {
                alert('Error en la petición');
            }
        }
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/ping")
def ping():
    time.sleep(0.05)  # 50 ms delay simulado
    return jsonify({"message": "pong"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
