from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = 'this key'

@app.route('/')
def route_index():
    return render_template('index.html')

@app.route('/handle_form', methods=['POST'])
def form_results():
    session['full_name']= request.form['full_name']
    session['city']= request.form['city']
    session['language']= request.form['language']
    session['Comment']=request.form['Comment']
    print(request.form)
    return redirect('/results')

@app.route('/results')
def show_results():
    return render_template('results.html')

if __name__ == '__main__':
    app.run(debug=True)