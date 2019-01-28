from model_parse import *

print('Enter the model\'s name: ')
model_name = input()
if model_name:
	model = open(model_name + '.json', 'r')
	config = open('config.py', 'w')
	mdata = json.loads(model.read())
	api_methods = mdata['methods']

	config.write(
		'base_url = \'' + mdata['base_url'] + '\'\n'
		'content_type_header_json = {\'content-type\' : \'application/json\'}' + '\n')
	config.close()

	for i in range(len(api_methods)):
		method = api_methods[i]
		create_exec_tree(method['url'], method['type'], method['data'])
		create_testcase(method['url'], method['type'], method['description'])

	print('\n' + 'Skeleton has been formed !')
	model.close()

else:
	print('Empty model\'s name')