from gerencianet import Gerencianet

credentials = {
    'client_id': 'Client_Id_98feb8e4aa192c7d6badc5efdbdec83fa03658ae',
    'client_secret': 'Client_Secret_8d7bd22e1432364e8759f93a549ec3edf00f3a72',
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