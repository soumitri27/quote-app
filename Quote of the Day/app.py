from flask import Flask, render_template
import random
from quotes import quotes_list

app = Flask(__name__)

@app.route('/')
def index():
    quote = random.choice(quotes_list)
    return render_template('index.html', quote=quote)

if __name__ == '__main__':
    app.run(debug=True)
