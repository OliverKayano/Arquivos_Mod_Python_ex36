# Operacoes com arquivos e diretorios em Python:
#Algoritmo Op_ArqMod-Ex36.

import os

#Declarar.
linha : str = ''
dir: str = ''
arq : str = ''
txt : str = ''

def main():
    num : int = 0
    fatorial : int = 1
    soma : float = 1.0
    aux : int = 0
    
    num = int(input("Insira um valor: "))
    escreveArq(aux, fatorial, soma, num)
    print(soma)

    for aux in range (2, (num+1), 1):
        fatorial = fator(fatorial, aux)
        soma += divisao(fatorial)
        print (" + ", divisao(fatorial))
        escreveArq(aux, fatorial, soma, num)

    print(f"\n\nSoma = {soma}")

#Fim.

def fator(f, ax):
    valor : int = 0

    valor = f*ax
    return valor

#Fim-segue.

def divisao(fat):
    div : float = 0

    div = 1/fat
    return div

#Fim-segue.

def escreveArq(cont, fato, s, final):
    #Variaveis grobais:
    global dir
    global arq
    global txt
    global linha

    dir = '/tmp/exercicios/'
    arq = 'ex36.txt'

    #Variaveis locais:
    file: str = ''
    tipo: str = ''
    enc: str = ''
    
    if not (os.path.exists(dir)):
        #Criando o diretorio.
        os.mkdir(dir)
        os.makedirs(dir, exist_ok = True)
        os.chmod(dir, 0o744) #Autorizacao de criacao, leitura e alteracao para o primeiro usuario, leitura para os demais.

    if (os.path.exists(dir) and os.path.isdir(dir)):
        tipo = 'w'
        txt = dir + arq
        enc = 'utf-8'
        linha = str(s)

        if (os.path.exists(txt)) and (cont != 0):
            tipo = 'a'
            linha = ' + '+ '1/' + str(fato)

        with open (txt, tipo, encoding=enc) as file:
            file.write(linha)

        if final == cont:
            linha = '\n\nSoma = ' + str(s)
        
            with open (txt, tipo, encoding=enc) as file:
                file.write(linha)
    
    else:
        print("Diretorio invalido")
    
    #Fim-se.
#Fim-segue.

if __name__ == '__main__':
   main()
#Fim-se.