import textwrap
def menu():
   menu = """
   ======================= MENU =======================

    [d]\t Depositar
    [s]\t Sacar
    [e]\t Extrato
    [nc]\t Nova conta
    [lc]\t Listar contas
    [nu]\t Novo usuário
    [q]\t Sair

    ===================================================

    => """
   return input(textwrap.dedent(menu))

def depositar(saldo, valor, extrato, /):
  if valor > 0:
      saldo += valor
      extrato += f"Depósito:\t R$ {valor:.2f}\n"
      print("\n====Depósito realizado com sucesso!====")
  else:
      print("\n ------------Operação falhou! Valor inválido")
  return saldo, extrato
   
def sacar(*, saldo, valor, extrato, limite, numero_saques, LIMITE_SAQUES):
  excedeu_saldo = valor > saldo
  excedeu_limite = valor > limite
  excedeu_saques = numero_saques >= LIMITE_SAQUES

  if excedeu_saldo: 
    print("Operação falhou")

  elif excedeu_limite:
    print("Operação falhou")
  
  elif excedeu_saques:
     print("Operação falhou")

  elif valor > 0:
     saldo -= valor
     extrato += f"Saque:\t\tR$ {valor:.2f}\n"
     numero_saques += 1
     print("\n====Saque realizado com sucesso====")

  else:
     print("\n -------- Operação falhou! Valor inválido --------")

  return saldo, extrato 

def exibir_extrato(saldo, /, *, extrato): #argumento posicional: saldo; Argumento nomeado: extrato
  print("\n=================== EXTRATO ===================")
  print("Não foram realizadas movimentações." if not extrato else extrato)
  print(f"\nSaldo:\t\tR$ {saldo:.2f}")
  print("\n===============================================")

def criar_usuario(usuarios):
  cpf = input ("Informe o CPF (somente números): ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("Já existe usuário com esse CPF! ")
    return

  nome = input("Informe o nome completo: ")
  data_nascimento = input("Informe a data de nascimento: ")
  endereco = input("Informe o endereço: ")

  usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})

  print("============== Usuário criado com sucesso ==============")

def filtrar_usuario(cpf, usuarios):
   usuarios_filtrados = [usuario for usuario in usuarios if usuario["cpf"] == cpf]
   return usuarios_filtrados[0] if usuarios_filtrados else None
   
def criar_conta(agencia, numero_conta, usuarios):
  cpf = input("Informe o CPF do usuário: ")
  usuario = filtrar_usuario(cpf, usuarios)

  if usuario:
    print("\n========== Conta criada com sucesso! ==========")
    return {"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario}
  
  print("\n---------Usuário não encontrado, fluco de criação de conta encerrado! ---------")
  
def listar_contas(contas):
  for conta in contas:
    linha = f"""\
          Agência:\t{conta['agencia']}
          C/C:\t\t{conta['numero_conta']}
          Titular:\t{conta['usuario']['nome']}
          """
    print("=" * 100)
    print(textwrap.dedent(linha))

def main():
  LIMITE_SAQUES = 3
  AGENCIA = "0001"

  saldo = 0
  limite = 500
  extrato = ""
  numero_saques = 0
  usuarios = []
  contas = []

  while True:
    opcao = menu() #entrada do usuário para a opção desejada

    if opcao == "d":
        valor = float(input("Informe o valor do depósito: R$ "))

        saldo, extrato = depositar(saldo, valor, extrato)

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n" #atribuição de valor a extrato
            operacao_realizada = True
        
        else:
            print("Operação falhou! O valor informado é inválido.") #caso o valor seja menor ou igual a zero
          
    elif opcao == "s": 
      
      if numero_saques < LIMITE_SAQUES:
          sacar = float(input("Informe o valor do saque: ")) 
          
          if sacar > saldo:
                  print("Você não tem saldo suficiente para realizar essa operação.")
            
          elif sacar > 0 and sacar <= limite:
                extrato += f"Saque: R$ {sacar:.2f}\n"
                saldo -= sacar
                numero_saques += 1
                operacao_realizada = True
                
          else:
              print("Operação falhou! O valor informado é inválido.")
      else:
        print("Limite de saques diários excedido. Tente novamente amanhã.")
        
    elif opcao == "e":
      exibir_extrato(saldo, extrato=extrato)
      #if operacao_realizada:
        ###print(f"""\n      =================Extrato=================      \n
          #  Essas foram as movimentações:\n\n{extrato}\n
          #  Saldo final: R$ {saldo:.2f}

          #  Obrigado por usar nossos serviços!""") #usando o format para inserir de maneira mais fácil os valores de saldo e extrato 

      #else:
      #  print("\nNenhuma operação realizada anteriormente.")

    elif opcao == "nu":
      criar_usuario(usuarios)

    elif opcao == "nc":
      numero_conta = len(contas) + 1
      conta = criar_conta(AGENCIA, numero_conta, usuarios)

      if conta:
         contas.append(conta)
    
    elif opcao == "lc":
      listar_contas(contas)

    elif opcao == "q":
      print("Obrigado por usar nossos serviços")
      break

    else:
      print("Operação inválida. Por favor, escolha uma das opções do menu.")

  
main()