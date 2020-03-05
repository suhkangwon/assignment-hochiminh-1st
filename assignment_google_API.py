import requests
import webbrowser

GOOGLE_MAPS_API_URL = 'https://www.google.com/maps/dir/?api=1'

params = {'origin': 'go dai hung thinh', 'destination': 'publik office', 'travelmode': 'walking',
          'key': ''}


req = requests.get(GOOGLE_MAPS_API_URL, params=params)


print(req.url)
webbrowser.open(req.url)
