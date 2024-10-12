from flask import Flask, render_template
from getshows import get_shows
import pandas as pd
from time import sleep
from datetime import datetime
from flask_apscheduler import APScheduler


app = Flask(__name__)

# declare the global variable for storing show info with new structure
SHOWS = []

print("SHOWS variable has been declared.")

# For live implementation.  If this is the first time the server is running the code, make the API
# calls.  Otherwise, follow the scheduler's schedule.
INITIAL_RUN = 0
print(f"INITIAL RUN = {INITIAL_RUN}")

scheduler = APScheduler()


##################################################################################################
##################################################################################################
"""
This section is going to contain all of the functions needed to get show information.  Before, you 
thought it was silly to have job1() calling call_shows(), but that's not the case because job1() is
also going to be calling all of the scraping modules you develop for the venues that are truly local
and hosting local bands, all which also need to be scheduled.  Silly goose, you were right all along
:)

"""


def call_shows(df):
    print("Ring ring!!!  I'm inside call_shows(), calling the API")
    for index, row in df.iterrows():
        venue, band, date = get_shows(row["Venue Name"], row["vID"])
        date = datetime.strptime(date, "%Y-%m-%d").strftime("%b %d, '%y")
        SHOWS.append([venue, band, date])
        sleep(0.09)


def scrape_highdive():
    pass


def scrape_bluemoontavern():
    pass


def scrape_connorbyrne():
    pass


def scrape_centralsaloon():
    pass


def scrape_tractortavern():
    pass


def job1():
    # Get the list of venues with their specific venue codes used in the API calls
    df = pd.read_csv("Listed_Venues.csv")

    # Make the API calls and pull the event information
    call_shows(df)

    print(f"Ring ring!!!  I'm inside job1() and calling call_shows().\n"
          f"INITIAL RUN = {INITIAL_RUN}")

##################################################################################################
##################################################################################################




if INITIAL_RUN == 0:
    job1()
    INITIAL_RUN = 1
else:
    pass

print(f"INITIAL RUN = {INITIAL_RUN}")


@app.route("/")
def index():
    global SHOWS
    return render_template("index.html", shows=SHOWS)


if __name__ == "__main__":
    scheduler.add_job(id="job1", func=job1, trigger="cron",
                      day_of_week="mon-sun", hour=6, minute=00)
    scheduler.start()
    app.run(debug=True, port=5001, use_reloader=False, host="0.0.0.0")


@app.route("/Contact_Us")
def contact_us():
    pass

