from flask import Flask, render_template, jsonify, request
from pokemontcgsdk import Card
import json

app = Flask(__name__,
            template_folder='./public/',
            static_url_path='',
            static_folder='./public/')


## localhost:5000
@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')


@app.errorhandler(404)
def page_not_found(e):
    return "<h1>404</h1><p>The resource could not be found.</p>", 404


@app.route("/cards", methods=['GET'])
def getAllCards():
    ## Card.where(page=5, pageSize=100)
    card = Card.find('xy1-1')
    name = card.name
    print(name)
    return ('', 200)


@app.route("/card", methods=['GET'])
def getCard():
    name = request.args.get('name')
    cards = []
    try:
        cards = Card.where(name=name)
    except:
        return

    pokelista = []
    for card in cards:
        pokelista.append({
            'name': card.name,
            'imageUrl': card.image_url,
            'id': card.id
        })
    return (jsonify(pokelista), 200)

if __name__ == "__main__":
    app.run(debug=True)