def indicadores(tabela):
    indicador_violento = 0
    indicador_nao_violento = 0
    for linha in tabela:
        for coluna in linha:
            if coluna == 'Municipios':
                pass
            elif linha[coluna] == '0':
                pass
            else:
                match coluna:
                    case  'Vitimas de Homicidio Doloso' | 'Vitimas de Latrocinio' | 'Vitimas de Lesao Corp Seg Morte':
                        indicador_violento += int(linha[coluna]) * 10
                    case  ' Roubos' | ' Delitos Relacionados a Armas e Municoes':
                        indicador_violento += int(linha[coluna]) * 2
                    case ' Roubo de Veiculo':
                        indicador_violento += int(linha[coluna]) * 3
                    case ' Entorpecentes Trafico':
                        indicador_violento += int(linha[coluna]) * 5
                    case ' Furtos' | 'Furto de Veiculo ':
                        indicador_nao_violento += int(linha[coluna]) * 3
                    case ' Estelionato':
                        indicador_nao_violento += int(linha[coluna]) * 1
                    case ' Entorpecentes Posse':
                        indicador_nao_violento += int(linha[coluna]) * 2
                    case _:
                        pass
    return indicador_violento, indicador_nao_violento