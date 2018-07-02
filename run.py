# Import libraries
from flask import Flask
from App.controllers import controller


app = Flask(__name__)
app.register_blueprint(controller, url_prefix="/")

if __name__ == "__main__":
	app.run(debug=True,
         host= "0.0.0.0")
