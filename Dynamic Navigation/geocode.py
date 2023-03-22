import geocoder
from googleplaces import GooglePlaces, types, lang
import requests
import json

# Requesting for API
send_url = 'https://cloud.google.com /maps-platform/places/?apis =AIzaSyAu-w7TJnBSZdUIf4vT22teotIEIJ8l2eA'
r = requests.get(send_url)
j = json.loads(r.text)
print(j)
lat = j['latitude']
lon = j['longitude']
  
# Getting the Location
g1 = geocoder.ip('me')
print(g1.latlng)
latitude1 = g1.lat
longitude1 = g1.lng
print(latitude1)
print(longitude1)

# getting the location of the nearby ps

API_KEY = 'AIzaSyAu-w7TJnBSZdUIf4vT22teotIEIJ8l2eA'
google_places = GooglePlaces(API_KEY)
query_result = google_places.nearby_search(
        # lat_lng ={'lat': 46.1667, 'lng': -1.15},
        lat_lng ={'lat': 28.4089, 'lng': 77.3178},
        radius = 5000,
        types =[types.TYPE_POLICE])
if query_result.has_attributions:
    print (query_result.html_attributions)
for place in query_result.places:
    print(place)
    # place.get_details()
    print (place.name)
    print("Latitude", place.geo_location['lat'])
    print("Longitude", place.geo_location['lng'])
    print()
  

