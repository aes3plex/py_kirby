import json
import os


def create_exec_tree(path, method_type, data):
	path_arr = list(filter(lambda x: True if len(x) != 0 else False, path.rsplit('/')))
	current_path = 'Executors/'
	if not os.path.exists(current_path):
		os.makedirs(current_path)
		open(current_path + '__init__.py', 'w').close()
	for i in range(len(path_arr)):
		if path_arr[i] == path_arr[-1]:
			executor = open(current_path + method_type + '_' + path_arr[i] + '.py', 'w')
			create_exec(executor, method_type, data)
			print('Executor ' + '\'' + method_type + '_' + path_arr[i] + '\'' + ' was created')
			break
		current_path += path_arr[i] + '/'
		if not os.path.exists(current_path):
			os.makedirs(current_path)
			open(current_path + '__init__.py', 'w').close()


def create_exec(file, method_type, data):
	if 'get' in method_type:
		file.write(
			'from API.base import *' + '\n' + '\n' + '\n'
			+ 'def run():' + '\n'
			+ '\t' + 'return execute(' + '\'' + method_type + '\'' + ', get_url(__file__))' + '\n'
			)

	elif 'post' in method_type:
		file.write(
			'from API.base import *' + '\n' + '\n' + '\n'
			+ 'def run():' + '\n'
			+ '\t' + 'data = ' + str(data) + '\n'
			+ '\t' + 'return execute(' + '\'' + method_type + '\'' + ', get_url(__file__), data)' + '\n'
			)
	else: print('incorrect method\'s type')
	file.close()


def create_testcase(path, method_type, description):
	tc_dir = 'Testcases/'	
	if not os.path.exists(tc_dir):
		os.makedirs(tc_dir)
		open(tc_dir + '__init__.py', 'w').close()
	path_arr = list(filter(lambda x: True if len(x) != 0 else False, path.rsplit('/')))
	executor_name = method_type + '_' + path_arr[-1]
	import_path = ''
	for i in range(len(path_arr) - 1):
		import_path += '.' + path_arr[i]

	case = open(tc_dir + 'test_' + executor_name + '.py', 'w')
	case.write(
		'import pytest' + '\n'
		+ 'from allure import title, description, story, severity' + '\n'
		+ 'from API.base import *' + '\n'
		+ 'from API.Executors' + import_path + ' import ' + executor_name + '\n' + '\n' + '\n'
		+ '@title("' + executor_name + '")' + '\n'
		+ '@description("' + description + '")' + '\n'
		+ '@severity(\'Critical\')' + '\n'
		+ 'def test_run():' + '\n'
		+ '\t' + 'with step("Base checks"):' + '\n'
		+ '\t' + '\t' + 't = ' + executor_name + '.run()' + '\n'
		+ '\t' + '\t' + 'base_assert(t, ' + '\'' + method_type +  '\'' + ')' + '\n'
		+ '\t' + '\t' + 'with step("Request data"):' + '\n'
		+ '\t' + '\t' + '\t' + 'base_attachments(t)' + '\n'
		)
	case.close()
	print('Testcase ' + '\'' + 'test_' + executor_name + '\'' + ' was created')

