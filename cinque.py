from flask import Flask, render_template
app = Flask(__name__)

@app.route('/') # L'utente richiede l'home page
def home():
  return render_template("index5.html")

@app.route('/unapersona') 
def singolo():
  return render_template("persona.html")

@app.route('/gruppo') 
def gruppo():
  return render_template("gruppo.html")

@app.route('/gruppoconguida') 
def gruppoconguida():
  return render_template("gruppoconguida.html")


if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)