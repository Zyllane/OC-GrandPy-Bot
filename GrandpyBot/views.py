from flask import Flask,render_template,request
from .classes.Parser import Parser
from .classes.ApiManager import ApiManager
from random import randint
import time

from flask_cors import CORS

app = Flask(__name__)

app.config.from_object('config')

grandpa_sentences = ['Ca me rappelle quelque chose... Oui ça me revient! ',
                     'J\'ai une anecdote rigolotte sur cet endroit! ',
                     'Savais-tu que ',
                     'Ma foi Damien, je parie que tu ne la connaissais pas celle-là! ',
                     'J\ai trouvé cet article sur Wikipédia. Tu connais ce site? ']


@app.route('/')
def index():
    """
        default route of the application
    """
    return render_template("home.html")


@app.route('/process', methods=["POST"])
def process():
    """
        called by the front in main.js
        process the userentry and send to the front the different results of the user search (map url, bot message...)
    """
    result = {
        "url": "",
        "summary": ""
    }
    if request.method == "POST":
        query = request.form["query"]
        parser = Parser()
        parseResult = parser.parse(query)
        apiMng = ApiManager()
        place = apiMng.search_place(parseResult)
        if place != None:
            wikiSearch = apiMng.wiki_geo_search(str(place["lat"]), str(place["lng"]))
            randomSentence = randint(0, len(grandpa_sentences)-1)
            randomArticle = randint(0,len(wikiSearch["query"]["geosearch"])-1)
            articleId = wikiSearch["query"]["geosearch"][randomArticle]["pageid"]
            summary = str(apiMng.parse_wiki_article(articleId)["query"]["pages"][str(articleId)]["extract"])
            result["url"] = place["url"]
            result["summary"] = grandpa_sentences[randomSentence] + summary
    time.sleep(2)
    return result

if __name__ == "__main__":
    app.run()