from flask import Flask, render_template, url_for
import json

app = Flask(__name__)

def load_products():
    with open('products.txt', 'r') as file:
        products = json.load(file)
    return products

@app.route('/')
def index():
    products = load_products()
    return render_template('index.html', products=products)

if __name__ == '__main__':
    app.run(debug=True)
