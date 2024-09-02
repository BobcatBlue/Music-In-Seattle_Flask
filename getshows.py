import requests
from datetime import datetime
import os


API_KEY = os.getenv("show_data_api")
URL_1 = os.getenv("URL_1")
URL_2 = os.getenv("URL_2")


def get_shows(venue_name, venueId):
    url = f"{URL_1}{venueId}{URL_2}{API_KEY}"

    response = requests.get(url)
    show_data = response.json()
    try:

        # Find the next show/earliest date in the list
        all_events = show_data.get('_embedded').get('events')
        list_length = len(all_events)
        date_list = []
        counter = 0
        while counter < list_length:
            date = show_data.get('_embedded')['events'][counter].get('dates').get('start').get('localDate')
            date = datetime.strptime(date, "%Y-%m-%d")
            counter += 1
            date_list.append(date)
        earliest = min(date_list)
        earliest_index = date_list.index(earliest)


        show_events: list = show_data.get('_embedded').get('events')
        next_show = show_events[earliest_index]
        return venue_name, \
            next_show.get('name'), next_show.get('dates').get('start').get('localDate')

    except Exception:
        band = "No info"
        date = "No info"
        return venue_name, band, date


if __name__ == "__main__":
    get_shows("The Crocodile", "KovZpZA1vFtA")