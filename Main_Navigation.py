from geopy.distance import geodesic
from location_co_ordinates_Police import lat1,lon1
from location_co_ordinates_Vic import lat2,lon2
pol_loc = [lat1, lon1]
vic_loc = [lat2 , lon2]
print(geodesic(pol_loc, vic_loc).kilometers,"kms")
dis = geodesic(pol_loc, vic_loc).kilometers
