from db.db import Graph


class CRUD:
    def __init__(self):
        #Graph("bolt://34.200.218.33:7687", "neo4j", "roof-money-hardcopies")
        self.db = Graph("bolt://34.200.218.33:7687", "neo4j", "roof-money-hardcopies")

    # ------------------------------------------FUNCTIONS CREATE------------------------------------------------
    def createPerson(self, nome, dataDeNascimento, cartaoDoSus, cpf):
        query = "CREATE (:Pessoa{nome: $nome, dataDeNascimento: $dataDeNascimento, cartaoDoSus: $cartaoDoSus, +cpf: $cpf})"
        self.db.execute_query(query, {'nome': nome, 'dataDeNascimento': dataDeNascimento, 'cartaoDoSus': cartaoDoSus, 'cpf': cpf})

    def createPSF(self, numIdent, endereco, cidade):
        query = "CREATE (:PSF{numIdent: $numIdent, endereco: $endereco, cidade: $cidade})"
        self.db.execute_query(query,{'numIdent': numIdent, 'endereco': endereco, 'cidade': cidade})

    def createVaccine(self, nome, eficacia, validade):
        query = "CREATE (:Vacina{nome: $nome, eficacia: $eficacia, validade: $validade})"
        self.db.execute_query(query,{'nome': nome, 'eficacia': eficacia, 'validade': validade})

    def createManufacturer(self, nome, sede, fundacao):
        query = "CREATE (:Fabricante{nome: $nome, sede: $sede, fundacao: $fundacao})"
        self.db.execute_query(query,{'nome': nome, 'sede': sede, 'fundacao': fundacao})

    def createRelationshipPersonVaccine(self, nomePerson, nomeVaccine, lote):
        query = "MATCH (p:Pessoa{nome: $nomePerson}), (v:Vacina{nome: $nomeVaccine}) CREATE (p)-[:RECEBE{lote: $lote}]->(v)"
        self.db.execute_query(query,{'nomePerson': nomePerson, 'nomeVaccine': nomeVaccine, 'lote': lote})

    def createRelationshipPersonPSF(self, nomePerson, numIdentPSF):
        query = "MATCH (p:Pessoa{nome: $nomePerson}), (s:PSF{numIdent: $numIdentPSF}) CREATE (p)-[:PERTENCE_A]->(S)"
        self.db.execute_query(query, {'nomePerson': nomePerson, 'numIdentPSF': numIdentPSF})

    def createRelationshipVaccineManufacturer(self, nomeVaccine, nomeManufacturer):
        query = "MATCH (v:Vacina{nome: $nomeVaccine}), (f:PSF{nome: $nomeManufacturer}) CREATE (v)-[:FABRICADA_POR]->(f)"
        self.db.execute_query(query,{'nomeVaccine': nomeVaccine,'nomeManufacturer': nomeManufacturer})

    # ------------------------------------------FUNCTIONS READ------------------------------------------------

    def readPerson(self, nome):
        query = "MATCH (p:Pessoa{nome: $nome}) RETURN p"
        print(self.db.execute_query(query,{'nome': nome}))

    def readPSF(self, numIdent):
        query = "MATCH (s:PSF{numIdent: $numIdent}) RETURN s"
        print(self.db.execute_query(query,{'numIdent': numIdent}))

    def readVaccine(self, nome):
        query = "MATCH (v:Vacina{nome: $nome}) RETURN v"
        print(self.db.execute_query(query,{'nome': nome}))

    def readManufacturer(self, nome):
        query = "MATCH (f:Fabricante{nome: $nome}) RETURN f"
        print(self.db.execute_query(query,{'nome': nome}))

    # ------------------------------------------FUNCTIONS UPDATE------------------------------------------------

    def updatePerson(self, nome, cpf):
        return self.db.execute_query('match (p:Pessoa{nome: $nome}) set p.cpf = $cpf return p',
                                      {'nome': nome, 'cpf': cpf})

    def updatePSF(self, cidade, numIdent, endereco):
        return self.db.execute_query('match (p:PSF{cidade: $cidade, numIdent: $numIdent}) set p.endereco = $endereco return p',
                                      {'cidade': cidade, 'numIdent': numIdent, 'endereco': endereco})

    # ------------------------------------------FUNCTIONS DELETE------------------------------------------------

    def deletePerson(self, nome):
        query = "MATCH (p:Pessoa{nome: $nome}) DETACH DELETE p"
        self.db.execute_query(query,{'nome': nome})

    def deletePSF(self, numIdent):
        query = "MATCH (s:PSF{numIdent: $numIdent}) DETACH DELETE s"
        self.db.execute_query(query,{'numIdent': numIdent})

    def deleteVaccine(self, nome):
        query = "MATCH (v:Vacina{nome: $nome}) DETACH DELETE v"
        self.db.execute_query(query,{'nome': nome})

    def deleteManufacturer(self, nome):
         query = "MATCH (f:Fabricante{nome: $nome}) DETACH DELETE f"
         self.db.execute_query(query,{'nome': nome})
