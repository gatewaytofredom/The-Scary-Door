from flask import Flask,  render_template
from random import randint
import json

app = Flask(__name__)


@app.route("/")
def hello():
  templateData = {}
  return render_template('main.html', **templateData)

@app.route("/readPin/")
def readPin():
  response = randint(0,10)
  if response <= 5:
    output="Nice"
  else:
    output="Naughty"

  templateData = {
    'title' : 'Status of Pin' + str(23),
    'response' : response,
    'screenout' : output
  }

  return json.dumps(templateData)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=125, debug=True)

			
			
			
			