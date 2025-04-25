# Entrada: quantidade de sanduíches
quantidade = int(input("Digite a quantidade de sanduíches a fazer: "))

# Cálculos em gramas
queijo_gramas = quantidade * 2 * 50
presunto_gramas = quantidade * 50
carne_gramas = quantidade * 100

# Conversão para quilos
queijo_quilos = queijo_gramas / 1000
presunto_quilos = presunto_gramas / 1000
carne_quilos = carne_gramas / 1000

# Saída dos resultados
print("Queijo (kg):", queijo_quilos)
print("Presunto (kg):", presunto_quilos)
print("Carne (kg):", carne_quilos)
