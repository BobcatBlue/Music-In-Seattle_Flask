from flask import Flask, render_template
from getshows import get_shows
import pandas as pd
from time import sleep


app = Flask(__name__)


file_name = "Output.csv"
df = pd.read_csv("Listed_Venues.csv")

"""
# create an empty dictionary to hold the show information
shows_tonight = {
    "venue": [],
    "show": [],
    "date": [],
}


# make the API calls to get show information and store it in the shows_tonight dictionary
for index, row in df.iterrows():
    venue, band, date = get_shows(row["Venue Name"], row["vID"])
    shows_tonight["venue"].append(venue)
    shows_tonight["show"].append(band)
    shows_tonight["date"].append(date)
    sleep(0.09)
"""

"""
# declare the OLD global variable
SHOW_INFO = list(zip(shows_tonight["venue"], shows_tonight["show"], shows_tonight["date"]))
"""

# declare the NEW global variable for storing show info with new structure
SHOWS = []

# Test loop for restructuring how the information is stored
for index, row in df.iterrows():
    venue, band, date = get_shows(row["Venue Name"], row["vID"])
    SHOWS.append([venue, band, date])
    sleep(0.09)

"""
# convert the dictionary to a pandas dataframe
df_show_data = pd.DataFrame(shows_tonight)
df_show_data.to_csv(file_name, index=False)

# test code to output and verify the contents that get_shows() has returned
print(df_show_data.to_string())
print(shows_tonight)
"""


@app.route("/")
def index():

    return render_template("index.html", shows=SHOWS)


app.run(debug=True, port=5001)

