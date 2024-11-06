from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')  # Main page of the application

@app.route('/process_command', methods=['POST'])
def process_command():
    command = request.json.get("command").lower()
    response = "Command not recognized."

    # Sample commands for navigation
    if "open module one" in command:
        response = "Opening Module One."
    elif "open module two" in command:
        response = "Opening Module Two."
    elif "go to quizzes" in command:
        response = "Navigating to Quizzes."
    elif "start course" in command:
        response = "Starting the course overview."

    return jsonify({"response": response})

if __name__ == '__main__':
    app.run(debug=True)
