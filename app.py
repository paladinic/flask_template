from flask import Flask, url_for, render_template
import os

# App config.
DEBUG = True
app = Flask(__name__)
app.config.from_object(__name__)
app.config['SECRET_KEY'] = '7d441f27d441f27567d441f2b6176a'

# index
@app.route("/", methods=['GET', 'POST'])
def index():
    return render_template('index.html')

# index
@app.route("/page2", methods=['GET', 'POST'])
def page2():
    return render_template('page2.html')

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port = port, host="0.0.0.0")

