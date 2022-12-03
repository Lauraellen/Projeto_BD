from db.db import Graph

class CRUD:
    def __init__(self):
        self.db = Graph("bolt://34.200.218.33:7687", "neo4j", "roof-money-hardcopies")

    def createPerson(self, nome, dataDeNascimento, cartaoDoSus, cpf):
        query = "CREATE (:Pessoa{nome: \"" + nome + "\", dataDeNascimento: \"" + dataDeNascimento + \
                "\", cartaoDoSus: " + cartaoDoSus + ", cpf: " + cpf + "})"
        self.db.execute_query(query)

    def createPSF(self, numIdent, endereco, cidade):
        query = "CREATE (:PSF{numIdent: " + numIdent + ", endereco: \"" + endereco + \
                "\", cidade: \"" + cidade + "\"})"
        self.db.execute_query(query)

    def createVaccine(self, nome, eficacia, validade):
        query = "CREATE (:Vacina{nome: \"" + nome + "\", eficacia: \"" + eficacia + \
                "\", validade: \"" + validade + "\"})"
        self.db.execute_query(query)

    def createManufacturer(self, nome, sede, fundacao):
        query = "CREATE (:Fabricante{nome: \"" + nome + "\", sede: \"" + sede + \
                "\", fundacao: " + fundacao + "})"
        self.db.execute_query(query)
