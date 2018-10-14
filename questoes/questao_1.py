def main():
	op = True
	senhas = ""
	while op != False:
		senha = input("Insira a sua senha: ")
		for senha in senha.split(","):
			confirm = 0
			
			if len(senha)>=6 and len(senha)<= 12:
				confirm+=1

			for letra in senha:
				if letra == '@' or letra == '#' or letra == '$':
					confirm+=1

			for numero in senha:
				if numero.isdigit() == True:
					confirm+=1
					break
			
			for letra in senha:
				if letra.isalpha() == True and letra.islower() == True:
					confirm+=1
					break

			for letra in senha:
				if letra.isalpha() == True and letra.isupper() == True:
					confirm+=1
					break

			if confirm == 5:
				senhas+= str(senha)+','
		print(senhas[:-1])		
		op = input("Deseja continuar?(s/n)").lower()

		if op == 's':
			op == True
		else:
			break
if __name__ == '__main__':
    main()
