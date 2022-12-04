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
            "3 - Atualizar dados de um paciente \n"
            "4 - Adicionar uma vacina a ficha do paciente \n"
            "5 - Vincular paciente a um PSF \n"
            "6 - Remover um paciente do sistema \n"
            "7 - Voltar ao menu principal \n"
        ))

    if(value1 == 2):
         print("O que deseja fazer agora?")
         value2 = int(input(
             "1 - Cadastrar uma nova vacina no sistema \n"
             "2 - Consultar dados de uma vacina \n"
             "3 - Atualizar dados de uma vacina \n"
             "4 - Verificar fabricante de alguma vacina \n"
             "5 - Vincular vacina a um fabricante \n"
             "6 - Remover alguma vacina do sistema \n"
             "7 - Voltar ao menu principal \n"
         ))

    if(value1 == 3):
        print("O que deseja fazer agora?")
        value2 = int(input(
            "1 - Cadastrar um novo fabricante de vacinas no sistema \n"
            "2 - Consultar dados de algum fabricante \n"
            "3 - Atualizar dados de algum fabricante \n"
            "4 - Remover algum fabricante do sistema \n"
            "5 - Voltar ao menu principal \n"
        ))
    
    if(value1 == 4):
        print("O que deseja fazer agora?")
        value2 = int(input(
            "1 - Cadastrar um novo PSF no sistema \n"
            "2 - Consultar dados de algum PSF \n"
            "3 - Atualizar dados de algum PSF \n"
            "4 - Remover algum PSF do sistema \n"
            "5 - Voltar ao menu principal \n"
        ))




    if (value == 1):
        name = input("Entre com o nome do paciente: \n")
        crud.readPerson(name)
    if(value == 2):
        vacina = input("Entre com o nome da vacina: \n")
        crud.readVaccine(vacina)
    if(value == 9):
        vacina = input("Entre com o nome da vacina: \n")
        crud.findManufacturerByVaccine(vacina)

    menu = False



