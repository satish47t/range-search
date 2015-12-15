from geopy.geocoders import Nominatim
from cassandra.cluster import Cluster
cluster = Cluster()
session = cluster.connect()
geolocator = Nominatim()
location = geolocator.geocode("175 5th Avenue NYC")
curr_latitude = location.latitude
curr_longitude = location.longitude
print "Your current location : (" + str(curr_latitude) + ", " + str(curr_longitude) + ")"
session.set_keyspace('ny_restaurants')
query = raw_input('Enter search query:')
rows = session.execute("SELECT * FROM raw_restaurants")
print 'Found ' + str(len(rows.current_rows)) + ' restaurant(s).'
c = 1
for res_row in rows:
    print str(c) + '.----------------------'
    print res_row.name
    print res_row.display_address
    print res_row.display_phone
    c += 1