from pathlib import Path

root_dir = Path('files')
file_paths = root_dir.glob('**/*')
for path in file_paths:
  if path.is_file():
    # print(path)
    # print(path.parts[-2])
    parent_folder = path.parts[-2]
    new_file_name = f'{parent_folder}-{path.name}'
    print(new_file_name)

