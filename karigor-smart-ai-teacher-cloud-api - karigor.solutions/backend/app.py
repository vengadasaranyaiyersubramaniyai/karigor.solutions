from flask import Flask, request, jsonify
from chatbot import Chatbot

app = Flask(__name__)
chatbot = Chatbot()

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_input = data['message']
    response = chatbot.get_response(user_input)
    return jsonify({'message': response})

if __name__ == '__main__':
    app.run(debug=True)
