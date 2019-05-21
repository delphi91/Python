#Calculate distance by formula
from geopy.geocoders.osm import Nominatim
import math

def distanceCoordinates():
    geolocation = Nominatim(user_agent='geolocation')
    l = input('Set coordinates of first place:\n>>>\t')
    m = input('Set coordinates of second place:\n>>>\t')

    location1 = geolocation.reverse(l)
    latitude1 = location1.latitude
    longitude1 = location1.longitude

    location2 = geolocation.reverse(m)
    latitude2 = location2.latitude
    longitude2 = location2.longitude

    result = math.sqrt(((latitude2-latitude1)**2)+((math.cos((latitude1*math.pi) / 180)*(longitude2-longitude1))**2))*(40075.704/360)
    print('Distance: ~',round(result,2),'km')

distanceCoordinates()