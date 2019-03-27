import flask

def front_page():
	return flask.render_template('index.html')

def home_page():
	return flask.render_template('home.html')

def capture_page():
	return flask.render_template('capture.html')


def photos_list():
	return flask.render_template('photos.html')