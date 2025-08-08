from flask import Flask, render_template, request, jsonify
from model import run_agent

import warnings
warnings.filterwarnings('ignore')

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get('message')
    explanation_length = data.get('explanation_length', 'medium')
    bot_response = run_agent(user_message,explanation_length)

    return jsonify({"response": str(bot_response)})

if __name__ == '__main__':
    app.run(debug=True)
