from pathlib import Path

root_dir = Path('data')
file_paths = root_dir.iterdir()

for index, path in enumerate(file_paths):
  new_file_name = f'{index+1}-{path.stem[:-1]}{path.suffix}'
  new_filePath = path.with_name(new_file_name)
  path.rename(new_file_name)