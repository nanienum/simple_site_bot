from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/bot", methods=['GET'])
def start_bot():
    question = request.args['question']
    print("\tgot question", question)
    return "smth"


@app.route('/')
@app.route('/index')
def index():
    user = {'nickname': 'Supergood'}
    return render_template("index.html", title='Home', user=user)

if __name__ == '__main__':
    app.run(debug=True)
