from flask import session, request, redirect, url_for

endpoints_not_requiring_login = [
	"",
	"index",
	"login_form",
]

def logged_in_before_request():
	if request.endpoint in endpoints_not_requiring_login:
		return

	if 'email' not in session:
		return redirect(url_for('index'))