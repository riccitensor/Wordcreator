import re

str1 = """a b c sdf we weffwe"""


#str1 = re.sub('a', 'A', str1)




str1 = re.sub('([^A-Za-z0-9\ \(\)])', '', str1)
print(str1)