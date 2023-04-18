from flask import Flask, render_template, request
app = Flask(__name__)

import pandas as pd 
df = pd.read_excel("https://github.com/wtitze/3E/blob/main/BikeStores.xls?raw=true", sheet_name="customers")
df1 = df.groupby('state').count()[['customer_id']].reset_index().sort_values(by = 'customer_id', ascending = False )

@app.route("/", methods = ['GET'])
def home():
    return render_template("home.html")

@app.route("/nomecognomeinput", methods = ['get'])
def nomecognome():
    return render_template("nomecognomeinput.html")

@app.route("/risultatonome", methods = ['get'])
def risultatonome():
    nome = request.args.get('nome')
    cognome = request.args.get('cognome')
    nomeintero = df[(df['first_name'].str.contains(nome)) & (df['last_name'].str.contains(cognome))]
    return render_template("risultatonome.html", nomeintero = nomeintero.to_html())

@app.route("/cittàinput", methods = ['get'])
def cittàinput():
    return render_template("cittàinput.html")

@app.route("/risultatocittà", methods = ['get'])
def città():
    città = request.args.get('città')
    cittàintera = df[df['city'].str.contains(città)]
    return render_template("risultatocittà.html", cittàintera = cittàintera.to_html())

@app.route("/stato", methods = ['get'])
def stato():
    return render_template("stato.html")

@app.route("/numero", methods = ['get'])
def numero():
    return render_template("numero.html")

@app.route("/grafici", methods = ['get'])
def grafici():
    return render_template("grafici.html")

@app.route("/noMail", methods = ['get'])
def noMail():
    return render_template("noMail.html")

@app.route("/provider", methods = ['get'])
def provider():
    return render_template("provider.html")

if __name__ == '__main__':
  app.run(host='0.0.0.0', port=3245, debug=True)