'''
Created on 21-Aug-2013

@author: Nithin K Anil (itsnka@gmail.com)
'''

import bing
import google

query='kerala'
pages=3


result=bing.SearchEngine.search(query, pages)
file=open(query+'_bing','w')
for k in result:
    file.write(str(k.name)+"\t")
    file.write(str(k.link)+"\t")
    file.write(str(k.description)+"\t")
    file.write("\n")
file.flush()
file.close()

result=google.SearchEngine.search(query, 3)
file=open(query+'_google','w')
for k in result:
    file.write(str(k.name)+"\t")
    file.write(str(k.link)+"\t")
    file.write(str(k.description)+"\t")
    file.write("\n")
file.flush()
file.close()

print "Search Complete Sucessfully.To get the results check the files in the root directory"