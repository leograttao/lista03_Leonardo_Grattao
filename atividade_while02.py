soma = 0 
cont = 0 
while cont < 10:
    nota = float(input(f"digite uma nota: "))
    soma += nota 
    cont += 1 

media = soma / cont 
print(f"sua media foi {media}")