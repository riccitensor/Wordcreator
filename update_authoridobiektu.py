from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """ MATCH (w:Word {value:'Root'})<-[:IS]-(n:Word{value:'Object'}) SET n.author_id = 0; """

result = gdb.query(q=q)

