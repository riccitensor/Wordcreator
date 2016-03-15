from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

def isset(variable):
	return variable in locals() or variable in globals()

if (len(sys.argv)>1):
    query = str(sys.argv[1])
else:
    query = ""

for ttt in sys.argv:
    print("Arg = "+ttt);



gdb = GraphDatabase("http://localhost:7474/db/data/")
q = query

result = gdb.query(q=q)

print("{")
licznik = 0;

for temp in result:
  licznik=licznik+1
  node = temp[0]
  if (licznik>1): 
     print(',')
  print('"'+str(licznik)+'": {')
  print('"value":"'+node['value']+'",')
  print('"id":"'+str(node['id'])+'"')
  print("}")
print("}")

