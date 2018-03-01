from flask import Flask, request, render_template, redirect, url_for
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route('/fill', methods=['POST', 'GET'])
def get_user_data():
    error = None
    if request.method == 'POST':
        error = check_error(request)

        if error != None:
            return render_template('form.html', error=error)
        else:
            # your_10_minute_function_call() 
            return redirect(url_for('index'))
    return render_template('form.html')
        

def check_error(request):
    if request.form['data1'] == "":
        return "Please check form data"
    if request.form['data2'] == "":
        return "data2 error"
    if request.form['data3'] == "":
        return "data3 error"
    if request.form['data4'] == "":
        return "data4 error"
