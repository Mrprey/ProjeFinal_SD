from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

app = Flask(__name__)

datas = [
    {
        "nome": 'Arroz',
        "preco": '6.00'
    },
    {
        'nome': 'óleo',
        'preco': '9.00',
    },
    {
        'nome': 'soja',
        'preco': '4.00',
    },
        {
        'nome': 'pimentao',
        'preco': '4.00',
    },
            {
        'nome': 'macarrao',
        'preco': '4.00',
    },
            {
        'nome': 'leite em pó',
        'preco': '4.00',
    },
    {
        'nome': 'sal',
        'preco': '1.00',
    },
    {
        'nome': 'azeite',
        'preco': '13.00',
    },
        {
        'nome': 'vinagre',
        'preco': '4.00',
    },
        {
        'nome': 'miojo',
        'preco': '1.40',
    }
]


@app.route('/')
def index():
    return 'Welcome to the course API'


@app.route('/datas', methods=["GET"])
def get():
    return jsonify({"datas": datas})


@app.route('/datas/<int:data_id>', methods=["GET"])
def get_data(data_id):
    try:
        return jsonify({"data": datas[data_id]})
    except Exception as e:
        abort(404)


@app.route('/datas', methods=['POST'])
def post_iten():
    if not request.json or not 'nome' in request.json:
        abort(400)
    message = {
        'nome': request.json['nome'],
        'preco': request.json['preco'],
    }

    datas.append(message)
    return jsonify({'data': datas[-1]})


if __name__ == "__main__":
    app.run(debug=True)
