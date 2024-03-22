cont = 0
somatot = 0

somaN = int(input("Quantos números você quer somar?"))
while cont < somaN:
    num = float(input("Digite um número: "))
    if num < 10:
        print("Números menores que dez são invalidos!!!")
    else:
        somatot = num + somatot
        cont += 1

print("a soma de todos os numeros é: {} ".format(somatot))