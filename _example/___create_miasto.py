from neo4jrestclient.client import GraphDatabase
from neo4jrestclient import client
from neo4jrestclient import query
import requests
import json
import sys

gdb = GraphDatabase("http://localhost:7474/db/data/")
q = """CREATE (spol:Spoldzielnia { value : 'Poludnie' })
CREATE (mT:Home { value : 'Trojanska' })
CREATE (mR:Home { value : 'Renesansowa' })
CREATE (mK:Home { value : 'Kasandry' })
CREATE (pS:Person { value : 'Slawek' })
CREATE (pR:Person { value : 'Remek' })
CREATE (pW:Person { value : 'Wojtek' })
CREATE (pK:Person { value : 'Krzychu' })
CREATE (pB:Person { value : 'Bolek' })
CREATE (pC:Person { value : 'Czesław' })
CREATE (pTT:Person { value : 'Tosiek' })
CREATE (pZZ:Person { value : 'Zbychu' })
CREATE (pWW:Person { value : 'Wlodek' })
CREATE (pFF:Person { value : 'Franko' })
CREATE (pMM:Person { value : 'Mietek' })
CREATE (i01:Item { value : 'telefon'})
CREATE (i02:Item { value : 'komputer'})
CREATE (i03:Item { value : 'laptop'})
CREATE (i04:Item { value : 'telefon'})
CREATE (i05:Item { value : 'komputer'})
CREATE (i06:Item { value : 'laptop'})
CREATE (mT)-[:HAS]->(spol)
CREATE (mR)-[:HAS]->(spol)
CREATE (mK)-[:HAS]->(spol)
CREATE (pS)-[:HAS]->(mT)
CREATE (pR)-[:HAS]->(mT)
CREATE (pW)-[:HAS]->(mT)
CREATE (pK)-[:HAS]->(mR)
CREATE (pB)-[:HAS]->(mR)
CREATE (pC)-[:HAS]->(mR)
CREATE (pTT)-[:HAS]->(mK)
CREATE (pZZ)-[:HAS]->(mK)
CREATE (pWW)-[:HAS]->(mK)
CREATE (pFF)-[:HAS]->(mK)
CREATE (pMM)-[:HAS]->(mK)
CREATE (i01)-[:HAS]->(pS)
CREATE (i02)-[:HAS]->(pS)
CREATE (i03)-[:HAS]->(pS)
CREATE (i04)-[:HAS]->(pR)
CREATE (i05)-[:HAS]->(pR)
CREATE (i06)-[:HAS]->(pR)"""

gdb.query(q=q)
