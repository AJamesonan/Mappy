<<<<<<< HEAD
from flask import Flask, render_template, request, redirect #import flask class
app = Flask(__name__) #made an instance of the Flask class called "app"
@app.route('/') #set up a routing rule using the "@" decorator with the route method: @app. route("/route_string"). The routing rule is associated with the function immediately following it.
def hello_world():
    return render_template('index.html')

@app.route('/users', methods=['POST'])
def create_user():
    print ('Got Post info')
    print(request.form)
    return redirect('/')









if __name__=="__main__": 
    app.run(debug=True)
    # runs the app! This takes all of our routing rules that we set up and actually starts up the server.
=======
from flask import Flask #import flask class
app = Flask(__name__) #made an instance of the Flask class called "app"
@app.route('/') #set up a routing rule using the "@" decorator with the route method: @app. route("/route_string"). The routing rule is associated with the function immediately following it.
def hello_world():
    return "Hello World"


@app.route('/success')
def success():
    return 'success'

@app.route('/hello/<string:name>')
def hello(name):
    print(name)
    return 'Hello, ' + name









if __name__=="__main__": 
    app.run(debug=True)
    # runs the app! This takes all of our routing rules that we set up and actually starts up the server.
>>>>>>> 8a4770cb25b054a607ca935dd43ab4814dc86942
    