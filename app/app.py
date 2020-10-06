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

    summa = str(int(number1) + int(number2))
    return render_template ('results.html', summa=summa)

if __name__== '__main__':
    app.run(debug=True)

