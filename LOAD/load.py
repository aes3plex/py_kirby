from add_to_path import *
set_import_path()
from API.Executors.api import post_users

from locust import TaskSet,  task, Locust, events
import requests
import json
import time


class CustomClient(object):

	def __init__(self):
		pass

	def execute(self, name):
		response = None
		start_time = time.time()
		try:
			response = post_users.run()
		except Exception as e:
			total_time = int((time.time() - start_time) * 1000)
			events.request_failure.fire(request_type="execute", name=name, response_time=total_time, exception=e)
		else:
			total_time = int((time.time() - start_time) * 1000)
			events.request_success.fire(request_type="execute", name=name, response_time=total_time, response_length=len(response.content))

		return response


class Tasks(TaskSet):	
	@task
	def index(self):
		self.client.execute('REQUEEEEST')


class User(Locust):
	def __init__(self, *args, **kwargs):
		super(Locust, self).__init__(*args, **kwargs)
		self.client = CustomClient()

	task_set = Tasks
	min_wait = 5000
	max_wait = 9000

	
    



