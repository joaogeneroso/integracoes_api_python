from gerencianet import Gerencianet
import credentials

gn = Gerencianet(credentials)

params = {
  'id': 1660091
}
 
body = {
  'email': "lexi.oliveira@gerencianet.com.br"
}
 
print(gn.resend_billet(params=params, body=body))