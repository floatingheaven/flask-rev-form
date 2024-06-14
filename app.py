from flask import Flask,render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

ENV = 'dev'

if ENV == 'def':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Piwdiepay123localhost/lada'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:Piwdiepay123localhost/lada'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedvack()
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        rating = request.form.get('rating', False)
        comments = request.form['comments']
        friendrec = request.form.get('ratingf', False)
        # print(customer, dealer,  comments, friendrec, rating)
        if customer =='' or dealer == '':
            return render_template('index.html', message='Пожалуйста, заполните всю форму')
        return render_template('success.html')

if __name__ == '__main__':
    app.run()
