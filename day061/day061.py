import re

text = 'Data is the new oil'

x = re.search("Data", text)
print(f'The word (Data) is in index #{x.start()}')


