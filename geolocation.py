from geopy.geocoders.osm import Nominatim
import geopy
from geopy import distance

def coordinates():
    geolocator = Nominatim(user_agent='geolocation')
    l = input(('Set coordinates\n>>>\t'))
    location = geolocator.reverse(l)
    print(location.address)
    print(location.latitude, location.longitude)

def address():
    geolocator = Nominatim(user_agent='geolocation')
    address = input('Set address\n>>>\t')
    location = geolocator.geocode((address))
    print(location.address)
    print(location.latitude, location.longitude)

def distanceCoordinates():
    geolocation = Nominatim(user_agent='geolocation')

    l = input('Set coordinates of first place:\n>>>\t')  # 54.766397 17.5595503/// 49.0081579, 22.8841572 /// 53.9159654 14.2675889
    m = input('Set coordinates of second place:\n>>>\t')

    location1 = geolocation.reverse(l)
    latitude1 = location1.latitude
    longitude1 = location1.longitude
    placeOne = (latitude1, longitude1)

    location2 = geolocation.reverse(m)
    latitude2 = location2.latitude
    longitude2 = location2.longitude
    placeTwo = (latitude2, longitude2)

    print('Distance: ',geopy.distance.geodesic(placeOne, placeTwo).km,'km')
    print(location1.address)
    print(location2.address)

def distanceAddress():
    geolocation = Nominatim(user_agent='geolocation')

    addressOne = input('Set address of first place:\n>>>\t')  # 54.766397 17.5595503/// 49.0081579, 22.8841572 /// 53.9159654 14.2675889
    addressTwo = input('Set address of second place:\n>>>\t')

    location1 = geolocation.geocode(addressOne)
    latitude1 = location1.latitude
    longitude1 = location1.longitude
    placeOne = (latitude1, longitude1)

    location2 = geolocation.geocode(addressTwo)
    latitude2 = location2.latitude
    longitude2 = location2.longitude
    placeTwo = (latitude2, longitude2)

    print('Distance: ', geopy.distance.geodesic(placeOne, placeTwo).km,'km')
    print(location1.address)
    print(location2.address)

i = input('Check information by:\n1 - set address\n2 - set coordinates\nor\nCheck the distanse between cities by:\n3 - coordinates\n4 - address\n>>>\t')
i = int(i)
if i == 1:
    address()
elif i == 2:
    coordinates()
elif i ==3:
    distanceCoordinates()
elif i == 4:
    distanceAddress()
else:
    print('Incorrect choice - end of program!')