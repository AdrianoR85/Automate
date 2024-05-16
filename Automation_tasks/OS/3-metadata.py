from pathlib import Path
from datetime import datetime

path = Path('../Data', 'Files1', 'Files1_a.txt')

stats = path.stat()
second_created = stats.st_ctime
date_created_str = datetime.fromtimestamp(second_created).strftime('%Y-%m-%d_%H:%M:%S')

