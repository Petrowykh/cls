# Новый проект

from flask import Flask, render_template, request


app = Flask(__name__)




@app.route('/')
def index():
    return render_template('index.html')

@app.route('/results', methods=['POST'])
def render_result():
    number1 = request.form['number1']
    number2 = request.form['number2']
    return "Summa: " + number1 + number2

if __name__== '__main__':
    app.run(debug=True)

