from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route('/')
def default():
    return "Hello! I am a home page"

@app.route('/quote', methods=['GET', 'POST'])
def home():
    from random_word import RandomWords
    from quote import quote

    r = RandomWords()
    w = r.get_random_word()
    print("Keyword Generated: ", w)

    res = quote(w, limit=1)
    data = "hello world"
    return jsonify({'data': res})


if __name__ == '__main__':
    app.run()
