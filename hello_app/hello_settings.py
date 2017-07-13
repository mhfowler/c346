import os, json

PROJECT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__)))
print('PROJECT_PATH: {}'.format(PROJECT_PATH))

DATA_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), '../data'))
print('DATA_PATH: {}'.format(PROJECT_PATH))

# configure path to env.json (default is env.json but can use FORCE_ENVIRON to override this)
ENV_PATH = os.path.join(PROJECT_PATH, 'env.json')
print('ENV_PATH: {}'.format(ENV_PATH))

# load env.json into ENV_DICT
ENV_DICT = json.loads(open(ENV_PATH, "r").read())