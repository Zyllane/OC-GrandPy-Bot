import pytest
from GrandpyBot.classes.ApiManager import ApiManager

def test_search_place():
    """
        unit test for searching a location
    """
    research = "Où se trouve Paris?"
    mng = ApiManager()
    assert mng.search_place(research) != None

def test_geo_search():
    """
        unit test for searching the location by lat and lng
    """
    lat = "48.87641358619437"
    lng = "2.2427458153407525"
    gs = ApiManager()
    assert gs.wiki_geo_search(lat, lng) != None

def test_parse_wiki_article():
    """
        unit test to retrieve summary from given article
    """
    pageid = "ezfds"
    pwa = ApiManager()
    assert pwa.parse_wiki_article(pageid) != None