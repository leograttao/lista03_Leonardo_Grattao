cont = 0
somaImp = 0
totImp = 0
somaPar = 0
while cont < 5 and somaImp < 30:

    num = int(input("Digite um número inteiro:"))
    if num < 0:
        print("esse número é invalido")
    elif num % 2 == 0:
        print("O número {} é par".format(num))
        cont += 1
        somaPar = num + somaPar
    elif num % 2 == 1:
        print("O número {} é ímpar".format(num))
        somaImp = num + somaImp
        totImp += 1
print("A soma dos números ímpares é {}".format(somaImp))
print("O total de números ímpares digitados é: {}".format(totImp))
print("A soma dos números pares é: {}".format(somaPar))