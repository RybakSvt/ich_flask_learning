from flask import Flask

app = Flask(__name__)

@app.route('/')
def home_page() -> str:
	return "Hello, Flask!"

@app.route('/user/<string:user_name>')
def get_user_name(user_name: str) -> str:
	return f"Hello, '{user_name}'"


if __name__ == '__main__':
	app.run(debug=True)