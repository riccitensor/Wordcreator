from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

csvpath = "d:/serwer/www/temp/csv/"
gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """MATCH (n) RETURN {id: id(n), value: n.value}"""
result = gdb.query(q=q)

textfile = open(csvpath+'test.csv','w')
textfile.write("source,target,value\n")


for temp in result:
  node = temp[0]
  print(node['value'])
  print(node['id'])
  id = node['id']
  value = node['value']
  url = "http://localhost:7474/db/data/node/"+str(id)+"/relationships/out"
  R0 = requests.request('GET', url)
  R1 = R0.content.decode("utf-8")
  R2 = json.loads(R1)  
  if (len(R2)>0):
    for ttt in R2:
      print("-> "+ttt['end'])
      T0 = requests.request('GET', ttt['end'])      
      T1 = T0.content.decode("utf-8")
      #print(T1)
      T2 = json.loads(T1) 
      print("   " + T2['data']['value'])
      if (T2['data']['value']!=''):
        textfile.write(node['value']+","+T2['data']['value']+","+"0.7\n")
  print("")
textfile.close()