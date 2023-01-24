import geocoder
from IP_address_find_vic import ip_address_vic
g = geocoder.ip(ip_address_vic)

lat2 = g.lat
lon2 = g.lng