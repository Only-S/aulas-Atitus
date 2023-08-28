def indicadores(tabela):
    
    municipio_v = {}
    municipio_nv = {}
    for linha in tabela:
        leitor = dict(linha, delimiter=';')        
        for coluna in leitor:
            indicador_violento = 0
            indicador_nao_violento = 0
            municipio = linha['Municipios']  
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
            if municipio in municipio_v:
                municipio_v[municipio] += indicador_violento
            else:
                municipio_v[municipio] = indicador_violento

            if municipio in municipio_nv:
                municipio_nv[municipio] += indicador_nao_violento
            else:
                municipio_nv[municipio] = indicador_nao_violento

    return municipio_v, municipio_nv
        