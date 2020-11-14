from flask import Flask, render_template

app = Flask(__name__,
            template_folder='./public/',
            static_url_path='',
            static_folder='./public/')

@app.route("/")
@app.route("/home")
@app.route("/index")
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.run()