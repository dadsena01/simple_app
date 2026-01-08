from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form['username']
        return f"Hello <span style='color: blue;'>{name}</span>, welcome to the app!"
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)