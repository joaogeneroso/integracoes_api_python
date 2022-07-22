from gerencianet import Gerencianet

credentials = {
    'client_id': 'Client_Id_98feb8e4aa192c7d6badc5efdbdec83fa03658ae',
    'client_secret': 'Client_Secret_8d7bd22e1432364e8759f93a549ec3edf00f3a72',
    'pix_cert': './seuCert.pem',
    'sandbox': True
}

gn = Gerencianet(credentials)

params = {
    'id': 1660581
}
 
body = {
    'payment': {
        'credit_card': {
            'installments': 1,
            'payment_token': "5bd97fc8b5dfa59d90d90265758f6d841074b33a",
            'billing_address': {
                'street': "Av. JK",
                'number': 909,
                'neighborhood': "Bauxita",
                'zipcode': "35400000",
                'city': "Ouro Preto",
                'state': "MG"
            },
            'customer': {
                'name': "Gorbadoc Oldbuck",
                'email': "oldbuck@gerencianet.com.br",
                'cpf': "94271564656",
                'birth': "1977-01-15",
                'phone_number': "5144916523"
            }
        }
    }
}
 
print(gn.pay_charge(params=params, body=body))