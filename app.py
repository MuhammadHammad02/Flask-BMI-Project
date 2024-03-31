from flask import Flask, render_template, request
from waitress import serve  

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def calculate():
    bmi = 0
    if request.method== 'POST' and 'weight' in request.form:
        w = float(request.form.get('weight'))
        h = float(request.form.get('height'))
        bmi = round(w/((h/100)** 2),2)
    return render_template('index.html',bmi=bmi)

if __name__ == '__main__':
     serve(app, host="0.0.0.0", port=8000)