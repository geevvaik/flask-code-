from flask import Flask
from flask import render_template
app = Flask('server app')


@app.route('/')
def home():
    return render_template('home.html')

    
app = Flask(__name__, static_url_path='/static')


if __name__ == "__main__":
   app.run()
   

