import pytest
from GrandpyBot.classes.ApiManager import ApiManager
from unittest import mock

mockplace = {
    "lat": 2,
    "lng": 3
}

apimng = ApiManager()
def test_searchplace(monkeypatch):
    """
        mock test for searching a location
    """
    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                "results": [
                    {
                        "geometry": {
                            "location": {
                                "lat": 2,
                                "lng": 3
                            }
                        }
                    }
                ],
                "status": "OK"
            }

    monkeypatch.setattr("requests.get", MockRequestsGet)
    result = apimng.search_place("où se trouve Paris?")
    assert (result["lat"] == mockplace["lat"])
    assert (result["lng"] == mockplace["lng"])


def test_geo_search(monkeypatch):
    """
        mock test for searching the location by lat and lng
    """
    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                    "batchcomplete": "",
                    "query": {
                        "geosearch": [
                            {
                                "pageid": 4859351,
                                "ns": 0,
                                "title": "Pont de Puteaux",
                                "lat": 48.876944,
                                "lon": 2.244167,
                                "dist": 119.5,
                                "primary": ""
                            }
                        ]
                    }
                }
    lat = "48.87641358619437"
    lng = "2.2427458153407525"
    gs = ApiManager()

    monkeypatch.setattr("requests.get", MockRequestsGet)
    result = gs.wiki_geo_search(lat, lng)
    assert (result["query"]["geosearch"][0]["title"] == "Pont de Puteaux")

def test_parse_wiki_article(monkeypatch):
    """
        unit test to retrieve summary from given article
    """
    class MockRequestsGet:
        def __init__(self, url, params):
            pass

        def json(self):
            return {
                "batchcomplete": "",
                "query": {
                    "pageids": [
                        "4859351"
                    ],
                    "pages": {
                        "4859351": {
                            "pageid": 4859351,
                            "ns": 0,
                            "title": "Pont de Puteaux",
                            "extract": "test"
                        }
                    }
                }
            }
    monkeypatch.setattr("requests.get", MockRequestsGet)
    pageid = "4859351"
    pwa = ApiManager()
    result = pwa.parse_wiki_article(pageid)
    assert (result["query"]["pages"][pageid]["extract"] == "test")