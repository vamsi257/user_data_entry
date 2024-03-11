# from flask import Flask, render_template, request
# import json

# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
# def index():
#     if request.method == 'POST':
#         data = {
#             'name': request.form['name'],
#             'address': request.form['address'],
#             'phone': request.form['phone'],
#             'email': request.form['email']
#         }
#         with open('data.json', 'a') as f:
#             json.dump(data, f)
#             f.write('\n')
#         return 'Data saved successfully!'
#     return render_template('index.html')

# if __name__ == '__main__':
#     app.run(debug=True)
from flask import Flask, render_template, request
import json

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = {
            'name': request.form['name'],
            'address': request.form['address'],
            'phone': request.form['phone'],
            'email': request.form['email']
        }
        with open('data.json', 'a') as f:
            json.dump(data, f)
            f.write('\n')
        return render_template('submitted.html', data=data)  # Render submitted.html and pass data
    return render_template('index.html')

@app.route('/display')
def display():
    all_data = []
    with open('data.json', 'r') as f:
        for line in f:
            all_data.append(json.loads(line))
    return render_template('display.html', all_data=all_data)

if __name__ == '__main__':
    app.run(debug=True)
