from flask import Flask
from views import views

# create Flask app instance
app = Flask(__name__)

# register views blueprint
app.register_blueprint(views)

# run the Flask app if executed as the main script
if __name__ == '__main__':
    app.run(debug=False)
