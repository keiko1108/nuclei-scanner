from flask import Flask, request, render_template
import subprocess

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/scan", methods=["POST"])
def scan():
    target = request.form["target"]
    cmd = [
        "nuclei",
        "-u", target,
        "-json-export", "results/output.json",
        "-c", "3",          # รันพร้อมกันแค่ 3 thread (ปกติ 25)
        "-rl", "5",         # ส่ง request แค่ 5 ครั้ง/วินาที
        "-timeout", "5",    # หมดเวลา 5 วินาที/request
        "-t", "http/technologies"  # สแกนแค่ category เดียว ไม่สแกนทุก template
    ]
    subprocess.run(cmd)
    return "Scan completed"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
