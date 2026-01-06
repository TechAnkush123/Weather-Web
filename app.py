print("App file is running...")
from flask import Flask, render_template, request
import requests

app = Flask(__name__)

API_KEY = "45a4f3922bb8c4a3294f9a79aff0afbc"
BASE_URL = "http://api.openweathermap.org/data/2.5/weather?"

@app.route("/", methods=["GET", "POST"])
def index():
    weather_data = None
    if request.method == "POST":
        city = request.form["city"]
        url = BASE_URL + "q=" + city + "&appid=" + API_KEY + "&units=metric"
        response = requests.get(url).json()
        if response.get("main"):
            weather_data = {
                "city": city,
                "temperature": response["main"]["temp"],
                "description": response["weather"][0]["description"].title(),
                "icon": response["weather"][0]["icon"]
            }
    return render_template("index.html", weather=weather_data)

if __name__ == "__main__":
    app.run(debug=True)