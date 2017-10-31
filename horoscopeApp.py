from flask import Flask , render_template,request
from horoscope_api import get_horoscope, zodiac_sign
from datetime import datetime

app = Flask("My Flask App")


@app.route("/") 
def default_path():
	return render_template ("index.html") #This 


# 1. From the webpage take DOB as input
# 2. Using the DOB identify Zodiac Sign - The function to calculate sign is in horoscope_api.py to use this fuction we need to import see line 2
# 3. Once Sign is identified, we have a function that call REST API to get horoscope for the sign
# 4. The response from the API is in json format (baically name:value pair e.g {sign:leo, day:today})
# 5. Pass json data to the target HTML page that has logic to read data from the json
@app.route("/horoscope", methods=["POST"])
def read_form():
	form_data = request.form
	date = datetime.strptime(form_data["dob"], '%d-%m-%y').date()
	month = date.month
	day = date.day
	print date
	sign= zodiac_sign (month,day)
	print sign
	data = get_horoscope(sign)
	return render_template ("myhoroscope.html",data=data) 
	#return "All OK"


if __name__ == '__main__':
	app.run(debug=True)