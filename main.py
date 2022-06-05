
from flask import *
from low_iq_test import generateCaptcha


app = Flask(__name__)

@app.route("/")

def main_page():
	return render_template("index.html",
		title="low iq test",
		text=generateCaptcha()
	)



if __name__ == "__main__":
	app.run(debug = True)
