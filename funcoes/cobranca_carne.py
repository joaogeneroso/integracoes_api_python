from gerencianet import Gerencianet

credentials = {
    'client_id': 'Client_Id_98feb8e4aa192c7d6badc5efdbdec83fa03658ae',
    'client_secret': 'Client_Secret_8d7bd22e1432364e8759f93a549ec3edf00f3a72',
    'pix_cert': './seuCert.pem',
    'sandbox': True
}

gn = Gerencianet(credentials)

def id():
    return int(input("ID: "))

def name():
    return str(input("Nome: "))

def value():
    return int(input("Valor: "))

def amount():
    return int(input("Quantidade: "))

def name_person():
    return str(input("Nome pessoa: "))

def email():
    return str(input("Email: "))

def cpf():
    return str(input("CPF: "))

def birth():
    return str(input("Aniversario: "))

def phone_number():
    return str(input("Telefone: "))



def createCarnet():
    body = {
    'items': [{
        'name': name(),
        'value': value(),
        'amount': amount()
        }],
        'customer': {
            'name': name_person(),
            'email': email(),
            'cpf': cpf(),
            'birth': birth(),
            'phone_number': phone_number()
        },
        'repeats': int(input("Repetições: ")),
        'expire_at': str(input("Data: "))
    }
    response = gn.create_carnet(body=body)
    print(response)

def detailCarnet():
    params = {
    'id': id()
    }

    response =  gn.detail_carnet(params=params)
    print(response)