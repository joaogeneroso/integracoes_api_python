from gerencianet import Gerencianet

credentials = {
    'client_id': 'Client_Id_98feb8e4aa192c7d6badc5efdbdec83fa03658ae',
    'client_secret': 'Client_Secret_8d7bd22e1432364e8759f93a549ec3edf00f3a72',
    'pix_cert': './seuCert.pem',
    'sandbox': True
}

gn = Gerencianet(credentials)

def nome():
    name = str(input("Nome do produto: "))
    return name
def valor():
    value = int(input("Valor do produto: "))
    return value
def quantidade():
    amount = int(input("Quantidade: "))
    return amount
def id():
    id = int(input("ID: "))

    params = {
    'id': id
    }
    return params

def createCharge():
    name = nome()
    value = valor()
    amount = quantidade()

    body = {
    'items': [{
        'name': name,
        'value': value,
        'amount': amount
    }]
    }
    print(gn.create_charge(body=body))

def detailCharge():
    response =  gn.detail_charge(params=id())
    print(response)

def updateChargeMetadata():
    notification_url = str(input("URl de notificação: "))
    custom_id = str(input("Custom ID:"))
    body = {
        'notification_url': notification_url,
        'custom_id': custom_id
    }
    
    gn.update_charge_metadata(params=id(), body=body)

def updateBillet():
    expire_at = str(input("Data de expiração: "))
    body = {
    'expire_at': expire_at
    }

    response =  gn.update_billet(params=id(), body=body)
    print(response)

def cancelCharge():
    response = gn.cancel_charge(params=id())
    print(response)

def payCharge_boleto():
    body = {
        'payment': {
            'banking_billet': {
                'expire_at': str(input("Data de expiração: ")),
                'customer': {
                    'name': str(input("Nome: ")),
                    'email': str(input("Email: ")),
                    'cpf': str(input("CPF: ")),
                    'birth': str(input("Data de aniversario: ")),
                    'phone_number': str(input("Numero de celular: "))
                }
            }
        }
    }
    
    print(gn.pay_charge(params=id(), body=body))

def resendBillet():
    body = {
        'email': str(input("Email: "))
    }
    
    print(gn.resend_billet(params=id(), body=body))

def createChargeHistory():
    body = {
    'description': str(input("Digite a descrição: "))
    }
    
    print(gn.create_charge_history(params=id(), body=body))

def linkCharge():
    body = {
    'items': [{
        'name': nome(),
        'value': valor(),
        'amount': quantidade()
    }],
    'settings': [{
        'payment_method': 'all',
        'expire_at': str(input("Data de expiração: ")),
        'request_delivery_address': False,
    }]
    }

    #print(gn.link_charge(body=body))

def updateChargeLink():
    body = {
    'billet_discount': 1,
    'card_discount': 1,
    'message': '',
    'expire_at': str(input("Data de expiração: ")),
    'request_delivery_address': False,
    'payment_method': 'all'
    }

    response = gn.update_charge_link(params=id(), body=body)
    print(response)

def settleCharge():
    response = gn.settle_charge(params=id())
    print(response)

def oneStepBoleto():
    body = {
        'items': [{
        'name': str(input("Nome: ")),
        'value': int(input("Valor: ")),
        'amount': int(input("Quantidade: "))
        }],
        'shippings': [{
            'name': str(input("Shipping: ")),
            'value': int(input("Valor shipping: "))
        }],
        'payment': {
            'banking_billet': {
                'expire_at': str(input("Data de expiração: ")),
                'customer': {
                    'name': str(input("Nome: ")),
                    'email': str(input("Email: ")),
                    'cpf': str(input("CPF: ")),
                    'birth': str(input("Aniversario: ")),
                    'phone_number': str(input("Telefone: "))
                
                }
            }   
        }
    }

    response = gn.create_charge_onestep(params=None, body=body)
    print(response)