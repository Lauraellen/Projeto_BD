from db.db import Graph

class CRUD:
    def __init__(self):
        self.db = Graph("bolt://34.200.218.33:7687", "neo4j", "roof-money-hardcopies")

#------------------------------------------FUNCTIONS CREATE------------------------------------------------
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


#------------------------------------------FUNCTIONS READ------------------------------------------------

    def readPerson(self, nome):
        query = "MATCH (p:Pessoa{nome: \"" + nome + "\"}) RETURN p"
        print(self.db.execute_query(query))

    def readPSF(self, numIdent):
        query = "MATCH (s:PSF{numIdent: \"" + numIdent + "\"}) RETURN s"
        print(self.db.execute_query(query))

    def readVaccine(self, nome):
        query = "MATCH (v:Vacina{nome: \"" + nome + "\"}) RETURN v"
        print(self.db.execute_query(query))

    def readManufacturer(self, nome):
        query = "MATCH (f:Fabricante{nome: \"" + nome + "\"}) RETURN f"
        print(self.db.execute_query(query))
