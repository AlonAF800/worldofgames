from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def home():
    score = 500
    return render_template_string('<html><body><div id="score">{{ score }}</div></body></html>', score=score)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8777)
