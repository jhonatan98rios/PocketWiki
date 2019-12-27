import wikipedia
from flask import Flask, jsonify, request

app = Flask(__name__)
wikipedia.set_lang("pt")

@app.route('/', methods=['GET']) #Recebe um argumento na rota
def hello():
    hello = [{
        "description": "Realize consultas na Wiki, de forma rapida e intuitiva",
        "title": "Pocket Wiki"
    }]

    return jsonify(hello)

@app.route('/<string:query>', methods=['GET']) #Recebe um argumento na rota
def pesquisa(query):    
    results = wikipedia.search(query)
    wiki = wikipedia.summary(results[0], sentences=5)
    
    busca = {
        "description": wiki,
        "title": query
    }

    return jsonify(busca), 200 #Retorna todos os devs filtrados

if __name__ == '__main__':
    app.run(debug=True)





