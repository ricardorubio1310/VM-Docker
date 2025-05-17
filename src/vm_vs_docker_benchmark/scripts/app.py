from flask import Flask, render_template_string, jsonify
import time

app = Flask(__name__)

HTML_PAGE = """
<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8" />
    <title>Benchmark Mejorado</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet"/>
</head>
<body class="bg-light">
    <div class="container py-5">
        <div class="text-center mb-4">
            <h1 class="display-5">Benchmark de Latencia</h1>
            <p class="lead">Simula latencia y mide el rendimiento de tu entorno</p>
        </div>

        <div class="text-center mb-4">
            <button id="pingBtn" class="btn btn-success me-2">Enviar Ping</button>
            <button id="resetBtn" class="btn btn-danger">Reiniciar</button>
        </div>

        <div class="text-center mb-4">
            <p><strong>Respuestas:</strong> <span id="counter">0</span></p>
            <p><strong>Última latencia:</strong> <span id="latency">-</span> ms</p>
            <p><strong>Promedio:</strong> <span id="average">-</span> ms</p>
        </div>

        <div class="table-responsive">
            <table class="table table-striped table-bordered">
                <thead class="table-dark">
                    <tr>
                        <th>#</th>
                        <th>Latencia (ms)</th>
                    </tr>
                </thead>
                <tbody id="historyTable"></tbody>
            </table>
        </div>
    </div>

    <script>
        let counter = 0;
        let latencias = [];

        document.getElementById('pingBtn').onclick = async () => {
            const start = performance.now();
            const resp = await fetch('/ping');
            const end = performance.now();

            if (resp.ok) {
                const latency = (end - start).toFixed(2);
                latencias.push(parseFloat(latency));
                counter++;
                document.getElementById('counter').textContent = counter;
                document.getElementById('latency').textContent = latency;
                document.getElementById('average').textContent = (
                    latencias.reduce((a, b) => a + b, 0) / latencias.length
                ).toFixed(2);

                const row = `<tr><td>${counter}</td><td>${latency}</td></tr>`;
                document.getElementById('historyTable').insertAdjacentHTML('beforeend', row);
            } else {
                alert('Error en la petición');
            }
        };

        document.getElementById('resetBtn').onclick = () => {
            counter = 0;
            latencias = [];
            document.getElementById('counter').textContent = 0;
            document.getElementById('latency').textContent = '-';
            document.getElementById('average').textContent = '-';
            document.getElementById('historyTable').innerHTML = '';
        };
    </script>
</body>
</html>
"""

@app.route("/")
def index():
    return render_template_string(HTML_PAGE)

@app.route("/ping")
def ping():
    time.sleep(0.05)  # 50 ms simulated delay
    return jsonify({"message": "pong"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
