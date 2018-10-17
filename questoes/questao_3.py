def main():
	entrada = input("Insira sua ROT e a mensagem que deseja passar: ")
	alfabeto = "abcdefghijklmnopqrstuvwxyz"
	alfabetoM = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
	ROT = 0
	numeros = ""
	mensagemN = ""
	mensagemE = ""

	for u in entrada[5:]:
		if u.isdigit() == True:
			entrada = ""

	if entrada[0:3] != "ROT" or entrada[3].isdigit() == False:
		print("Erro")

	else:
		for num in entrada:
			if num.isdigit() == True:
				numeros+=num
		
		ROT = int(numeros)
		
		for men in entrada[3:]:
			if men.isalpha() == True:
				mensagemN+= men
			if men == " ":
				mensagemN+= men
				
		mensagemN = mensagemN.lstrip()
		
		for c in mensagemN:
			if c == " ":
				mensagemE+= c
			if c.isupper() == True:
				cin = alfabetoM.index(c)
				n = cin + ROT
				while n >= 26:
					n-= 26
				mensagemE+= alfabetoM[n]
				
			if c.islower() == True:
				cin = alfabeto.index(c)
				n = cin + ROT
				while n >= 26:
					n-= 26
				mensagemE+= alfabeto[n]


		if entrada[-1] == ".":
			mensagemE+= entrada[-1]

		print(mensagemE)
if __name__ == '__main__':
    main()
