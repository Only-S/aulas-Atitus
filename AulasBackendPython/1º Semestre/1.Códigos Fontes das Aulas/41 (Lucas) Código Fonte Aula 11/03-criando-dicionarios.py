# Dicionário Vazio
dic = {}

# Dicionário com dados
glossario = {"algoritmo": "maneira chique de falar passo a passo",
             "bug": "problema no código do programa",
             "estrutura de dados": "coleção de dados organizados",
             "indentação": "recuos usados para organizar código",
             "variável": "rótulo que referencia um valor"}

turma = {1756: 9.5, 2025: 7.4, 2094: 7.2, 2132: 5.9, 1822: 7.6}

print(glossario["bug"])

media = (turma[1756] + turma[2132] + turma[2094]) / 3
print(media)

#print(turma["1756"])   # Produz erro!

# Adicionando novo valor ao dicionário
glossario["exceção"] = "erro na execução do programa"
print(glossario)

# Modificando valor já existente
turma[1756] = 10.0 

# Remoção de uma palavra do glossário
del glossario["bug"]
print(glossario)

# Remoção com pop
nota = turma.pop(1756)
print(nota)

# Iterando sobre dicionários
for chave in glossario:
    print(f"{chave} -> {glossario[chave]}")