from flask import Flask, render_template
from getshows import get_shows
import pandas as pd
from time import sleep
from datetime import datetime
from flask_apscheduler import APScheduler


app = Flask(__name__)

# declare the global variable for storing show info with new structure
SHOWS = []

# For live implementation.  If this is the first time the server is running the code, make the API
# calls.  Otherwise, follow the scheduler's schedule.
INITIAL_RUN = 0

scheduler = APScheduler()


def call_shows(df):
    for index, row in df.iterrows():
        venue, band, date = get_shows(row["Venue Name"], row["vID"])
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%b %d, '%y")
        SHOWS.append([venue, band, date])
        sleep(0.09)


def job1():
    # Get the list of venues with their specific venue codes used in the API calls
    df = pd.read_csv("Listed_Venues.csv")

    call_shows(df)

    # # Make API calls and put event information into a list of lists
    # for index, row in df.iterrows():
    #     venue, band, date = get_shows(row["Venue Name"], row["vID"])
    #     date = datetime.strptime(date, "%Y-%m-%d").strftime("%b %d, '%y")
    #     SHOWS.append([venue, band, date])
    #     sleep(0.09)

if INITIAL_RUN == 0:
    job1()
    INITIAL_RUN = 1
else:
    pass


@app.route("/")
def index():
    return render_template("index.html", shows=SHOWS)


if __name__ == "__main__":
    scheduler.add_job(id="job1", func=job1, trigger="cron",
                      day_of_week="mon-sun", hour=00, minute=1)
    scheduler.start()
    app.run(debug=True, port=5001, use_reloader=False)


