from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="wazeyes") # Nome do seu aplicativo
location = geolocator.reverse("-23.5703022, -46.6451267")

print(location.address)
print((location.latitude, location.longitude))