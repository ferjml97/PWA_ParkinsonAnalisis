from flask import Flask, flash
from flask import render_template
from flask import Response
import subprocess
import requests

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/my-link/")
def my_link():
    files = {'audio': open("fer_audio.wav", 'rb')}
    # Send the HTTP request and get the reply
    reply = requests.post("https://morning-brushlands-40885.herokuapp.com/features_extract", files=files)
    #reply = requests.post("http://127.0.0.1:5000/features_extract", files=files)
    print(reply)
    print(reply.text)
    guardar = reply.text
    respuesta = ""
    if guardar == 'Patient does not have parkinson':
        respuesta = 'Paciente usted no tiene Parkinson'

    return render_template("results.html", respuesta = respuesta ) 

@app.route("/envio2")
def envio2():
    return render_template("envio2.html")

@app.route("/results")
def results():
    return render_template("results.html")

@app.route('/sw.js')
def sw():
    return app.send_static_file('sw.js')

if __name__ == "__main__":
    app.run()

'''
@app.route("/grabar")
def grabar():
    return render_template("grabar.html")
    
@app.route('/run')
def run():
   result = subprocess.check_output( ['python', 'peticion.py', '-i', 'test.txt'] )
   #result = subprocess.check_output("python peticion.py", shell=True)
   return render_template('results.html', **locals())

@app.route('/generate')
def generate():
   print( 'Hello World!')
   flash('Process complete!')
   return render_template('home.html')
'''
