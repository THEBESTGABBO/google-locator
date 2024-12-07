from locationsharinglib import Service
import geopy.distance

def getCoordinates(username):
    cookies_file = 'cookies.txt'
    google_email = username
    service = Service(cookies_file=cookies_file, authenticating_account=google_email)
    '''
    for person in service.get_all_people():
        print(person)

    print(person.address)

    person = service.get_person_by_full_name(full_name)
    print(person)
    print(person.address)

    person = service.get_person_by_nickname("gabrielebellante09@gmail.com")
    print(person)
    '''
    latitude, longitude = service.get_coordinates_by_nickname(username)
    coordinates=(latitude, longitude)
    return coordinates

try:
    location = getCoordinates("gabrielebellante09@gmail.com")
    home = (45.6959364, 12.2596954)
    
    print(geopy.distance.geodesic(location, home).km)
    
    print(location)
    
except:
    from cookies_retriever import *
    retrieveCookiesFromGoogle("gabrielebellante09@gmail.com","@invent0r09","https://www.google.com/maps")
    