## QUESTÃO 1 ##
#
# Um site exige que os usuários insiram nome de usuário e senha para se registrarem. 
# Escreva um programa para verificar se a senha digitada pelos usuários é forte o suficiente.
# A seguir estão os critérios para verificar a senha:
#
# 1. Pelo menos uma letra entre [a-z]
# 2. Pelo menos 1 número entre [0-9]
# 3. Pelo menos uma letra entre [A-Z]
# 4. Pelo menos 1 caractere de [$ # @]
# 5. Comprimento mínimo da senha: 6
# 6. Comprimento máximo da senha: 12
#
# Seu programa deve aceitar uma sequência de senhas separadas por vírgula e as verificará 
# de acordo com os critérios acima. As senhas que correspondem aos critérios devem ser 
# impressas, separadas por uma vírgula.
# Exemplo
# Se as seguintes senhas forem fornecidas como entrada para o programa:
# ABd1234@1, umF1#, 2w3E*, 2We3345
# Então, a saída do programa deve ser:
# ABd1234@1
##

##
# A sua resposta da questão deve ser desenvolvida dentro da função main()!!! 
# Deve-se substituir o comado print existente pelo código da solução.
# Para a correta execução do programa, a estrutura atual deve ser mantida,
# substituindo apenas o comando print(questão...) existente.
##
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
