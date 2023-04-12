from pygeocoder import Geocoder

api_key = 'AIzaSyAvthhsE-7RRe1NV9kELYDWwGmVAWaBL-8'
endereco = 'Lins de Vasconcelos, 1222 Sao Paulo'

resultado = Geocoder(api_key).geocode(endereco)

print(resultado)