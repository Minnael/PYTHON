print("DIGITE A QUANTIDADE DE LINHAS:", end=" ")
LINHA = int(input())
print("DIGITE A QUANTIDADE DE COLUNAS:", end=" ")
COLUNA = int(input())

DIMENSAO = LINHA * COLUNA

MATRIZ_A = []
MATRIZ_B = []
MATRIZ_SOMA = []

for i in range(0, DIMENSAO):
	MATRIZ_A.append([])
	MATRIZ_B.append([])

print("PREENCHA A MATRIZ A:")
for i in range(0, DIMENSAO):
	NUMERO = int(input())
	MATRIZ_A[i].append(NUMERO)

print("PREENCHA A MATRIZ B:")
for i in range(0, DIMENSAO):
	NUMERO = int(input())
	MATRIZ_B[i].append(NUMERO)

print("SOMANDO...")
for i in range(0, DIMENSAO):
	MATRIZ_SOMA.append(MATRIZ_A[i][0] + MATRIZ_B[i][0])

cont = 1
print("[", end="")
for i in range(0, DIMENSAO):
	print(MATRIZ_SOMA[i], end=" ")
	if (cont==LINHA):
		print("]")
		if (i<DIMENSAO-1):
			print("[", end="")
		cont = 0
	cont = cont + 1




