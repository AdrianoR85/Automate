from pathlib import Path
from datetime import datetime

root_dir = Path('Data')

for path in root_dir.glob('**/*'):
  if path.is_file():
    stats = path.stat()
    paths = path.parts
    second_created = stats.st_ctime
    date_created = datetime.fromtimestamp(second_created)
    date_created_str = date_created.strftime('%Y-%m-%d_%H_%M_%S')
    new_filename = f'{date_created_str}_{path.name}'
    new_path = path.with_name(new_filename)
    path.rename(new_path)
    