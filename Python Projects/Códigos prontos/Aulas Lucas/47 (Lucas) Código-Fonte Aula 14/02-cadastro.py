def cadastro(nome, idade, profissao, status = "ativo"):
    print(f"Nome     : {nome}")
    print(f"Idade    : {idade}")
    print(f"Profissão: {profissao}")
    print(f"Status   : {status}")

## Programa Principal
nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
prof = input("Digite sua profissão: ")
st = input("Digite o status (opcional): ")

if st: # testa se s é uma string não vazia
    cadastro(nome, idade, prof, st)
else:
    cadastro(nome, idade, prof)
