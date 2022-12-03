from db.db import Graph


class CRUD:
    def __init__(self):
        self.db = Graph("bolt://44.192.100.12:7687", "neo4j", "specialist-surge-troop")

    # ------------------------------------------FUNCTIONS CREATE------------------------------------------------
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

    def createRelationshipPersonVaccine(self, nomePerson, nomeVaccine, lote):
        query = "MATCH (p:Pessoa{nome: \"" + nomePerson + "\"}), (v:Vacina{nome: \"" + nomeVaccine + \
                "\"}) CREATE (p)-[:RECEBE{lote:" + lote + "}]->(v)"
        self.db.execute_query(query)

    def createRelationshipPersonPSF(self, nomePerson, numIdentPSF):
        query = "MATCH (p:Pessoa{nome: \"" + nomePerson + "\"}), (s:PSF{numIdent: " + numIdentPSF + \
                "}) CREATE (p)-[:PERTENCE_A]->(S)"
        self.db.execute_query(query)

    def createRelationshipVaccineManufacturer(self, nomeVaccine, nomeManufacturer):
        query = "MATCH (v:Vacina{nome: \"" + nomeVaccine + "\"}), (f:PSF{nome: \"" + nomeManufacturer + \
                "\"}) CREATE (v)-[:FABRICADA_POR]->(f)"
        self.db.execute_query(query)

    # ------------------------------------------FUNCTIONS READ------------------------------------------------

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

    # ------------------------------------------FUNCTIONS UPDATE------------------------------------------------

    def updatePerson(self, nome, cpf):
        return self.db.execute_query('match (p:Pessoa{nome: $nome}) set p.cpf = $cpf return p',
                                      {'nome': nome, 'cpf': cpf})

    def updatePSF(self, cidade, numIdent, endereco):
        return self.db.execute_query('match (p:PSF{cidade: $cidade, numIdent: $numIdent}) set p.endereco = $endereco return p',
                                      {'cidade': cidade, 'numIdent': numIdent, 'endereco': endereco})
    # ------------------------------------------FUNCTIONS DELETE------------------------------------------------

    def deletePerson(self, nome):
        query = "MATCH (p:Pessoa{nome: \"" + nome + "\"}) DETACH DELETE p"
        self.db.execute_query(query)

    def deletePSF(self, numIdent):
        query = "MATCH (s:PSF{numIdent: \"" + numIdent + "\"}) DETACH DELETE s"
        self.db.execute_query(query)

    def deleteVaccine(self, nome):
        query = "MATCH (v:Vacina{nome: \"" + nome + "\"}) DETACH DELETE v"
        self.db.execute_query(query)

    def deleteManufacturer(self, nome):
        query = "MATCH (f:Fabricante{nome: \"" + nome + "\"}) DETACH DELETE f"
        self.db.execute_query(query)
