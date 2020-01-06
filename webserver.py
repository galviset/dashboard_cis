from flask import render_template
from flask import Flask

dashboard = Flask(__name__)

@dashboard.route('/')
@dashboard.route('/index')
def index():
    return render_template('index.html')

if __name__ == "__main__":
    dashboard.run(debug=True, port=80, host='127.0.0.1')
