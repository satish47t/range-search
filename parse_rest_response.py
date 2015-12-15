import json
from pprint import pprint
json_text = ''
json_text_list = []

def quote(str):
    return "'" + str + "',"

with open('output.json') as in_file:
    data = json.load(in_file)
display_phone = ''
id  = ''
is_claimed = True
is_closed = False
address = ''
city = ''
latitude = 0.0
longitude = 0.0
country_code = ''
display_address = ''
geo_accuracy = 0.0
postal_code = 0
state_code = ''
name = ''
phone = ''
rating = 0.0
review_count = 0
categories = ''
l = []

for entry in data["businesses"]:
    display_phone = entry["display_phone"]
    id = entry["id"]
    is_claimed = str(entry["is_claimed"]).lower()
    is_closed = str(entry["is_closed"]).lower()
    address = ''.join(entry["location"]["address"])
    city = entry["location"]["city"]
    latitude = float(entry["location"]["coordinate"]["latitude"])
    longitude = float(entry["location"]["coordinate"]["longitude"])
    country_code = entry["location"]["country_code"]
    display_address = ''.join(entry["location"]["display_address"])
    geo_accuracy = float(entry["location"]["geo_accuracy"])
    postal_code = int(entry["location"]["postal_code"])
    state_code = entry["location"]["state_code"]
    name = entry["name"]
    phone = entry["phone"]
    rating = float(entry["rating"])
    review_count = int(entry["review_count"])
    l = entry["categories"]
    categories = ' '.join([item for sublist in l for item in sublist])

    insert_string = "INSERT INTO raw_restaurants (display_phone, id, is_claimed, is_closed, address, city, latitude, longitude, country_code, display_address, geo_accuracy, postal_code, state_code, name, phone, rating, review_count, categories) values (" + quote(display_phone) + quote(id) + is_claimed + ", " + is_closed + "," + quote(address) + quote(city) + str(latitude) + ", " + str(longitude) + ", " + quote(country_code) + quote(display_address) + str(geo_accuracy) + ", " + str(postal_code) + ", " + quote(state_code) + quote(name) + quote(phone) + str(rating) + ", " + str(review_count) + ", " + quote(categories) + ");"
    print insert_string.replace(",);", ");")