from pathlib import Path

p1 = Path('files/data', 'text.txt')
print(p1.name)
print(p1.stem) # Return the name before dot
print(p1.suffix) # return the name after dot include the dot
print(p1.exists())
print('\n')
if p1.exists():
  with open(p1, 'r', encoding='utf-8') as f:
    print(f.read())
    
p2 = Path('files')
file_paths = p2.glob('**/*')

for path in p2.iterdir():
  if 'files\data' == str(path):
    letters = ['a', 'b', 'c']    
    for letter in letters:
      print(letter)
      with open(f'{path}/{letter}.txt', 'w', encoding='utf-8') as f:
        f.write('')
