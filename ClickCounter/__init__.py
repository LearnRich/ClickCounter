from flask import Flask

counter = 0

def create_app():
	app = Flask(__name__)
	app.config.from_object('config.Config')
	
	from .main import main

	app.register_blueprint(main.home)

	return app
