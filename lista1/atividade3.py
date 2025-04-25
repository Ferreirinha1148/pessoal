# Entrada de dados
horas_normais = float(input("Digite o número de horas normais trabalhadas: "))
horas_extras = float(input("Digite o número de horas extras trabalhadas: "))

# Cálculo do salário bruto
salario_bruto = (horas_normais * 10) + (horas_extras * 15)

# Cálculo do salário líquido (desconto de 10%)
salario_liquido = salario_bruto * 0.90

# Saída dos resultados
print("Salário bruto: R$", salario_bruto)
print("Salário líquido: R$", salario_liquido)

