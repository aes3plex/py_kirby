import sys
import os

def set_import_path():
	home = '\\'.join(os.path.abspath(__file__).rsplit('\\')[:-2])
	if home not in sys.path:
		sys.path.append(home)
