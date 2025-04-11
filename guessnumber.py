import random

gen_numb = random.randint(1,10)

print("Jogo Guess the number!")
print(gen_numb)

while True: 
    inp=input("Advinha o numero! -->")

    try:
        if int(inp) == gen_numb:
            print("Acercaste BOI!")
            break 
        else:
            # 1- Fazer verificação se o numero introduzido é maior ou menor ao gerado. 
            if int(inp) > gen_numb:
                print("O numero inserido é maior ao numero gerado.")
            else:
                print ("o numero inserido é menor ao numero gerado")
                
    except Exception as e:
        print(f"Ocorreu um erro: {e}")
        
           
    print("Tenta outra vez!")  