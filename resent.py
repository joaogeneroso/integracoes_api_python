from gerencianet import Gerencianet

credentials = {
    'client_id': 'Digite seu Client_Id',
    'client_secret': 'Digite seu Client_Secret',
    'pix_cert': './seuCert.pem',
    'sandbox': True
}

gn = Gerencianet(credentials)

params = {
  'id': 1660091
}
 
body = {
  'email': "lexi.oliveira@gerencianet.com.br"
}
 
print(gn.resend_billet(params=params, body=body))