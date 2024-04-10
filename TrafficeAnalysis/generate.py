import re
import os
passwd=[]
s= os.listdir('./files/attachment_1579250492_upload/upload')
for i in s:
    f = open('upload/'+i,'r').read()
    find=re.findall(r"\[(.*?)]",f)
    find_1=' '.join(find)
    passwd.append(find_1)
    p = open('passwd.txt', 'w')
    for lb in passwd:
        p.write(lb + '\n')