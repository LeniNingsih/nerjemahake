from flask import Flask, render_template, request
import subprocess

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    source_text = request.form['source_text']
    
    # Simpan source_text ke file
    with open("data/source.txt", "w") as f:
        f.write(source_text)

    # Jalankan kode untuk menerjemahkan
    command = "onmt_translate -model data/model_step_2000.pt -src data/source.txt -output data/pred.txt"
    subprocess.run(command, shell=True)

    # Baca file pred.txt
    with open("data/pred.txt", "r") as f:
        pred_text = f.read()
    
    return pred_text

if __name__ == '__main__':
    app.run()
