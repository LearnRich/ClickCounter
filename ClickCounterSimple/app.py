from flask import Flask, url_for, redirect, render_template

app = Flask(__name__)

counter = 0

@app.route('/')
@app.route('/home/')
def landing_page():
    return render_template('home.html', counter=counter)

@app.route('/count/')
def count():
    global counter
    counter += 1
    return redirect(url_for('landing_page'))

if __name__ == '__main__':
    app.run(debug=True, host="127.0.0.1", port="8080")