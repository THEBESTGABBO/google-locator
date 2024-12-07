from locationsharinglib import Service

def getCoordinates(username):
    cookies_file = 'cookies.txt'
    google_email = username
    service = Service(cookies_file=cookies_file, authenticating_account=google_email)
    
    latitude, longitude = service.get_coordinates_by_nickname(username)
    coordinates=(latitude, longitude)
    return coordinates

try:
    location = getCoordinates("youremail@gmail.com") 
    print(location)
    
except:
    from cookies_retriever import *
    retrieveCookiesFromGoogle("youremail@gmail.com","yourpassword","https://www.google.com/maps")
    
