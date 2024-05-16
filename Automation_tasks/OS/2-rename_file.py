from pathlib import Path

root_dir = Path('Data')
folder_paths = root_dir.glob('**/*')

for path in folder_paths:
  if path.is_file():
    parent_folder = path.parts[-2] # create a tuple of paths
    new_filename = f'{parent_folder}_{path.name}'
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)