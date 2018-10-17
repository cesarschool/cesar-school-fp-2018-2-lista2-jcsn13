def main():
	ano = int(input("Insira o ano: "))
	mes = int(input("Insira o mes: "))
	dia = int(input("Insira o dia: "))
	anoN = ano
	mesN = mes
	diaN = dia
	bi = False

	if dia < 1 or dia > 31 or mes < 1 or mes > 12:
		print("Mes ou dia invalidos!")

	else:

		if ano % 4 == 0 and (ano % 100 != 0 or ano % 400 == 0):
			bi = True

		if bi == False:
			
			if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
				if dia == 31:
					diaN = 1
					mesN+=1
				else:
					diaN = dia+1

			if mes == 2:
				if dia == 28:
					diaN = 1
					mesN+=1
				else:
					diaN = dia+1

			if mes == 4 or mes == 6 or mes == 9 or mes == 11:
				if dia == 30:
					diaN = 1
					mesN+=1
				else:
					diaN = dia+1

			if mesN == 13:
				anoN+= 1
				diaN = 1
				mesN = 1

			if(mesN == 1 or mesN< 10):
				if diaN == 1 or diaN<10:
					print(str(anoN)+"-0"+str(mesN)+"-0"+str(diaN))
				else:
					print(str(anoN)+"-0"+str(mesN)+"-"+str(diaN))
			else:
				if diaN == 1 or diaN<10:
					print(str(anoN)+"-"+str(mesN)+"-0"+str(diaN))
				else:
					print(str(anoN)+"-"+str(mesN)+"-"+str(diaN))

		if bi == True:
			if(dia>29):
				print("Fevereiro não tem esse dia!")
			else:
				if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
					if dia == 31:
						diaN = 1
						mesN+=1
					else:
						diaN = dia+1

				if mes == 2:
					if dia == 29:
						diaN = 1
						mesN+=1
					else:
						diaN = dia+1

				if mes == 4 or mes == 6 or mes == 9 or mes == 11:
					if dia == 30:
						diaN = 1
						mesN+=1
					else:
						diaN = dia+1

				if mesN == 13:
					anoN+= 1
					diaN = 1
					mesN = 1

				if(mesN == 1 or mesN< 10):
					if diaN == 1 or diaN<10:
						print(str(anoN)+"-0"+str(mesN)+"-0"+str(diaN))
					else:
						print(str(anoN)+"-0"+str(mesN)+"-"+str(diaN))
				else:
					if diaN == 1 or diaN<10:
						print(str(anoN)+"-"+str(mesN)+"-0"+str(diaN))
					else:
						print(str(anoN)+"-"+str(mesN)+"-"+str(diaN))
if __name__ == '__main__':
    main()
