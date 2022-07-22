from gerencianet import Gerencianet
import credentials

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