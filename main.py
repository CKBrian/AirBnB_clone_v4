#!/usr/bin/python3
"""
 Test cities access from a state
"""
from models import storage
from models.state import State
from models.place import Place
from models.city import City
from models.user import User
from models.amenity import Amenity

"""
 Objects creations
"""
clients = ['Robert', 'Faith', 'Boniface', 'Wambua', 'Julien', 'Sylvian']
us_states_and_cities = {
    "California": ["Los Angeles", "San Francisco", "San Diego", "Sacramento", "San Jose"],
    "Texas": ["Houston", "Dallas", "Austin", "San Antonio", "Fort Worth"],
    "Florida": ["Miami", "Orlando", "Tampa", "Jacksonville", "Fort Lauderdale"],
    "New York": ["New York City", "Buffalo", "Rochester", "Albany", "Syracuse"],
    "Illinois": ["Chicago", "Springfield", "Peoria", "Rockford", "Naperville"],
    "Georgia": ["Atlanta", "Savannah", "Augusta", "Columbus", "Macon"],
    "Colorado": ["Denver", "Colorado Springs", "Aurora", "Fort Collins", "Boulder"],
    "Arizona": ["Phoenix", "Tucson", "Mesa", "Chandler", "Scottsdale"],
    "Ohio": ["Columbus", "Cleveland", "Cincinnati", "Toledo", "Akron"],
    "Washington": ["Seattle", "Tacoma", "Spokane", "Vancouver", "Bellevue"]
}

# Create Users:
print("-- Create a new User --")
m_user = User(email="a.gmail", password="passwd")
print(m_user.to_dict())
m_user.save()
print("\n-- Create a new User --")
my_user = User()
my_user.first_name = "Betty"
my_user.last_name = "Bar"
my_user.email = "airbnb@mail.com"
my_user.password = "root"
print(my_user.to_dict())
my_user.save()
my_user.save()
print(my_user)

print("-- Create a new User 2 --")
my_user2 = User()
my_user2.first_name = "John"
my_user2.email = "airbnb2@mail.com"
my_user2.password = "root"
my_user2.save()
print(my_user2)

# create states
for state, cities in us_states_and_cities.items():
    state_1 = State(name=state)
    print("New state: {}".format(state))
    state_1.save()
    for city in cities:
        city_1 = City(name=city, state_id=state_1.id)
        print("New city: {}".format(city))
        city_1.save()

# creates amenities
amenity_1 = Amenity(id="2a", name="Spa")
#amenity_1.save()
amenity_2 = Amenity(id="1b", name="Parking")
amenity_2.save()
amenity_3 = Amenity(id="1c", name="Swimming pool")
amenity_3.save()
amenity_4 = Amenity(id="1d", name="Toiletries")
amenity_4.save()

# creates places
place_1 = Place(id="A", name="Atlantis", user_id="6540", city_id="12")
place_1.save()
place_2 = Place(id="z", name="Asgard", user_id="6540", city_id="12")
#place_2.save()

# creates places_amenities
place_amenity_1 = place_2.amenities.append(amenity_1)
print(place_2)
print(amenity_1)
print(place_2.amenities[0].id)
place_amenity_2 = place_1.amenities.append(amenity_2)
place_amenity_3 = place_1.amenities.append(amenity_3)
place_amenity_4 = place_1.amenities.append(amenity_4)


place_amenity_5 = place_2.amenities.append(amenity_1)
place_amenity_6 = place_2.amenities.append(amenity_2)
place_amenity_7 = place_2.amenities.append(amenity_3)
place_amenity_8 = place_2.amenities.append(amenity_4)
storage.save()
