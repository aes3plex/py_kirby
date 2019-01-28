from API.base import *


def run():
	data = {'name': 'morpheus', 'job': 'leader'}
	return execute('post', get_url(__file__), data)

