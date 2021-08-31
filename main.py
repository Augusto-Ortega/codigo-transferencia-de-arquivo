
nome = input("Você dirige? ")
if nome == "sim" or "claro" or "yes" :
    nome = True
elif nome != "sim" :
    nome = False
if nome == True:
    nome = bool(True)
    
elif nome == False:
    nome = bool(False)
idade = int(input("Qual sua idade? "))

if idade < 18 and nome == True:
    print("Ele é menor de idade e dirige, ligue 190!")
if idade >= 18 and nome == True:
    print("Ele é maior de idade e dirige. Tudo normal.")
if idade >= 18 and nome == False: 
    print ("Ele não é menor de idade e não dirige. Tudo normal.")
if idade < 18 and nome == False:
    print("Ele é menor de idade e não dirige. Tudo normal.")
