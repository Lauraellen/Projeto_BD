from db.crud import CRUD

crud = CRUD()

menu = True
while(menu):

    print("Seja bem vindo ao sistema de controle de vacinas!")
    print("O que deseja fazer?")

    value1 = int(input(
        "1 - Acessar a área de pacientes \n"
        "2 - Acessa a área de vacinas \n"
        "3 - Acessa a área de fabricantes de vacinas \n"
        "4 - Acessar a área de PSF \n"
    ))

    if(value1 == 1):

        print("O que deseja fazer agora?")
        value2 = int(input(
            "1 - Adicionar um novo paciente ao sistema \n"
            "2 - Verificar dados de um paciente cadastrado no sistema \n"
            "3 - Atualizar CPF de um paciente \n"
            "4 - Adicionar uma vacina a ficha do paciente \n"
            "5 - Vincular paciente a um PSF \n"
            "6 - Verificar a qual PSF o paciente pertence \n"
            "7 - Remover um paciente do sistema \n"
            "8 - Voltar ao menu principal \n"
        ))

        if(value2 == 1):
            nome = input("Informe o nome do paciente: ")
            dataDeNascimento = input("Agora informe a data de nascimento: ")
            cartaoDoSus = input("Informe seu cartão do SUS: ")
            cpf = input("Por último, digite o cpf do paciente: ")
            crud.createPerson(nome,dataDeNascimento,cartaoDoSus,cpf)
            print("Paciente adicionado no sistema!")
            print('')
        elif(value2 == 2):
            nome = input("Informe o nome do paciente: ")
            crud.readPerson(nome)
            print('')
        elif(value2 == 3):
            nome = input("Informe o nome do paciente: ")
            cpf = input("Agora informe o CPF a ser atualizado no sistema: ")
            crud.updatePerson(nome,cpf)
            print("CPF do paciente atualizado no sistema!")
            print("")
        elif(value2 == 4):
            nomePaciente = input("Informe o nome do paciente: ")
            nomeVacina = input("Informe o nome da vacina que o paciente recebeu: ")
            lote = input("Digite o número lote da vacina recebida pelo paciente: ")
            crud.createRelationshipPersonVaccine(nomePaciente,nomeVacina,lote)
            print("Vacina adicionada na ficha do paciente!")
            print("")
        elif(value2 == 5):
            nome = input("Informe o nome do paciente: ")
            cidade = input("Informe a cidade do paciente: ")
            numIdent = input("Digite o número de identificação do PSF: ")
            crud.createRelationshipPersonPSF(nome,cidade,numIdent)
            print("Paciente vinculado ao PSF informado!")
            print("")
        elif (value2 == 6):
            nome = input("Informe o nome do paciente: ")
            result = crud.findPSFByPerson(nome)
            print(result)
        elif(value2 == 7):
            nome = input("Informe o nome do paciente que deseja remover do sistema: ")
            crud.deletePerson(nome)
            print("Paciente removido do sistema!")
            print("")
        elif(value2 != 8):
            print("Valor digitado inválido, tente novamente.")
            print("")

    elif(value1 == 2):
         print("O que deseja fazer agora?")
         value3 = int(input(
             "1 - Cadastrar uma nova vacina no sistema \n"
             "2 - Consultar dados de uma vacina \n"
             "3 - Verificar fabricante de alguma vacina \n"
             "4 - Vincular vacina a um fabricante \n"
             "5 - Remover alguma vacina do sistema \n"
             "6 - Verificar quantas unidades de alguma vacina há no sistema\n"
             "7 - Voltar ao menu principal \n"

         ))

         if (value3 == 1):
             nome = input("Informe o nome da vacina: ")
             eficacia = input("Agora informe a eficácia da vacina: ")
             validade = input("Por último, informe também o tempo de validade da vacina: ")
             crud.createVaccine(nome,eficacia,validade)
             print("Vacina adicionada no sistema!")
             print('')
         elif (value3 == 2):
             nome = input("Informe o nome da vacina: ")
             crud.readVaccine(nome)
             print('')
         elif (value3 == 3):
             nomeVacina = input("Informe o nome da vacina: ")
             crud.findManufacturerByVaccine(nomeVacina)
             print("")
         elif (value3 == 4):
             nomeVacina = input("Informe o nome da vacina: ")
             nomeFabricante = input("Informe agora o nome do fabricante da vacina: ")
             crud.createRelationshipVaccineManufacturer(nomeVacina,nomeFabricante)
             print("Vacina vinculada ao fabricante informado!")
             print("")
         elif (value3 == 5):
             nome = input("Informe o nome da vacina: ")
             crud.deleteVaccine(nome)
             print("Vacina deletada do sistema!")
             print("")
         elif (value3 == 6):
             nome = input("Informe o nome da vacina: ")
             print('Há ' + (str(crud.countVaccine(nome)) + ' vacina(s) cadastrada no sistema'))
         elif (value3 != 7):
             print("Valor digitado inválido, tente novamente.")
             print("")

    elif(value1 == 3):
        print("O que deseja fazer agora?")
        value4 = int(input(
            "1 - Cadastrar um novo fabricante de vacinas no sistema \n"
            "2 - Consultar dados de algum fabricante \n"
            "3 - Remover algum fabricante do sistema \n"
            "4 - Voltar ao menu principal \n"
        ))

        if (value4 == 1):
            nome = input("Informe o nome do fabricante: ")
            sede = input("Informe o país onde fica a sede do fabricante: ")
            fundacao = input("Por último, informe o ano de fundação da empresa fabricante: ")
            crud.createManufacturer(nome,sede,fundacao)
            print("Fabricante adicionado no sistema!")
            print('')
        elif (value4 == 2):
            nome = input("Informe o nome do fabricante: ")
            crud.readManufacturer(nome)
            print('')
        elif (value4 == 3):
            nome = input("Informe o nome do fabricante: ")
            crud.deleteManufacturer(nome)
            print("Fabricante deletado do sistema!")
            print("")
        elif (value4 != 4):
            print("Valor digitado inválido, tente novamente.")
            print("")

    elif(value1 == 4):
        print("O que deseja fazer agora?")
        value5 = int(input(
            "1 - Cadastrar um novo PSF no sistema \n"
            "2 - Consultar dados de algum PSF \n"
            "3 - Atualizar o endereço de algum PSF \n"
            "4 - Remover algum PSF do sistema \n"
            "5 - Voltar ao menu principal \n"
        ))

        if (value5 == 1):
            numIdent = input("Informe o número de identificação do PSF: ")
            cidade = input("Agora informe a cidade onde fica localizado o PSF: ")
            endereco = input("Por último, informe o endereço da unidade de atendimento do PSF: ")
            crud.createPSF(numIdent,endereco,cidade)
            print("PSF adicionado ao sistema!")
            print('')
        elif (value5 == 2):
            numIdent = input("Informe o número de identificação do PSF: ")
            cidade = input("Agora informe a cidade onde fica localizado o PSF: ")
            crud.readPSF(numIdent,cidade)
            print('')
        elif (value5 == 3):
            numIdent = input("Informe o número de identificação do PSF: ")
            cidade = input("Agora informe a cidade onde fica localizado o PSF: ")
            endereco = input("Por último, informe o endereço do PSF a ser atualizado no sistema: ")
            crud.updatePSF(cidade,numIdent,endereco)
            print("Endereço do PSF atualizado no sistema!")
            print("")
        elif (value5 == 4):
            numIdent = input("Informe o número de identificação do PSF: ")
            cidade = input("Agora informe a cidade onde fica localizado o PSF: ")
            crud.deletePSF(numIdent,cidade)
            print("PSF deletado do sistema!")
            print("")
        elif (value5 != 5):
            print("Valor digitado inválido, tente novamente.")
            print("")
    else:
        print("Valor digitado inválido, tente novamente.")
        print("")