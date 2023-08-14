from flask import Flask, request, jsonify, session
import json
from modules import initializeBot

app = Flask(__name__)

genBooker = initializeBot()


@app.route('/')
def home():
    return jsonify(
        {
            'status': 'OK',
            'message': 'The api is ready.',
        }
    )





@app.route('/chat', methods=['POST'])
def receive_message():
    try:
        dict_str = request.data.decode("UTF-8")
        data = json.loads(dict_str)

        print(data)

        message = data['message']

        response = genBooker.chat(message)

        return jsonify(
            {
                'status': 'OK',
                'result': {
                    'answer': response,
                    'message':message
                }

            }
        ), 200

    except Exception as err:
        print(err)
        return jsonify(
            {
                'status': 'Failed',
                'message': "Something went wrong",

            }
        ), 400