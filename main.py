# app.py

from flask import Flask, render_template, request
import requests

app = Flask(__name__)

# URL de l'API Open Food Facts
API_URL = "https://world.|/api/v0/product/{}.jsoxxssxzzsn"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/scan', methods=['POST'])
def scan():
    barcode = request.form['barcode']
    # Appel de l'API Open Food Facts avec le code-barres scanné
    response = requests.get(API_URL.format(barcode))
    if response.status_code == 200:
        # Si la réponse est réussie, récupère les données du produit
        product_data = response.json()
        # Récupère les informations pertinentes du produit
        product_name = product_data['product']['product_name'] if 'product' in product_data and 'product_name' in product_data['product'] else 'N/A'
        product_composition = product_data['product']['ingredients_text'] if 'product' in product_data and 'ingredients_text' in product_data['product'] else 'N/A'
        return render_template('result.html', name=product_name, composition=product_composition)
    else:
        return "Erreur: Impossible de récupérer les informations du produit."

if __name__ == '__main__':
    app.run(host='0.0.0.0')
