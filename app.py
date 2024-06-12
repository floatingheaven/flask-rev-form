from flask import Flask,render_template, request

app = Flask(__name__)

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
        print(customer, dealer,  comments, friendrec, rating)
        return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
