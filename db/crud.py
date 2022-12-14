from db.db import Graph


class CRUD:
    def __init__(self):
        self.db = Graph("bolt://34.200.218.33:7687", "neo4j", "roof-money-hardcopies")

    # ------------------------------------------FUNCTIONS CREATE------------------------------------------------
    def createPerson(self, nome, dataDeNascimento, cartaoDoSus, cpf):
        query = "create (:Pessoa{nome: $nome, dataDeNascimento: $dataDeNascimento, cartaoDoSus: $cartaoDoSus, cpf: $cpf})"
        self.db.execute_query(query, {'nome': nome, 'dataDeNascimento': dataDeNascimento, 'cartaoDoSus': cartaoDoSus, 'cpf': cpf})

    def createPSF(self, numIdent, endereco, cidade):
        query = "create (:PSF{numIdent: $numIdent, endereco: $endereco, cidade: $cidade})"
        self.db.execute_query(query,{'numIdent': numIdent, 'endereco': endereco, 'cidade': cidade})

    def createVaccine(self, nome, eficacia, validade):
        query = "create (:Vacina{nome: $nome, eficacia: $eficacia, validade: $validade})"
        self.db.execute_query(query,{'nome': nome, 'eficacia': eficacia, 'validade': validade})

    def createManufacturer(self, nome, sede, fundacao):
        query = "create (:Fabricante{nome: $nome, sede: $sede, fundacao: $fundacao})"
        self.db.execute_query(query,{'nome': nome, 'sede': sede, 'fundacao': fundacao})

    def createRelationshipPersonVaccine(self, nomePerson, nomeVaccine, lote):
        query = "match (p:Pessoa{nome: $nomePerson}), (v:Vacina{nome: $nomeVaccine}) CREATE (p)-[:RECEBE{lote: $lote}]->(v)"
        self.db.execute_query(query,{'nomePerson': nomePerson, 'nomeVaccine': nomeVaccine, 'lote': lote})

    def createRelationshipPersonPSF(self, nomePerson, cidade, numIdentPSF):
        query = "match (p:Pessoa{nome: $nomePerson}), (s:PSF{numIdent: $numIdentPSF, cidade: $cidade}) CREATE (p)-[:PERTENCE_A]->(s)"
        self.db.execute_query(query, {'nomePerson': nomePerson, 'cidade': cidade, 'numIdentPSF': int(numIdentPSF)})

    def createRelationshipVaccineManufacturer(self, nomeVaccine, nomeManufacturer):
        query = "match (v:Vacina{nome: $nomeVaccine}), (f:Fabricante{nome: $nomeManufacturer}) CREATE (v)-[:FABRICADA_POR]->(f)"
        self.db.execute_query(query,{'nomeVaccine': nomeVaccine,'nomeManufacturer': nomeManufacturer})

    # ------------------------------------------FUNCTIONS READ------------------------------------------------

    def readPerson(self, nome):
        query = "match (p:Pessoa{nome: $nome}) return p"
        print(self.db.execute_query(query,{'nome': nome}))

    def readPSF(self, numIdent, cidade):
        query = "match (s:PSF{numIdent: $numIdent, cidade: $cidade}) return s"
        print(self.db.execute_query(query,{'numIdent': numIdent, 'cidade': cidade}))

    def readVaccine(self, nome):
        query = "match (v:Vacina{nome: $nome})return v"
        print(self.db.execute_query(query,{'nome': nome}))

    def readManufacturer(self, nome):
        query = "match (f:Fabricante{nome: $nome}) return f"
        print(self.db.execute_query(query,{'nome': nome}))

    def findManufacturerByVaccine(self, nome):
        print(self.db.execute_query("match (v:Vacina{nome: $nome})-[r:FABRICADA_POR]->(p:Fabricante) return p.nome", {
            'nome': nome}))

    def countVaccine(self, nome):
        query = self.db.execute_query('match (v:Vacina{nome: $nome}) return count(*)', {
            'nome': nome})
        a_record = query[0]
        qtdVaccine = list(a_record)
        return qtdVaccine[0]

    def findPSFByPerson(self, nome):
        query = self.db.execute_query('MATCH (p:Pessoa{nome: $nome})-[r:PERTENCE_A]->(s:PSF) return s', {
            'nome': nome})
        a_record = query[0]
        qtdVaccine = list(a_record)
        return qtdVaccine[0]
    # ------------------------------------------FUNCTIONS UPDATE------------------------------------------------

    def updatePerson(self, nome, cpf):
        return self.db.execute_query('match (p:Pessoa{nome: $nome}) set p.cpf = $cpf return p',
                                      {'nome': nome, 'cpf': cpf})

    def updatePSF(self, cidade, numIdent, endereco):
        return self.db.execute_query('match (p:PSF{cidade: $cidade, numIdent: $numIdent}) set p.endereco = $endereco return p',
                                      {'cidade': cidade, 'numIdent': numIdent, 'endereco': endereco})

    # ------------------------------------------FUNCTIONS DELETE------------------------------------------------

    def deletePerson(self, nome):
        query = "match (p:Pessoa{nome: $nome}) detach delete p"
        self.db.execute_query(query,{'nome': nome})

    def deletePSF(self, numIdent, cidade):
        query = "match (s:PSF{numIdent: $numIdent, cidade: $cidade}) detach delete s"
        self.db.execute_query(query,{'numIdent': numIdent, 'cidade': cidade})

    def deleteVaccine(self, nome):
        query = "match (v:Vacina{nome: $nome}) detach delete v"
        self.db.execute_query(query,{'nome': nome})

    def deleteManufacturer(self, nome):
         query = "match (f:Fabricante{nome: $nome}) detach delete f"
         self.db.execute_query(query,{'nome': nome})
