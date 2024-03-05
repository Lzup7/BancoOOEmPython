from banco import Banco

banco = Banco("banco.db")
while True:
  print("""
  1 - CRIAR CONTA
  2 - CONSULTAR SALDO
  3 - DEPOSITAR
  4 - SACAR
  0 - SAIR
  """)
  opcao = int(input("DIGITE A OPCÂO: "))
  if opcao == 1:
    nome = str(input("Informe o nome: "))
    saldo = float(input("Informe o saldo: "))
    id_conta = banco.criar_conta(nome, saldo)
    print(f"Conta criada com sucesso:\nNumero da sua conta é : {id_conta}")
  if opcao == 2:
    id_conta = input("Selecione seu Id: ")
    conta = banco.buscar_conta(id_conta)
    if conta:
      print(f"Saldo da conta {conta.titular}: R$ {conta.saldo}")
    else:
      print(f"Conta não encontrada")
  if opcao == 3:
    id_conta = input("Selecione seu Id: ")
    valor = float(input("Informe o valor do deposito: "))
    banco.depositar(id_conta, valor)
    print("Deposito realizado co sucesso!")
  if opcao == 4:
    id_conta = input("Selecione seu Id: ")
    valor = float(input("Informe o valor do saque: "))
    banco.sacar(id_conta, valor)
    print("Saque realizado co sucesso!")
  if opcao == 0:
    print("PROGAMA ENCERRADO")
    break
