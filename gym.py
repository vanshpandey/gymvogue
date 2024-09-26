from flask import Flask, render_template,json

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/productdetail')
def productdetail():
    return render_template('productdetail.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/bags')
def dufflebags():
    # Load the bags data from JSON file
    with open('bags.json') as f:
        bags = json.load(f)["bags"]
    return render_template('dufflebags.html', bags=bags)


if __name__ == '__main__':
    app.run(debug=True, host='192.168.1.34')
