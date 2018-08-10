from flask import Flask, request, render_template
from site_bot import get_answer

app = Flask(__name__)


@app.route("/bot", methods=['GET'])
def start_bot():
    question = request.args['question']
    print("\tgot question", question)
    return get_answer(question)


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Supergood'}
    return render_template("index.html", title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True)
