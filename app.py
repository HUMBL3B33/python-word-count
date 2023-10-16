from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        data = request.form
        if 'word' not in data:
            return jsonify(error='Please provide a "word" in the form'), 400

        word = data['word']
        word_length = len(word)

        return render_template('result.html', word=word, length=word_length)
    return render_template('index.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
