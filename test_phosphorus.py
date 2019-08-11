import pytest
import webtest
import phosphorus


app = phosphorus.App()

@app.add_endpoint(r'/([a-z])([0-9])')
def letter_number(match):
	return phosphorus.Response(f'{match.group(1)},{match.group(2)}')

app = webtest.TestApp(app)


def test_regex_groups():
	r = app.get('/d4')
	assert r.status == '200 OK'
	assert r.content_type == 'text/html'
	assert r.text == 'd,4'
