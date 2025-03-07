import os 

mensagens = []

nome = input ("Coloque seu nome: ")

while True:

    os.system('cls')


    if len(mensagens)> 0:
        for m in mensagens:
            print (m['nome'], "-", m['texto'] )

    print("__________")


    texto = input ("mensagem: ")
    if texto == "fim":
        break

    mensagens.append({
        "nome" : nome,
        "texto": texto

    })