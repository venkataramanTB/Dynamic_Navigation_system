import geocoder
from IP_address_find_pol import ip_address_pol
g = geocoder.ip(ip_address_pol)
lat1 = g.lat
lon1 = g.lng