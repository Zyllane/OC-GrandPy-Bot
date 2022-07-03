import os

import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

class ApiManager:
    """
    Class that query the different API (Googlemaps and Media Wiki)
    """

    def search_place(self, place):
        """
        Query the Googlemaps API with the given place in parameter to return latitude and longitude
        :param place: the name of a place we want geocoord
        :return: return  latitude and longitude if API call is "OK", return None if not
        """
        response = None
        params = {
            "key": API_KEY,
            "address": place
        }
        api_response = requests.get(url="https://maps.googleapis.com/maps/api/geocode/json", params=params).json()

        if api_response["status"] == "OK":
            lat = api_response["results"][0]["geometry"]["location"]["lat"]
            lng = api_response["results"][0]["geometry"]["location"]["lng"]
            response = {
                "lat": lat,
                "lng": lng,
                "url": f"https://www.google.com/maps/embed/v1/place?key={API_KEY}&q={lat},{lng}"
            }
        return response

    def wiki_geo_search(self, lat, lng):
        """
        Query the Media Wiki API with given latitude and longitude
        :param lat: latitude of a given place
        :param lng: longitude of a given place
        :return: *
        """
        response = None
        params = {
            "action": "query",
            "format": "json",
            "list": "geosearch",
            "gscoord": lat + "|" + lng
        }
        response = requests.get(url="https://fr.wikipedia.org/w/api.php", params=params).json()
        return response

    def parse_wiki_article(self, pageid):
        """
        Query the summary from the given pageid on wikipedia

        :param pageid:
        :return:
        """
        response = None
        params = {
            "action": "query",
            "format": "json",
            "prop": "extracts",
            "pageids": pageid,
            "exsentences": "5",
            "exintro": "1",
            "explaintext": "1",
            "indexpageids": 1
        }
        response = requests.get(url="https://fr.wikipedia.org/w/api.php", params=params).json()
        return response