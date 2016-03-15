from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys



query = "CREATE (w1:Word { value:'example word',author_name:'admin',author_id:1,time_create:timestamp() })"




gdb = GraphDatabase("http://localhost:7474/db/data/")
q = query
result = gdb.query(q=q)