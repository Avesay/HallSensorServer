from flask import Flask, request, render_template, abort, send_file, redirect, flash, Blueprint

main = Blueprint('main', __name__)
app = Flask(__name__)
app.config['SECRET_KEY'] = '9OLWxND4o83j4K4iuopO'

# Define a basic route and a function that will be called when accessing the root URL
@main.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    app.register_blueprint(main)
    app.run(host="0.0.0.0")  # Run the app in debug mode: debug=True
