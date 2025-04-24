from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for cross-origin requests

def generate_bot_response(user_message):
    user_message = user_message.lower()
    
    if 'hello' in user_message:
        return "Hello! How can I assist you today?"
    elif 'order' in user_message:
        return "For order inquiries, please visit our orders page."
    elif 'contact' in user_message:
        return "You can reach us at support@example.com"
    elif 'bye' in user_message:
        return "Goodbye! Have a great day!"
    elif 'help' in user_message:
        return "I can help with general inquiries. Ask me about orders, contact info, or services!"
    else:
        return "I'm still learning. Could you please rephrase that?"

@app.route('/api/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message', '')
    bot_response = generate_bot_response(user_message)
    return jsonify({'response': bot_response})

if __name__ == '__main__':
    app.run(debug=True)