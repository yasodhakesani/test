import re

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

print(x.group(0))

import re

txt = "The rain in Spain"

#Find all lower case characters alphabetically between "a" and "m":

import OOPs
from OOPs import multi_level_inheritence as ms

c=ms.Child()
c.common()

x = re.findall("[a-m]", txt)
print(x)

digit="hello0290"
x=re.findall("\d",digit)
print(x)

y=re.findall("he.*0",digit)
print(y)