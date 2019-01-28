from model_parse import *
import glob 

models_dir = "Models/"
model_list = dict()
os.chdir('../' + models_dir)
counter = 0
for file in glob.glob("*.json"):
    counter += 1
    model_list.update({str(counter) : file})
os.chdir('..')

print('You have such model_list as:' + '\n')
for key in model_list:
	print(key + '. ' + model_list[key])

print('\n' + 'Choose model\'s number: ')
model_num = input()
print('\n')
if model_num in model_list.keys():
	model = open(models_dir + model_list[model_num], 'r')
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
	print('\n' + 'Model not in list')