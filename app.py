from flask import Flask, jsonify, request

app = Flask(__name__)

devs = [
    {
        'id': 1,
        'name': 'Jeftar Mascarenhas',
        'lang': 'javascript'
    },
    {
        'id': 2,
        'name': 'Kevin Mascarenhas',
        'lang': 'python'
    },
    {
        'id': 3,
        'name': 'Cauã Thiago da Silva',
        'lang': 'python'
    }
]

@app.route('/devs', methods=['GET'])
def home():
    return jsonify(devs), 200

@app.route('/devs/<string:lang>', methods=['GET'])
def devs_per_lang(lang):
    devs_per_lang = [dev for dev in devs if dev['lang'] == lang]
    return jsonify(devs_per_lang), 200

@app.route('/devs/<int:id>', methods=['GET'])
def devs_per_id(id):
    for dev in devs:
        if dev['id'] == id:
            return jsonify(dev), 200
    return jsonify({'error': 'not found'}), 400

@app.route('/devs', methods=['POST'])
def save_dev():
    data = request.get_json()
    devs.append(data)
    return jsonify(devs), 201

if __name__ == '__main__':
    app.run(debug=True)
