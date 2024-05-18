# save this as app.py
from flask import Flask, request, render_template
from markupsafe import escape
app = Flask(__name__)

post = [
	{
		
	}
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/about')
def about():
	return render_template('about.html')

if __name__ == "__main__":
	app.run(debug=True)