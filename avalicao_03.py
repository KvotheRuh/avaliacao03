# Aluno: Carlos Eduardo Nogueira Morciani
# Curso: Ciência da Computação

# ================================================================================================

# 1.Escreva um algoritmo recursivo para cada uma das alternativas (2,25).


# a)S(1) = 10
#   S(n) = S(n – 1) + 10,  para n >= 2
def S(n):
    if n == 1:
        return 10

    else:
        return S(n - 1) + 10

print('Questão número 1 letra A')
print(S(1))
print(S(2))
print(S(3))
print(S(4))
print(S(5))
print("\n")



# b)A(1) = 2
#   A(n) = A(n – 1)^-1 ,  para n >= 2


def A(n):
    if n == 1:
        return 2

    else:
        return A(n - 1)**-1

print('Questão número 1 letra B')
print(A(1))
print(A(2))
print(A(3))
print(A(4))
print(A(5))
print("\n")


# c)B(1) = 1
#   B(n) = B(n – 1) + n^2,  para n >= 2


def B(n):
    if n == 1:
        return 1

    else:
        return B(n - 1) + n**2

print('Questão número 1 letra C')
print(B(1))
print(B(2))
print(B(3))
print(B(4))
print(B(5))
print("\n")


# d)P(1) = 1
#   P(n) = n^2*P(n – 1) + n - 1,  para n >= 2


def P(n):
    if n == 1:
        return 1

    else:
        return (n**2) * P(n - 1) + n - 1

print('Questão número 1 letra D')
print(P(1))
print(P(2))
print(P(3))
print(P(4))
print(P(5))
print("\n")


# e)D(1) = 3
#   D(2) = 5
#   D(n) = (n – 1)*D(n – 1) + (n – 2)*D(n – 2), para n > 2


def D(n):
    if n == 1:
        return 3

    elif n == 2:
        return 5

    else:
        return (n - 1) * D(n - 1) + (n - 2) * D(n - 2)

print('Questão número 1 letra E')
print(D(1))
print(D(2))
print(D(3))
print(D(4))
print(D(5))
print("\n")


# f)W(1) = 2
#   W(2) = 5
#   W(n) = W(n – 1)*W(n – 2), para n > 2


def W(n):
    if n == 1:
        return 2

    elif n == 2:
        return 5

    else:
        return W(n - 1) * W(n - 2)

print('Questão número 1 letra F')
print(W(1))
print(W(2))
print(W(3))
print(W(4))
print(W(5))
print("\n")


# g)T(1) = 1
#   T(2) = 2
#   T(3) = 3
#   T(n) = T(n – 1) + 2*T(n – 2) + 3*T(n – 3),   para n > 3


def T(n):
    if n == 1:
        return 1

    elif n == 2:
        return 2

    elif n == 3:
        return 3

    else:
        return T(n - 1) + 2 * T(n - 2) + 3 * T(n - 3)

print('Questão número 1 letra G')
print(T(1))
print(T(2))
print(T(3))
print(T(4))
print(T(5))
print(50*"-")
print("\n")


# ================================================================================================

# 2.Escreva uma definição recursiva para uma progressão geométrica com termo inicial a e razão r. (0,75)


def PG(numero, t_inicial, razao):
    if numero == 1:
        return t_inicial

    else:
        return PG(numero - 1, t_inicial, razao) * razao

print('Questão número 2')
print(PG(1,1,1))
print(PG(2,2,2))
print(PG(3,3,3))
print(PG(4,4,4))
print(50*"-")
print("\n")


# ================================================================================================

# 3.Uma coleção T de números é definida recursivamente por:
#   2 pertence a T
#   Se X pertence a T, então 	X+3 pertence a T 	e 	2*X pertence a T

#   Quais dos seguintes números pertencem a T? 6 , 7 , 19 , 12.
#   Faça um programa recursivo para demonstrar. (0,5)

'''
Obs: Caso o número pertença a T, o programa retorna True, caso contrário, retorna False.
'''

def T_3(x):
    if x == 2:
        return True

    elif x < 2:
        return False

    elif T_3(x - 3) or T_3(x - 1) % 2 == 0:
        return True

    else:
        return False

print('Questão número 3')
print(T_3(6))
print(T_3(7))
print(T_3(19))
print(T_3(12))
print(50*"-")
print("\n")


# ================================================================================================

# 8.Escreva o corpo da função recursiva para computar S(n) para uma dada sequência S(1 ponto):
# a)1 , 3 , 9 , 27 , ...


def A_8(n):
    if n == 0:
        return 1
    else:
        return 3 * A_8(n - 1)

print('Questão número 08 letra A')
print(A_8(0))
print(A_8(1))
print(A_8(2))
print(A_8(3))
print("\n")


# b)2 , 1 ,1/2,1/4, ...


def B_8(n):
    if n == 0:
        return 1

    elif n > 0:
        return 2**n * B_8(n - 1)

    else:
        return B_8(n + 1) / 2

print('Questão número 08 letra B')
print(B_8(1))
print(B_8(0))
print(B_8(-1))
print(B_8(-2))
print(B_8(-3))
print(50*"-")
print("\n")


# ================================================================================================

# 9.Membros antigos da Sociedade de Pitágoras definiram números figurados como sendo o número de pontos em uma certa configuração geométrica. Os primeiros números triangulares são 1, 3, 6 e 10, e são semelhantes ao diagrama da figura abaixo:

# Encontre a fórmula para o n-ésimo número triangular e escreva um programa recursivo.(0,5)
'''
A formúla que define os números triangulares e T= (n*(n + 1))/2
'''


def T_9(n):
    if n == 1:
        return 1
    else:
        return n + T_9(n - 1)

print('Questão número 09')
print(T_9(1))
print(T_9(2))
print(T_9(3))
print(T_9(4))
print(T_9(5))
print(T_9(6))
print(50*"-")
print("\n")


# ================================================================================================

# 10.Em um experimento, certa colônia de bactérias tem inicialmente uma população igual a 50.000. Uma leitura é feita a cada hora e, no final deste intervalo, há três vezes mais bactérias que antes.

# (a) Escreva a definição recursiva para A(n), o número de bactérias presentes no início do n-ésimo período de tempo. (0,25)


def A_10(n):
    if n == 0:
        return 50000
    else:
        return A_10(n - 1) * 3


print('Questão número 10')
print(A_10(0))
print(A_10(1))
print(A_10(2))
print(A_10(3))
print(A_10(7))

# (b) Em quantas leituras a população excederá 153.450.026 bactérias?(0,25)
'''
RESPOSTA: Utilizando a definição recursiva da letra A da questao 10, podemos chegar a conclusão que a população de bactérias exederá
153.450.026 após 8 leituras onde o valor chegará a 328.050.000.
'''

print(f'Verificação da letra b: {A_10(8)}, dessa forma percebemos que após 8 verificações o número de bactérias e superior a 153.450.026')