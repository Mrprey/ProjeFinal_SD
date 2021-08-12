from flask import Flask, jsonify, request
from werkzeug.exceptions import abort

app = Flask(__name__)

datas = [
    {
        "title": 'Capitão América 2: O Soldado Invernal',
        "duration": '2h 16m'
    },
    {
        'title': 'The Avengers: Os Vingadores',
        'duration': '2h 24m',
    },
    {
        'title': 'Capitão América: Soldado Invernal',
        'duration': '3h 2m',
    },
    {
        'title': 'Homem de Ferro',
        'duration': '2h 6m',
    },
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
def post_movie():
    if not request.json or not 'title' in request.json:
        abort(400)
    message = {
        'title': request.json['title'],
        'duration': request.json['duration'],
    }

    datas.append(message)
    return jsonify({'data': datas[-1]})


if __name__ == "__main__":
    app.run(debug=True)
