from flask import Flask, render_template, request
import codecs
app = Flask(__name__)

@app.route('/', methods=['GET'])
def index():
    return render_template("index.html")

@app.route('/history', methods=['POST', 'GET'])
def history():
    file = codecs.open("note.txt", "r", "utf-8")
    lines = file.readlines()
    file.close()
    return render_template("history.html", lines=lines)

@app.route('/add', methods=['POST'])
def add():
    title = request.form['title']
    content = request.form['content']
    file = codecs.open("note.txt", "a", "utf-8")
    file.write(title + "," + content + "\n")
    file.close()
    return render_template("add.html", title=title, content=content)

if __name__ == "__main__":
    app.run(debug=True)