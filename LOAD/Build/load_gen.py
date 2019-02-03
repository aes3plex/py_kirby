import glob 
import os
import json


models_dir = "../../API/Models/"
model_list = dict()
os.chdir(models_dir)
counter = 0
for file in glob.glob("*.json"):
    counter += 1
    model_list.update({str(counter) : file})

print('\n' + 'Choose model number for load or press \'q\' to skip: ')
model_num = input()
print('\n')

if model_num in model_list.keys():
	model = open(models_dir + model_list[model_num], 'r')
	api_methods = json.loads(model.read())['methods']
	model.close()
	
	os.chdir('../../LOAD/')
	load = open('load.py', 'w')
	methods = dict()

	load.write(
		'from add_to_path import *' + '\n' 
		+ 'set_import_path()' + '\n' + '\n'
		+ 'from locust import TaskSet,  task, Locust, events' + '\n'
		+ 'import time' + '\n' + '\n')

	for i in range(len(api_methods)):
		method = api_methods[i]
		if(method['load'] != None):
			path = method['url']
			path_arr = list(filter(lambda x: True if len(x) != 0 else False, path.rsplit('/')))
			executor_name = method['type'] + '_' + path_arr[-1]
			methods.update({executor_name:str(method['load'])})
			import_path = ''
			for i in range(len(path_arr) - 1):
				import_path += '.' + path_arr[i]

			load.write(
			'from API.Executors' + import_path + ' import ' + executor_name + '\n')

	load.write('\n' + 'class CustomClient(object):' + '\n' + '\n'
		+ '\t' + 'def __init__(self):' + '\n' 
		+ '\t' + '\t' + 'pass' + '\n' + '\n'
		+ '\t' + 'def execute(self, name, request):' + '\n'
		+ '\t' + '\t' + 'start_time = time.time()' + '\n'
		+ '\t' + '\t' + 'response = None' + '\n'
		+ '\t' + '\t' + 'try:' + '\n'
		+ '\t' + '\t' + '\t' + 'response = request()' + '\n'
		+ '\t' + '\t' + 'except Exception as e:' + '\n'
		+ '\t' + '\t' + '\t' + 'total_time = int((time.time() - start_time) * 1000)' + '\n'
		+ '\t' + '\t' + '\t' + 'events.request_failure.fire(request_type="HTTP", name=name, response_time=total_time, exception=e)' + '\n'
		+ '\t' + '\t' + 'else:' + '\n'
		+ '\t' + '\t' + '\t' + 'total_time = int((time.time() - start_time) * 1000)' + '\n'
		+ '\t' + '\t' + '\t' + 'events.request_success.fire(request_type="HTTP", name=name, response_time=total_time, response_length=len(response.content))' + '\n'
		+ '\n' + '\t' + '\t' + 'return response' + '\n'+ '\n'
		+ 'class Tasks(TaskSet):' + '\n')

	for key in methods:
		load.write('\t' + '@task(' + methods[key] + ')' + '\n'
			+ '\t' + 'def ' + key + '(self):' + '\n'
			+ '\t' + '\t' + 'self.client.execute(\'' + key.upper() + '\', ' + key + '.run)' + '\n' + '\n' + '\n')

	load.write('class User(Locust):' + '\n'
		+ '\t' + 'def __init__(self, *args, **kwargs):' + '\n'
		+ '\t' + '\t' + 'super(Locust, self).__init__(*args, **kwargs)' + '\n'
		+ '\t' + '\t' + 'self.client = CustomClient()' + '\n' + '\n'
		+ '\t' + 'task_set = Tasks' + '\n'
		+ '\t' + 'min_wait = 5000' + '\n'
		+ '\t' + 'max_wait = 9000' + '\n')

	load.close()
	print('Load script has been created')

elif model_num == 'q':
	pass
else:
	print('\n' + 'Model not in list')