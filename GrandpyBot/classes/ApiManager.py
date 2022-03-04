import requests

API_KEY = ""

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
            response = {
                "lat": api_response["results"][0]["geometry"]["location"]["lat"],
                "lng": api_response["results"][0]["geometry"]["location"]["lng"]
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
        api_response = requests.get(url="https://fr.wikipedia.org/w/api.php", params=params).json()
        return api_response