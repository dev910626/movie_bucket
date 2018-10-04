from django.contrib.sessions.backends.db import SessionStore

from datetime import datetime


def update_session(ses):
	ses['last_visited'] = datetime.today().strftime("%m-%d-%Y %H:%M:%S")
	ses.save()

	return


def session_decorator(view_function):
	def wrapper(request, *args, **kwargs):
		if 'last_visited' not in request.session: #  session does not exist
			ses = SessionStore()
			update_session(ses)

			request.session['last_visited'] = ses.session_key

			request.session['message'] = 'Welcome to our Movie Bucket!'

		else:
			existing_ses = SessionStore(session_key=request.session['last_visited'])

			update_session(existing_ses)
			
			request.session['message']	= 'Welcome back! Your last visit was from ' + existing_ses['last_visited']

		return view_function(request, *args, **kwargs)

	return wrapper