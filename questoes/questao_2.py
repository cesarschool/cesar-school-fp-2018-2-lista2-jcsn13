def main():
	
	dir = " "
	contadorV = 0
	contadorH = 0

	while dir != '':
		dir = input("Insira uma direção e quantidade de passos: ").lower() 
		
		if dir[:4]=="cima" and dir[4]== " ":
			print("Sua distancia foi adicionada")
			contadorV+=int(dir[5:])

		elif dir[:5]=="baixo" and dir[5]== " ":
			print("Sua distancia foi adicionada")
			contadorV-=int(dir[6:])


		elif dir[:8]=="esquerda" and dir[8]== " ":
			print("Sua distancia foi adicionada")
			contadorH+=int(dir[9:])

		elif dir[:7]=="direita" and dir[7]== " ":
			print("Sua distancia foi adicionada")
			contadorH-=int(dir[8:])
		
		elif dir == "":
			break

		else:
			print("Você inseriu um comando inválido!")

	distancia = (contadorV**2 + contadorH**2)**(1/2)
	print("O robo percorreu:",int(distancia),"em relação a seu ponto inicial")

if __name__ == '__main__':
    main()
