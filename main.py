from db.crud import CRUD

crud = CRUD()

menu = True
while(menu):
    print("Seja bem vindo ao sistema de controle de vacinas!")
    print("O que deseja fazer?")

    value = int(input(
        "1 - Verificar dados do paciente cadastrado no sistema \n"
        "2 - Verificar dados da vacina \n"
        "3 - Verificar dados das PSF \n"
        "4 - Verificar dados do fabricante \n"
        "5 - Atualizar dados do paciente \n"
        "6 - Atualizar dados do PSF \n"
        "7 - Remover paciente do sistema \n"
        "8 - Remover vacina do sistema \n"

    ))

    if (value == 1):
        crud.readPerson('Lucas')
    if(value == 2):
        crud.readVaccine('Influenza')

    menu = False



