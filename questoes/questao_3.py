## QUESTÃO 3 ##
#
# Crie uma implementação da cifra rotacional, às vezes também chamada de cifra de César.
# 
# A cifra de César é uma simples cifra de deslocamento que se baseia na transposição 
# de todas as letras do alfabeto usando uma chave inteira entre 0 e 26. 
# O uso da chave 0 ou 26 sempre produzirá a mesma saída devido à aritmética modular. 
# A letra é deslocada para tantos valores quanto o valor da chave.
#
# A notação geral para cifras rotacionais é ROT + <chave>. A cifra rotacional mais comumente usada é a ROT13.
#
# Um ROT13 no alfabeto latino seria o seguinte:
# 	Normal:  abcdefghijklmnopqrstuvwxyz
#	Cifrado: nopqrstuvwxyzabcdefghijklm
#
# Exemplos:
#	Entrada: ROT5 omg 
#          Saída: trl
#	Entrada: ROT0 c 
#          Saída: c
#	Entrada: ROT26 Cool 
#          Saída: Cool
#	Entrada: ROT13 The quick brown fox jumps over the lazy dog. 
#          Saída: Gur dhvpx oebja sbk whzcf bire gur ynml qbt.
#	Entrada: ROT13 Gur dhvpx oebja sbk whzcf bire gur ynml qbt. 
#          Saída: The quick brown fox jumps over the lazy dog.
#
# Se um valor de entrada inválido for digitado, a seguinte mensagem 
# deve ser impressa: 'Erro'. 
# Entradas inválidas podem ser entradas que contém códigos de rotações 
# inválidos ou mensagens contendo caracteres que não estão no alfabeto. 
# Exemplos:
# 	Entrada: RARA abc Saída: Erro
# 	Entrada: ROT5 c99 Saída: Erro
#
# As entradas devem ser sempre compostas por ROT + <chave> + ' ' + 'mensagem', 
# ou seja, a cifra rotacional e a mensagem a ser cifrada separados por vírgula.
##


##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
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
