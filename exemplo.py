from gerencianet import Gerencianet

credentials = {
    'client_id': 'Digite seu Client_Id',
    'client_secret': 'Digite seu Client_Secret',
    'pix_cert': './seuCert.pem',
    'sandbox': True
}

gn = Gerencianet(credentials)

body = {
    'items': [{
        'name': "Carne",
        'value': 5000,
        'amount': 1
    }],
    'shippings': [{
        'name': "Default Shipping Cost",
        'value': 100
    }]
}

print (gn.create_charge(body=body))