
# Iport python flask
from flask import Flask

# Import render_template
from flask import render_template
app = Flask(__name__)

@app.route('/')
def hello_world():
    # render index.html
    return render_template('index.html')

if __name__ == '__main__':
    app.run()