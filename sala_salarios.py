
print("Olá funcionário, por favor digite no campo abaixo o seu salário para saber o reajuste.")
salario = float(input("Digite aqui o seu salário: R$"))

if(salario <= 280):
    salario_final = (salario * 0.20) + salario
    reajuste = (salario * 0.20)
    print("Houve um reajuste de + R${}    .logo, o salário final será de {}".format(reajuste, salario_final))
else:
    if(700 <= salario > 280):
        salario_final = (salario * 0.15) + salario
        reajuste = (salario * 0.15)
        print("Houve um reajuste de + R${}    .logo, o salário final será de {}".format(reajuste, salario_final))

    elif(1500 <= salario > 700):
        salario_final = (salario * 0.10) + salario
        reajuste = (salario * 0.10)
        print("Houve um reajuste de + R${}  .logo, o salário final será de {}".format(reajuste, salario_final))

    if (salario > 1500):
        salario_final = (salario * 0.05) + salario
        reajuste = (salario * 0.05)
        print("Houve um reajuste de + R${}    .logo, o salário final será de {}".format(reajuste, salario_final))