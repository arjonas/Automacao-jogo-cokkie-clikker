from selenium import webdriver
import time



# def comprar(saldo,contador,precos,listaa):
#
#     while contador < len(precos):
#
#         if int(saldo) >= int(precos[contador]):
#             chave= precos[contador]
#             classe = listaaa[chave]
#             print(f'aqui esta a classe {classe}')
#             compra = driver.find_element_by_id(classe)
#             print(compra)
#             compra.click()
#
#             money = driver.find_element_by_id('money')
#             saldo = int(money.text)
#         contador = contador +1
#         #print(f'numero {contador}')



def clicar(bicoito,contador,saldo):
    print(contador, len(precos))
    c = True


    while c :
        contador = 0
        tempo_start = time.time()

        tempo_saida = tempo_start + 5
        while time.time() < tempo_saida:

            bicoito.click()




        while contador <= 7:
            print(contador)
            print(saldo)
            print(precos[contador])
            if int(saldo) >= int(precos[contador]):
                chave= precos[contador]
                classe = listaaa[chave]
                print(f'aqui esta a classe {classe}')
                compra = driver.find_element_by_id(classe)
                print(compra)
                compra.click()
            contador = contador + 1

            money = driver.find_element_by_id('money')
            saldo = int(money.text.replace(',',''))



        #print(f'numero {contador}')


CONTADOR = 6

chrome_driver_path = r'C:\Users\ney_r\Desenvolvimento\chromedriver.exe'

driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get('http://orteil.dashnet.org/experiments/cookie/')


biscoito = driver.find_element_by_id('cookie')


money = driver.find_element_by_id('money')
precos = driver.find_elements_by_tag_name('b')




shop = [precos[n] for n in range(10,18)]
shopdic =[]
shop2 = [item.text.split('-') for item in shop]
for lista  in shop2:

    shopdic.append({lista[0]:int(lista[1].replace(',',''))})

print(shopdic)

print(money.text)



saldo = int(money.text)





listaaa  = {shopdic[0]['Cursor ']:'buyCursor',shopdic[1]['Grandma ']:'buyGrandma',shopdic[2]['Factory ']:'buyFactory',shopdic[3]['Mine ']:'buyMine',shopdic[4]['Shipment ']:'buyShipment',shopdic[5]['Alchemy lab ']:'buyAlchemy lab',shopdic[6]['Portal ']:'buyPortal',shopdic[7]['Time machine ']:'buyTime machine'}
print(listaaa)



contador = 0


precos= [shopdic[0]['Cursor '],shopdic[1]['Grandma '],shopdic[2]['Factory '],shopdic[3]['Mine '],shopdic[4]['Shipment '],shopdic[5]['Alchemy lab '],shopdic[6]['Portal '],shopdic[7]['Time machine ']]
numero = 7



precos.sort(reverse=True)


print(precos)
#
# for valor in precos:
#     if saldo >= valor :
#         chave =valor
#







clicar(biscoito,contador,saldo)

saldo = money.text


#
# for produto in listaaa:
#
#     if produto[numero] >=  saldo:
#
#         classe = pr

