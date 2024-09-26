#Escreva um programa que leia o número de um funcionário, seu número de horas trabalhadas, o valor que recebe por hora e calcula o salário desse funcionário. A seguir, mostre o número e o salário do funcionário, com duas casas decimais.#

F=int(input())
H=int(input())
VH=int(input())

SALARIO= H * VH

print(f'NUMBER= {F}')
print(f'SALARY= U${SALARIO:.2f}')


F = int(input("Digite o número do funcionário: "))
H = int(input("Digite o número de horas trabalhadas: "))
VH = int(input("Digite o valor recebido por hora: "))


SALARIO = H * VH


print(f'NUMBER= {F}')
print(f'SALARY= U${SALARIO:.2f}')



