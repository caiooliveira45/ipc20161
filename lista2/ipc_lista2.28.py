#
#Igor Menezes Sales Vieira 1615310007 
#Kid Mendes de Oliveira Neto 1615310011
#Victor Rafael da Silva e Silva 1615310025
#Josue Vasques Catachunga 1615310054
#

carnes = input("Qual o tipo de carne? (1)-File duplo;(2)-Alcatra;(3)-Picanha\n")
quantidade_carne = float(input("Quantos quilogramas de carne?\n"))
pagamento = input("Pagamento com o cartao Tabajara? (1)Sim ou (0)Nao\n")

if(carnes == 1):
    if(quantidade_carne <= 5):
        preco_total = (quantidade_carne*4.90)
        if(pagamento == 1):
            cartao_tabajara = (preco_total*5/100)
            preco_desconto = (preco_total-cartao_tabajara)
            print("Nota fiscal")
            print("File Duplo")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Cartao tabajara")
            print("Valor do desconto:R$%2.f"%cartao_tabajara)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        if(pagamento == 0):
            preco_desconto = preco_total
            print("Nota fiscal")
            print("File Duplo")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Outra forma de pagamento")
            print("Valor do desconto:R$",0.00)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        
    if(quantidade_carne > 5):
        preco_total = (quantidade_carne*5.80)
        if(pagamento == 1):
            cartao_tabajara = (preco_total*5/100)
            preco_desconto = (preco_total-cartao_tabajara)
            print("Nota fiscal")
            print("File Duplo")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Cartao tabajara")
            print("Valor do desconto:R$%2.f"%cartao_tabajara)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        if(pagamento == 0):
            preco_desconto = preco_total
            print("Nota fiscal")
            print("File Duplo")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Outra forma de pagamento")
            print("Valor do desconto:R$",0.00)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
if(carnes == 2):
    if(quantidade_carne <= 5):
        preco_total = (quantidade_carne*5.90)
        if(pagamento == 1):
            cartao_tabajara = (preco_total*5/100)
            preco_desconto = (preco_total-cartao_tabajara)
            print("Nota fiscal")
            print("Alcatra")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Cartao tabajara")
            print("Valor do desconto:R$%2.f"%cartao_tabajara)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        if(pagamento == 0):
            preco_desconto = preco_total
            print("Nota fiscal")
            print("Alcatra")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Outra forma de pagamento")
            print("Valor do desconto:R$",0.00)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
                    
    if(quantidade_carne > 5):
        preco_total = (quantidade_carne*6.80)
        if(pagamento == 1):
            cartao_tabajara = (preco_total*5/100)
            preco_desconto = (preco_total-cartao_tabajara)
            print("Nota fiscal")
            print("Alcatra")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Cartao tabajara")
            print("Valor do desconto:R$%2.f"%cartao_tabajara)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        if(pagamento == 0):
            preco_desconto = preco_total
            print("Nota fiscal")
            print("Alcatra")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Outra forma de pagamento")
            print("Valor do desconto:R$",0.00)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
if(carnes == 3):
    if(quantidade_carne <= 5):
        preco_total = (quantidade_carne*6.90)
        if(pagamento == 1):
            cartao_tabajara = (preco_total*5/100)
            preco_desconto = (preco_total-cartao_tabajara)
            print("Nota fiscal")
            print("Picanha")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Cartao tabajara")
            print("Valor do desconto:R$%2.f"%cartao_tabajara)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        if(pagamento == 0):
            preco_desconto = preco_total
            print("Nota fiscal")
            print("Picanha")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Outra forma de pagamento")
            print("Valor do desconto:R$",0.00)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
                                
    if(quantidade_carne > 5):
        preco_total = (quantidade_carne*7.80)
        if(pagamento == 1):
            cartao_tabajara = (preco_total*5/100)
            preco_desconto = (preco_total-cartao_tabajara)
            print("Nota fiscal")
            print("Picanha")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Cartao tabajara")
            print("Valor do desconto:R$%2.f"%cartao_tabajara)
            print("Valor a se pagar:R$%2.f"%preco_desconto)
        if(pagamento == 0):
            preco_desconto = preco_total
            print("Nota fiscal")
            print("Picanha")
            print("Quantidade de carne:",quantidade_carne)
            print("Preco total: R$%2.f"%preco_total)
            print("Outra forma de pagamento")
            print("Valor do desconto:R$",0.00)
            print("Valor a se pagar:R$%2.f"%preco_desconto)

            
            
        
