from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html', phrase ='Hello', times=5)

@app.route('/hello')
def hello():
    return 'hello'

@app.route('/dojo')
def dojo():
    return 'Dojo!'

@app.route('/say/<string:name>')
def say_name(name):
    print (name)
    return 'Hi ' + name + '!'

@app.route('/repeat/<int:mult>/<string:word>')
def word_mult(mult,word):
    print(mult)
    print(word)
    return render_template('index.html', mult= mult, word= word) 

if __name__ == '__main__':
    app.run(debug=True)

