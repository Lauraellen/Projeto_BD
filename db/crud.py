from db.db import Graph

class CRUD:
    def __init__(self):
        self.db = Graph("bolt://34.200.218.33:7687", "neo4j", "roof-money-hardcopies")