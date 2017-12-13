from flask import Flask,  render_template
from random import randint
import RPi.GPIO as GPIO
app = Flask(__name__)

GPIO.setmode(GPIO.BCM)

@app.route("/")
def hello():
    templateData = {

      }
    return render_template('main.html', **templateData)

@app.route("/readPin/")
def readPin():
    try:
      GPIO.setup(int(23), GPIO.IN)
    if GPIO.input(int(23)) == True:
         response = randint(0,10)
		if response <= 5:
			output="<font color="red">Nice!</font>"
		else
			output="<font color="red">Naughty!</font>"
    else:
         response = "not pressed"
			except:
		response = "There was an error reading pin " + 23 + "."

    templateData = {
      'title' : 'Status of Pin' + 23,
      'response' : response
	  'screenout' : output
      }

    return json.dumps(templateData)


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=125, debug=True)

			
			
			
			