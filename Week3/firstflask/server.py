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
    