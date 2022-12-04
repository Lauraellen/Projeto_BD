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
        "9 - Verificar fabricante de alguma vacina \n"

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



