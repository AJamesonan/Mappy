from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'counter key'

@app.route('/')
def landing():
    if 'counter_number' not in session:
        session['counter_number'] = 0
    session['counter_number'] +=1
    return render_template('index.html')

@app.route('/counter')
def counter_update():
    if 'counter_number' not in session:
        session['counter_number'] = 0
    session['counter_number'] +=1

    return redirect('/')

@app.route('/reset')
def counter_reset():
    if 'reset' not in session:
        session['counter_number'] = 0

    return redirect('/')




@app.route("/show")
def show_user():
    print("clicked")
    print(request.ancor)
    return render_template("show.html")


if __name__ == '__main__':
    app.run(debug=True)