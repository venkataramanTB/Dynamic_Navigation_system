from geopy.distance import geodesic
# from location_co_ordinates_Police import lat1,lon1
from location_co_ordinates_Vic import lat2,lon2
pol_loc = [	48.856614, 	2.352222]
vic_loc = [lat2 , lon2]
print(geodesic(pol_loc, vic_loc).kilometers,"kms")
dis = geodesic(pol_loc, vic_loc).kilometers



