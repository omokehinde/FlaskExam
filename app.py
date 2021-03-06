import os
import requests
import operator
import re
import nltk
from flask import Flask, render_template, request
from flask.ext.sqlalchemy import SQLAlchemy
from stop_words import stops
from collections import Counter
from bs4 import BeautifulSoup




app = Flask(__name__)
app.config.from_object('config.StagingConfig')

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://oroka:oroka@localhost/orokadb'  <= development db
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://zffnnmdysyzxls:yz7HoxKeLVukNdG4qbkPDe6Rhz@ec2-54-243-249-154.compute-1.amazonaws.com:5432/dd85dp46a8q63b'
# DATABASE_URL: postgres://zffnnmdysyzxls:yz7HoxKeLVukNdG4qbkPDe6Rhz@ec2-54-243-249-154.compute-1.amazonaws.com:5432/dd85dp46a8q63b
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from models import Result


@app.route('/', methods=['GET', 'POST'])
def index():
	errors = []
	results = {}
	if request.method == "POST":
		# get url the user entered
		try:
			url = request.form['url']
			r = requests.get(url)
			# print(r.text)
		except:
			errors.append(
				"Unable to get URL. Please enter a valid URL and try again."
				)
			return render_template('index.html', errors=errors)
		if r:
			# text processing
			raw = BeautifulSoup(r.text, 'html.parser').get_text()
			nltk.data.path.append('./nltk_data/tokenizers/punkt') # set the path
			tokens = nltk.word_tokenize(raw)
			text = nltk.Text(tokens)
			# remove punctuation, count raw words
			nonPunct = re.compile('.*[A-Za-z].*')
			raw_words = [w for w in text if nonPunct.match(w)]
			raw_word_count = Counter(raw_words)
			# stop words
			no_stop_words = [w for w in raw_words if w.lower() not in stops]
			no_stop_words_count = Counter(no_stop_words)
			# save the results
			results = sorted(
				no_stop_words_count.items(),
				key=operator.itemgetter(1),
				reverse=True
				)
			try:
				result = Result(
					url=url,
					result_all=raw_word_count,
					result_on_stop_words=no_stop_words_count
					)
				db.session.add(result)
				db.session.commit()
			except:
				errors.append("Unable to add to database.")
	return render_template('index.html', errors=errors, results=results)

@app.route('/<name>')
def hello_name(name):
	return "Hello {}!".format(name)


if __name__ == '__main__':
	app.run()