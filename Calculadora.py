#import------------------------------------------------
import os

#functions---------------------------------------------
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    return

def traz_resultado(lista):
    separa_parentesis(lista)
    valores=monta_digitos(lista)
    operacoes=monta_operacoes(lista)
    multiplicacoes(valores,operacoes)
    return soma(valores,operacoes)

def limpa_zero_esquerda(lista):
    if lista[0]=='0' and (lista[1] != '.' and lista[1] not in operadores):
        del lista[0]
    i=1
    while i<len(lista)-1:
        if lista[i]=='0' and lista[i-1] in operadores:
            del lista[i]
        i+=1
    return lista

def limpa_virgula(lista):
    for i in range(len(lista)):
        if lista[i]==',':
            lista[i]='.'
    return lista

def monta_digitos(lista):
    numeros=[]
    temp=''
    if lista[0]=='-':
        temp+=lista[0]
        del lista[0]
    try:
        for i in range(len(lista)):
            if (lista[i]=='-' and lista[i-1] in nao_numeros and lista[i+1] not in nao_numeros) or lista[i] not in operadores:
                temp+=lista[i]
                if lista[i]=='-' and lista[i-1] in operadores and lista[i+1] not in nao_numeros:
                    lista[i]='APAGAR'
            else:
                numeros.append(float(temp))
                temp=''
        if temp!='':
            numeros.append(float(temp))
        return numeros
    except:
        raise
    i=0
    while i <= range(lista[i]):
        if lista[i]=='APAGAR':
            del lista[i]
            i-=1
        i+=1


def monta_operacoes(lista):
    operacoes=[]
    for i in range(len(lista)):
        if lista[i] in operadores:
            operacoes.append(lista[i])
    return operacoes

def multiplicacoes(numeros,operacoes):
    try:
        i=0
        while i< (len(operacoes)):
            if operacoes[i] in ('*','/'):
                if operacoes[i]=='*':
                    numeros[i]*=numeros[i+1]
                elif operacoes[i]=='/':
                    numeros[i]/=numeros[i+1]
                del numeros[i+1]
                del operacoes[i]
                i-=1
            i+=1
        return
    except ZeroDivisionError:
        raise ZeroDivisionError

def soma(numeros,operacoes):
    i=0
    while i< (len(operacoes)):
        if operacoes[i] in ('+','-'):
            if operacoes[i]=='+':
                numeros[i]+=numeros[i+1]
            elif operacoes[i]=='-':
                numeros[i]-=numeros[i+1]
            del numeros[i+1]
            del operacoes[i]
            i-=1
        i+=1
    return numeros[0]

def repetir(msg=''):
    if msg!='':
        print(msg)
    try:
        continuar=str(input('\nPressione Enter para repetir ou S para sair\n'))
        clear_screen()
        if len(continuar)>0 and continuar[0].lower()=='s':
            return False
        else:
            return True
    except KeyboardInterrupt:
        clear_screen()
        pass

def separa_parentesis(lista):
    parentesis_aberto=False
    parentesis_achado=True
    temp=[]
    i=0
    pula=0
    pronto=False
    while parentesis_achado:
        parentesis_achado=False
        while i < len(lista):
            if lista[i] in ('(',')'):
                if lista[i]=='(':
                    pula+=1
                    if parentesis_aberto:
                        temp.append(lista[i])
                    else:
                        parentesis_aberto=True
                else:
                    pula-=1
                    if pula==0:
                        parentesis_aberto=False
                        resultado_temp=str(traz_resultado(temp))
                        temp=[]
                        for j in range(len(resultado_temp)):
                            lista.insert(i+1+j,resultado_temp[j])
                    else:
                        temp.append(lista[i])
                del lista[i]
                i-=1
            elif parentesis_aberto==True:
                temp.append(lista[i])
                del lista[i]
                i-=1
            i+=1
            
    return lista


#__main__
clear_screen()
operadores=('+', '-', '*', '/')
nao_numeros=(operadores, '(', ')')
while(True):
    try:
        
        digitos=[]
        operacoes=[]
        entrada=[]
        entrada=str(input('Insira a conta a ser realizada (suporta decimais, negativos, operações [+, -, *, /] e parentesis):\n'))
        if entrada=='':
            clear_screen()
            continue
        entrada=list(entrada.replace(' ',''))
        limpa_virgula(entrada)
        limpa_zero_esquerda(entrada)
        resultado=traz_resultado(entrada)
        print('Resultado:',resultado)
        if repetir():
            continue
        else:
            break
    except ZeroDivisionError:
        if repetir('Não é possível dividir por 0!'):
            continue
        else:
            break
    except KeyboardInterrupt:
        break
    except:
        if repetir('Entrada Inválida'):
            continue
        else:
            break
print ('Obrigado!')
