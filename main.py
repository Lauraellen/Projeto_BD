from db.crud import CRUD

crud = CRUD()

# crud.updatePerson('Lucas', 59890104008)
# crud.updatePSF('São Paulo', '2', 'Rua Paracatu, 125, Bairro Parque Imperial')
menu = True
while(menu):
    print("Seja bem vindo ao sistema de controle de vacinas!")
    print("O que deseja fazer?")

    value = int(input(
        "1 - Verificar pacientes cadastrados no sistema \n"
        "2 - Verificar vacinas disponiveis \n"
        "3 - Verificar dados das PSF \n"
        "4 - Verificar dados do fabricante \n"
        "5 - Atualizar dados do paciente \n"
        "6 - Atualizar dados do PSF \n"
        "7 - Remover paciente do sistema \n"
        "8 - Remover vacina do sistema \n"

    ))

    menu = False



