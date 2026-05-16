import random

print("tire dez 6 seguidos para vencer!")
v1=1
v2=6
coins=2
ct_game=0
coins_multiplier=0
upgrade_shop=0
lucky_number=6
coins_reducer=0.20
guess=input("faça sua aposta")
guess1=0
while True:
    def shop_randomizer():
        for i in range(1,4):
         sorteio_loja = random.randint(1,10)
         sorteio_loja=sorteio_loja + upgrade_shop
         if sorteio_loja ==1:
            j1='1'
            print(j1)
         if sorteio_loja ==2:
            j2='2'
            print(j2)
         if sorteio_loja ==3:
            j3='3'
            print(j3)
         if sorteio_loja ==4:
            j4='4'
            print(j4)
         if sorteio_loja ==5:
            j5='5'
            print(j5)
         if sorteio_loja ==6:
            j6='6'
            print(j6)
         if sorteio_loja ==7:
            j7='7'
            print(j7)
         if sorteio_loja ==8:
            j8='8'
            print(j8)
         if sorteio_loja ==9:
            j9='9'
            print(j9)
         if sorteio_loja ==10:
            j10='10'
            print(j10)
    def help():
        print('/exit sai do jogo')
        print('/g rola o dado')
        print('/shop entra na loja')
        print('/buy "nome do item" compra um item na loja')
        print('/exit shop sai da loja')
        print('/"nome do item" acessa as informações do item')


    def shop():
        print("itens disponiveis")
        shop_randomizer()

        print("dinheiro","--",coins,"--")
    def item():
        print("item comprado com sucesso")



    def game():
        print("você tirou --",sorteio,"--")
        print(f'dinheiro = --{coins:.2f}--')
        print("\nvocê tirou",ct_game,"\n6 seguidos!")

    print("comandos: /g /shop /exit /help")
    command= input('\ndigite um comando')
    if coins <=0:
        break
    if command== '/g' :
        guess1
        if guess1=='win':
            sorteio = random.randint(v1, v2)
            if sorteio ==lucky_number:
                ct_game=ct_game+1
                coins=coins+1
                coins=coins+coins_multiplier
                game()
                if ct_game==10:
                    print("VOCÊ VENCEU!!!")
                    s=str(input("quer continuar jogando?"))
                    if s== 'sim':
                        continue
                    if s== 'nao':
                        break
            else:
                ct_game=0
                coins=coins-coins_reducer
                coins = coins + coins_multiplier
                game()
                if coins==0:
                    print("game over")
                    break

    if command== '/shop' and ct_game<=1:
        while True:
            print(shop())
            command_shop = input('\ndigite um comando')
            ct_game=ct_game-1
            if command_shop =='/exit shop':
                break
            if command_shop == '/help':
                help()
                break
            if command_shop =='/buy 1'and shop()=='1':

                v1=+1
                coins=coins-1
                item()
                break
            if command_shop =='/buy 2'and shop()=='2':
                coins_multiplier=coins_multiplier+0.10
                coins=coins-2
                item()
                break
            if command_shop =='/buy 3'and shop()=='3':
                coins=coins-3
                upgrade_shop = upgrade_shop+1
                item()
                break
            if command_shop =='/buy 4'and shop()=='4':
                coins=coins-4
                lucky_number=lucky_number or 1
                item()
                break
            if command_shop == '/buy 5' and shop()=='5':
                coins = coins - 5
                coins_reducer=1
                guess1=guess
                item()
                break
    if command == '/help':
        help()





