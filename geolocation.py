from geopy.geocoders.osm import Nominatim

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

i = input(' 1 - set address\nor\n2 - set coordinates\n>>>\t')
i = int(i)
if i == 1:
    address()
elif i == 2:
    coordinates()
else:
    print('Incorrect choice - end of program!')
