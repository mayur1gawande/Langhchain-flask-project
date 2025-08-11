from flask import Flask, render_template, request, jsonify
from model import run_agent
import os

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
    explanation_length = data.get('explaination_length', 'medium')
    bot_response = run_agent(user_message,explanation_length)

    return jsonify({"response": str(bot_response)})

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(debug=False,host='0.0.0.0',port=port)


