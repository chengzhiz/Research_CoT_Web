from flask import Flask, render_template, request, jsonify
from dotenv import load_dotenv
from model import ask_chatgpt
import os

load_dotenv()

app = Flask(__name__, template_folder='templates', static_folder='static', static_url_path='/')

@app.route('/')
def index():
    return render_template('about.html')

@app.route('/interaction', methods=['GET', 'POST'])
def interaction1():
    # Load milestone1.html and pass an initial placeholder question
    question = "Waiting for a question..."
    answer = "waiting..."  # Set a default empty answer
    category = "waiting..."
    justification = "waiting..."
    return render_template('interaction.html', active='interaction1', question = question, 
                           answer = answer, category_name = category, justification = justification)

# New route to handle the ChatGPT question
@app.route('/ask-chatgpt', methods=['POST'])
def ask_chatgpt_route():
    data = request.get_json()
    user_input = data.get('question')  # Change this line to get 'question' instead of 'user_input'
    
    # Call the ask_chatgpt function and return its dictionary result directly
    response = ask_chatgpt(user_input)
    return jsonify(response)


@app.route('/takeaway')
def takeaway():
    return render_template('takeaway.html', active='takeaway')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
