from gerencianet import Gerencianet

credentials = {
    'client_id': 'Client_Id_98feb8e4aa192c7d6badc5efdbdec83fa03658ae',
    'client_secret': 'Client_Secret_8d7bd22e1432364e8759f93a549ec3edf00f3a72',
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