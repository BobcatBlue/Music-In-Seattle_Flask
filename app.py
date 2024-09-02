from flask import Flask, render_template
from getshows import get_shows
import pandas as pd
from time import sleep


app = Flask(__name__)


file_name = "Output.csv"
df = pd.read_csv("Listed_Venues.csv")

# declare the global variable for storing show info with new structure
SHOWS = []

# Test loop for restructuring how the information is stored
for index, row in df.iterrows():
    venue, band, date = get_shows(row["Venue Name"], row["vID"])
    SHOWS.append([venue, band, date])
    sleep(0.09)


@app.route("/")
def index():

    return render_template("index.html", shows=SHOWS)


app.run(debug=True, port=5001)

