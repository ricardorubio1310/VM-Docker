import requests
import time
import csv
import psutil
import os

url = "http://localhost:5000/ping"
duration = 60  # segundos
end_time = time.time() + duration
results = []

print("⏳ Ejecutando benchmark por 60 segundos...")
while time.time() < end_time:
    start = time.time()
    try:
        r = requests.get(url)
        latency = time.time() - start
        cpu = psutil.cpu_percent(interval=0.1)
        mem = psutil.virtual_memory().percent
        results.append([latency, cpu, mem])
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(0.2)

is_vm = input("¿Estás ejecutando esto en una VM? (s/n): ").strip().lower() == 's'
env_label = 'vm' if is_vm else 'docker'
filename = f"benchmark_simple_{env_label}.csv"
filepath_csv = f"../results/{filename}"

os.makedirs("../results", exist_ok=True)

with open(filepath_csv, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["latency", "cpu_percent", "memory_percent"])
    writer.writerows(results)

latencias = [r[0] for r in results]
cpus = [r[1] for r in results]
mems = [r[2] for r in results]

avg_latency = sum(latencias) / len(latencias)
max_latency = max(latencias)
min_latency = min(latencias)

avg_cpu = sum(cpus) / len(cpus)
max_cpu = max(cpus)
min_cpu = min(cpus)

avg_mem = sum(mems) / len(mems)
max_mem = max(mems)
min_mem = min(mems)

base_path = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
total_size = 0
for dirpath, dirnames, filenames in os.walk(base_path):
    for f in filenames:
        fp = os.path.join(dirpath, f)
        if os.path.exists(fp):
            total_size += os.path.getsize(fp)
disk_mb = total_size / (1024 * 1024)

total_requests = len(results)
errores = 0
network_mb = total_requests * len("dummy-response") * 0.001 / 1024

print(f"\n📊 RESUMEN DEL BENCHMARK")
print(f"📁 Entorno: {'VM' if is_vm else 'Docker'} — {base_path}")
print(f"🧠 RAM promedio: {avg_mem:.2f}%")
print(f"⚙️  CPU promedio: {avg_cpu:.2f}%")
print(f"⏱️  Latencia promedio: {avg_latency*1000:.2f} ms")
print(f"🔺 Latencia máx: {max_latency*1000:.2f} ms")
print(f"🔻 Latencia mín: {min_latency*1000:.2f} ms")
print(f"🔥 CPU máx: {max_cpu:.2f}%")
print(f"🧊 CPU mín: {min_cpu:.2f}%")
print(f"📈 RAM máx: {max_mem:.2f}%")
print(f"📉 RAM mín: {min_mem:.2f}%")
print(f"💾 Tamaño del entorno en disco: {disk_mb:.2f} MB")
print(f"📨 Total de peticiones: {total_requests}")
print(f"❌ Errores: {errores} ({(errores/total_requests)*100 if total_requests else 0:.2f}%)")
print(f"🌐 Tráfico de red: {network_mb:.2f} MB")
print(f"⏱️  Tiempo total medido: {duration - (end_time - time.time()):.2f} segundos")
print(f"✅ CSV guardado en: {filepath_csv}")
