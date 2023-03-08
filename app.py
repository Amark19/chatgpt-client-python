# flask app to create a REST API for the client service can communicate to chatgpt client

from flask import Flask, request, jsonify
from chatgpt_wrapper import ChatGPT

app = Flask(__name__)
gpt = ChatGPT()


@app.route('/chat/question', methods=['POST'])
def question():
    args = request.args
    body_json = request.get_json()
    question = body_json['question']
    if args.get('debug', default= False):
        print(f"Question you ask to chatgpt is: {question}")

    response = gpt.ask(question)

    if args.get('debug', default= False):
        print(f"Response for a question that you ask to chatgpt is: {response}")

    return response

@app.route('/chat/response', methods=['GET'])
def reply():
    return jsonify("ok")


if __name__ == '__main__':
    app.run(debug=False, threaded=False)
