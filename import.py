import myfile
print(myfile.title)

from myfile import title
print(title)

import threenames
print(threenames)
print(threenames.b, threenames.c)

from threenames import b, c
print(b, c)