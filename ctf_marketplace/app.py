from flask import Flask, render_template, jsonify, request

app = Flask(__name__)

class Product:
    def __init__(self, name, price, image):
        self.name = name
        self.price = price
        self.image = image

products = [
    Product("Nuggeta", 0, "image.png"),
    Product("Nuggetb", 1.49, "image.png"),
    Product("Nuggetc", 1.49, "image.png"),
    Product("Nugget", 1.49, "image.png"),
    Product("Flag", 9999.99, "image.png"),
    Product("Nugget", 1.49, "image.png")
]

@app.route('/')
def index():
    return render_template('index.html', products=products, balance=1)

@app.route('/buy', methods=['POST'])
def buy():
    item_name = request.json.get('item_name')
    for product in products:
        if product.name == item_name:
            if product.price <= 1:
                if product.name == "Flag":
                    return jsonify({"message": "🏳️ Flag bought! 🏳️"})
                return jsonify({"message": "item bought"})
            else:
                return jsonify({"message": "Insufficient funds"}), 403
    return jsonify({"message": "Item not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
