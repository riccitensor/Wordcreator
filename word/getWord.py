from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys #manipulacja IO
import re #edycja tekstu


if (len(sys.argv)>1):
    filtr = str(sys.argv[1])
else:
    filtr = ""

if (len(sys.argv)>2):
    author_id = str(sys.argv[2]) #author_id
else:
    author_id = ""


gdb = GraphDatabase("http://localhost:7474/db/data/")
q1 = """MATCH (w:Word)-[:HAS*]-(x) WHERE id(w)="""+filtr+""" RETURN {id: id(x), value: x.value, x: x.x, y: x.y}"""
#q1 = """MATCH (w:Word { value:'"""+filtr+"""' })-[:HAS*]-(x) RETURN {id: id(x), value: x.value, x: x.x, y: x.y}"""
#q1 = """MATCH (w:Word)<-[:PART]-(x) WHERE id(w)="""+filtr+""" RETURN {id: id(x), value: x.value, x: x.x, y: x.y}"""
q2 = """MATCH (w:Word) WHERE id(w)="""+filtr+""" return {id:id(w),value:w.value};"""

result = gdb.query(q=q1)
res = gdb.query(q=q2)

def getIdFromUrl(zdanie):
    wytnij = """http://localhost:7474/db/data/node/"""
    return int(re.sub(wytnij,'',zdanie))

################################################################################
# 
#                             NODY / EDGE
#
################################################################################

class nodzik:
  def __init__(self, id, value, x, y):
    self.id = id
    self.value = value
    self.x = x
    self.y = y
  def getId(self):
    return self.id

class Xnodzik:
  def __init__(self):
    self.licznik = 0
    self.nodes = []
    
  def setN(self,nn):
    self.nodes.insert(self.licznik,nn)
    self.licznik = self.licznik + 1
  def getIndexNode(self,id):
    licznik=0
    for temp in self.nodes:      
      if (temp.id == id):
        return licznik
      licznik=licznik+1
  def printAll(self):
    licznik=0
    for temp in self.nodes:
      licznik=licznik+1
      print(' el: '+str(licznik)+' id: '+str(temp.id)+' name: '+temp.value)
  def generate(self):
    licznik=0
    print("window.nodes = [")
    for node in self.nodes:      
      if (licznik>0):
        print(",")
      node.value = re.sub('([^A-Za-z0-9\ \(\)])', '', node.value)
      print("{'title': '"+node.value+"',id:"+str(node.id)+",'x':"+str(node.x)+",'y':"+str(node.y)+"}")
      licznik=licznik+1
    print("];")

class edzik:
  def __init__(self, source, target):
    self.source = source
    self.target = target
    
class Yedzik:
  def __init__(self):
    self.licznik = 0
    self.edges = []
  def setE(self,ee):
    self.edges.insert(self.licznik,ee)
    self.licznik = self.licznik + 1
  def printAll(self):
    licznik=0
    for temp in self.edges:
      licznik=licznik+1
      print(' el: '+str(licznik)+' S: '+str(temp.source)+' T: '+str(temp.target))
  def generate(self):
    licznik=0
    print("window.edges = [")
    for edge in self.edges:
      if (licznik>0):
        print(",")
      print("{source: nodes["+str(edge.source)+"], target: nodes["+str(edge.target)+"]}")
      licznik=licznik+1
    print("];")

XXXN = Xnodzik()
YYYE = Yedzik()


for temp in res:    
    node=temp[0]
    XXXN.setN(nodzik(node['id'],node['value'],100,100))
    break

for temp in result: 
  node = temp[0]
  id = node['id']
  value = node['value']
  if node['x'] is None:
    x = 100
  else:
    x = node['x'] 
  if node['y'] is None:
    y = 100
  else:
    y = node['y'] 

  url = "http://localhost:7474/db/data/node/"+str(id)+"/relationships/in"
  R0 = requests.request('GET', url)
  R1 = R0.content.decode("utf-8")
  R2 = json.loads(R1)
  XXXN.setN(nodzik(id,value,x,y))
  if (len(R2)>0):
    for ttt in R2:       
      T0 = requests.request('GET', ttt['end'])      
      T1 = T0.content.decode("utf-8")
      T2 = json.loads(T1) 
      
      if (T2['data']['value']!=''):
        target_index = XXXN.getIndexNode(getIdFromUrl(ttt['start']))
        if target_index is not None:
            YYYE.setE(edzik(target_index,XXXN.getIndexNode(id)))        

XXXN.generate()
YYYE.generate()

#XXXN.printAll()
#YYYE.printAll()