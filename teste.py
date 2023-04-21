##########QUESTÃO 2

def fibo(num):
    if num <= 1: 
        return num
    else:
        return fibo(num-1) + fibo(num-2)
    
num_input = int(input('Informe um número: '))

i = 0
while True:
    num_fibo = fibo(i)
    i += 1
    if num_fibo > num_input:
        print(f'O número {num_input} não está na sequência')
        break
    elif num_fibo == num_input:
        print(f'O número {num_input} está na sequência') 
        break

########QUESTÃO 5
def reverte_palavra(palavra):
    if len(palavra) == 1:
        return palavra
    else:
        return palavra[-1] + reverte_palavra(palavra[:-1])
    

palavra_input = str(input('Informe uma palavra: '))

print(reverte_palavra(palavra_input))