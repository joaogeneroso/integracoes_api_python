from asyncio.windows_events import NULL
from urllib import response
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

def repeats():
    return int(input("Repetições: "))

def interval():
    return int(input("Intervalo: "))



def createPlan():
    body = {
    'name': name(),
    'repeats': repeats(),
    'interval': interval()
    }
    
    response =  gn.create_plan(body=body)
    print(response)

def getPlans():
    params = {
    'name': name(),
    'limit': int(input("Numero max de assinaturas: ")),
    'offset': int(input("A partir de qual registro a busca será realizada: "))
    }

    response =  gn.get_plans(params=params)
    print(response)

def deletePlan():
    params = {
    'id': id()
}

    response =  gn.delete_plan(params=params)
    print(response)

def createSubscription():
    params = {
    'id': id()
    }

    body = {
        'items': [{
            'name': name(),
            'value': value(),
            'amount': amount()
        }]
    }

    response =  gn.create_subscription(params=params, body=body)
    print(response)

def detailSubscription():
    params = {
    'id': id()
}

    response =  gn.detail_subscription(params=params)
    print(response)

def paySubscription():
    body = {
    'payment': {
        'banking_billet': {
            'expire_at': str(input("Data: ")),
            'customer': {
                'name': name_person(),
                'email': email(),
                'cpf': cpf(),
                'birth': birth(),
                'phone_number': phone_number()
                }
            }
        }
    }

    params = {
        'id': id() # informe o subscription_id
    }

    response = gn.pay_subscription(params=params, body=body)
    print(response)