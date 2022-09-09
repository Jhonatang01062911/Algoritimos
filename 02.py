#Digit senha.
senha = str(input('Insira a senha: '))
#Senha CORRETA.
senha_correta = 'Senha123@'
#Se a senha for inserida e estiver correta esta LOGADO se não: esta Negado.
if senha == senha_correta:
    print('Você está logado')
else:
    print('Senha incorreta')