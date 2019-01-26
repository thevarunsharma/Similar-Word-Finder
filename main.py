from flask import Flask, render_template, request
import mlcode as ml

app = Flask(__name__)

@app.route("/", methods=["POST", "GET"])
def main():
    if request.method=="POST":
        data = request.form
        word = data['word'].lower()
        sim = ml.get_similar_words(word)
        found = True
        if sim=="Word not in vocabulary!":
            found = False
        return render_template('main.html', after_srch=True, found=found, word=word, results=sim)
    return render_template('main.html', after_srch=False)

app.config["TEMPLATES_AUTO_RELOAD"] = True
#app.run(debug=True)
