from gerencianet import Gerencianet
import credentials

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

def cancelCarnet():
    params = {
    'id': id()
    }

    response = gn.cancel_carnet(params=params)
    print(response)

def cancelParcel():
    params = {
    'id': id(),
    'parcel': int(input("Parcela: "))
    }

    response = gn.cancel_parcel(params=params)
    print(response)

def resendCarnet():
    params = {
    'id': id()
    }

    body = {
        'email': email()
    }

    response =  gn.resend_carnet(params=params, body=body)
    print(response)

def resendParcel():
    params = {
    'id': id(),
    'parcel': int(input("Parcela: "))
    }

    body = {
        'email': email()
    }

    response =  gn.resend_parcel(params=params, body=body)
    print(response)