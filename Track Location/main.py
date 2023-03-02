import phonenumbers
import io
from myphone import number
import opencage


from phonenumbers import geocoder

pepnumber = phonenumbers.parse(number)
location = geocoder.description_for_number(pepnumber,"en")
print(location)


from phonenumbers import carrier
service_pro = phonenumbers.parse(number)
print(carrier.name_for_number(service_pro,"en"))

# from opencage.geocoder import OpenCageGeocode

# key ='b9b0d8a6278846669dce669c8a1d15fb'
# geocoder= OpenCageGeocode(key)
# query = str(location)
# results= geocoder.geocode(query)
# print(results)

# lat = results[0][]
