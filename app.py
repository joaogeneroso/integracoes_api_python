from email.policy import default
from funcoes import cobranca_geral, cobranca_carne, cobranca_assinatura

menu_1 = str("     -MENU-      \n0 - Encerrar\n\nCobranças via Boleto ou Cartão\n1 - Criar nova cobrança\n2 - Retornar informações de cobrança existente"
"\n3 - Retornar informações de cobrança existente"
"\n4 - Alterar data de vencimento de uma cobrança existente"
"\n5 - Cancelar uma cobrança existente"
"\n6 - Associa método de pagamento boleto à uma cobrança já criada"
"\n7 - Reenvio do boleto bancário para o e-mail desejado"
"\n8 - Acrescentar descrição ao histórico de uma cobrança"
"\n9 - Retorna um link para uma tela de pagamento da Gerencianet"
"\n10 - Alterar determinados parâmetros/atributos de um link de pagamento existente"
"\n11 - Baixa manual em uma determinada cobrança"
"\n12 - Criar nova cobrança por boleto com pagador atribuido"
"\n\nCobranças via Carnê"
"\n13 - Cria um carnê"
"\n14 - Retorna informações de carnê existente"
"\n\nCobranças via Assinaturas"
"\n15 - Cria o plano de assinatura"
"\n16 - Retorna informações de um plano"
"\n17 - Cancela um plano de assinatura"
"\n18 - Cria assinaturas para vincular a planos"
"\n19 - Retorna informações de uma assinatura vinculada a um plano"
"\n20 - Associa método de pagamento à uma assinatura já criada")

def menu_pinc(operador_1):
    match operador_1:
        case 0:
            return

        case 1:
            cobranca_geral.createCharge()
            main()

        case 2:
            cobranca_geral.detailCharge()
            main()

        case 3:
            cobranca_geral.updateChargeMetadata()
            main()

        case 4:
            cobranca_geral.updateBillet()
            main()

        case 5:
            cobranca_geral.cancelCharge()
            main()

        case 6:
            cobranca_geral.payCharge_boleto()
            main()

        case 7:
            cobranca_geral.resendBillet()
            main()

        case 8:
            cobranca_geral.createChargeHistory()
            main()

        case 9:
            cobranca_geral.linkCharge()
            main()

        case 10:
            cobranca_geral.updateChargeLink()
            main()

        case 11:
            cobranca_geral.settleCharge()
            main()

        case 12:
            cobranca_geral.oneStepBoleto()
            main()

        case 13:
            cobranca_carne.createCarnet()
            main()

        case 14:
            cobranca_carne.detailCarnet()
            main()

        case 15:
            cobranca_assinatura.createPlan()
            main()

        case 16:
            cobranca_assinatura.getPlans()
            main()

        case 17:
            cobranca_assinatura.deletePlan()
            main()

        case 18:
            cobranca_assinatura.createSubscription()
            main()

        case 19:
            cobranca_assinatura.detailSubscription()
            main()

        case 20:
            cobranca_assinatura.paySubscription()
            main()

        case _:
            print("Entrada Invalida")
            main()

def main():
    print("\n")
    print(menu_1)
    operador_1 = int(input("Digite sua opção: "))
    print("\n")
    menu_pinc(operador_1)

main()