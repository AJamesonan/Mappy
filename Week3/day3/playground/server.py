from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def playground(x=1, color='aqua'):
    print('I AM HERE')
    return render_template('index.html', x=x, color=color)

@app.route('/play/<int:x>/<color>')
def play_select(x,color):
    return render_template('index.html', x=x, color=color)





if __name__ == '__main__':
    app.run(debug=True)


