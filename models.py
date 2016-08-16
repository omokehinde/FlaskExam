from app import db
from sqlalchemy.dialects.postgresql import JSON

class Result(db.Model):
	__tablename__ = 'results'

	id = db.Column(db.Integer, primary_key=True)
	url = db.Column(db.String())
	result_all = db.Column(JSON)
	result_on_stop_words = db.Column(JSON)

	def __init__(self, url, result_all, result_on_stop_word):
		self.url = url
		self.result_all = result_all
		self.result_on_stop_words = result_on_stop_words

	def __repr__(self):
		return '<id {}>'.format(self.id)
