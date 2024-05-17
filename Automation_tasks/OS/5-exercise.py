import os

# Root directory of OS
base_path = os.path.expanduser('~')

# Browse the download directory
path = os.path.join(base_path,'Downloads')
work_dir = os.chdir(path)

# List all files in the download directory
list_files = os.listdir(work_dir)

# Organization the path
types_files = ['exe', 'csv', 'txt', 'zip', 'pdf', 'jpg', 'png', 'jpeg', 'py', 'xlsx']
for type in types_files:
  if type not in os.listdir():
    os.mkdir(type)

# Organization the files
for file in list_files:
  for type in types_files:
    if '.' +type in file:
      old_path = os.path.join(path, file)
      new_path = os.path.join(path, type, file)
      os.replace(old_path, new_path)
    