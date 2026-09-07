nome_do_objeto = input("Qual nome do aparelho?")
Potencia  = int(input("Qual a potencia do aparelho?"))
Tempo = int(input("Por quantas horas o aparelho ficará ligado por dia?"))
Consumomensal = (Potencia * Tempo * 30) / 1000
Preço = float(Consumomensal * 0.75)
print(f"aparelho:{nome_do_objeto}.")
print(f"consumo de:{Consumomensal} kwh")
print(f"Considerando o preço minimo do kwh em 0,75, o preço do seu aparelho será de ${Preço}")
