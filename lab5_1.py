import os.path
path = '.'
num_files = len([f for f in os.listdir(path)
                if os.path.isfile(os.path.join(path, f))])
print(num_files)

DIR = '/pypy/venv/Scripts'
print(len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))]))
