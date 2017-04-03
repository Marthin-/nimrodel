#!/usr/bin/env python3

from flask import Flask, request, render_template, Markup
import markdown
import os
import sys

def inflate_md(myTitle):
	myTitle=str(myTitle)
	url = './static/markdown/' + myTitle
	with open(url, 'r') as myFile:
		raw = myFile.read()
		content = Markup(markdown.markdown(raw))
		return render_template('articles.html', **locals())

os.environ['SCRIPT_NAME'] = os.path.dirname(os.path.realpath(__file__))
app = Flask(__name__)

@app.route("/")
def main():
	return inflate_md("index")

@app.route("/articles")
@app.route("/article")
def index_articles():
# TODO une liste dynamique des articles
	return inflate_md("index")

@app.route('/articles/<myTitle>')
def dyn_article(myTitle):
	return inflate_md(myTitle)

@app.errorhandler(404)
def ma_page_404(error):
    return "Oups, on dirait que vous vous êtes perdu !", 404

if __name__ == "__main__":
	app.run(host="0.0.0.0")

