print("DIGITE A QUANTIDADE DE LINHAS:", end=" ")
LINHA = int(input())
print("DIGITE A QUANTIDADE DE COLUNAS:", end=" ")
COLUNA = int(input())

DIMENSAO = LINHA * COLUNA

MATRIZ_A = []
MATRIZ_B = []
MATRIZ_MULT = []

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
	
	
































