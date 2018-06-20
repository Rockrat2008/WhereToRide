#  AUTHOR:  Michael O'Brien
#  CREATED:  19 June 2018
#  UPDATED:  20 June 2018
#  DESCRIPTION:  Simple Website


from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def home():
    return render_template('home.html')


@app.route('/about/')

def about():
    return render_template('about.html')


@app.route('/bike shops')

def stores():
    return render_template('bike_shops.html')


@app.route('/map/')

def map():
    return render_template('map.html')


if __name__ == '__main__':
    app.run(debug = True)
