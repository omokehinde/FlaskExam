import os



basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	DEBUG = False
	TESTING = False
	CSRF_ENABLE = True
	SECRET_KEY = 'THISkeyIsHard2know@@1'
	# SQLALCHEMY_DATABASE_URI = 'postgresql://oroka:oroka@localhost/orokadb'
	SQLALCHEMY_DATABASE_URI = 'postgres://zffnnmdysyzxls:yz7HoxKeLVukNdG4qbkPDe6Rhz@ec2-54-243-249-154.compute-1.amazonaws.com:5432/dd85dp46a8q63b'
	# DATABASE_URL: postgres://zffnnmdysyzxls:yz7HoxKeLVukNdG4qbkPDe6Rhz@ec2-54-243-249-154.compute-1.amazonaws.com:5432/dd85dp46a8q63b

class ProductionConfig(Config):
	DEBUG = False


class StagingConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class DevelopmentConfig(Config):
	DEVELOPMENT = True
	DEBUG = True

class TestingConfig(Config):
	TESTING = True
		

		