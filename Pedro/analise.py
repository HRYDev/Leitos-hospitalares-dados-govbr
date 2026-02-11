import os, json
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

def DumpToFile(path, input): # Para Debug
    output = open(path, 'w', encoding='UTF-8')
    output.write(input.to_string(index=True, header=True))
    output.close()

ano = 2025
filters = [
    'RAZAO_SOCIAL', 'CO_CEP', 'CNES', 'NU_ENDERECO', 'NO_EMAIL', 'TP_GESTAO',
    'DESC_NATUREZA_JURIDICA', 'COMP', 'MOTIVO_DESABILITACAO', 'DS_TIPO_UNIDADE', 'NATUREZA_JURIDICA',
    'CO_TIPO_UNIDADE', 'NU_TELEFONE', 'NO_COMPLEMENTO', 'NO_LOGRADOURO', 'NO_BAIRRO'
]
targets = [
    'NOME_ESTABELECIMENTO', 'REGIAO', 'UF', 'MUNICIPIO',
    'LEITOS_EXISTENTE', 'LEITOS_SUS',
    'UTI_TOTAL_EXIST', 'UTI_TOTAL_SUS',
    'UTI_ADULTO_EXIST', 'UTI_ADULTO_SUS',
    'UTI_PEDIATRICO_EXIST', 'UTI_PEDIATRICO_SUS',
    'UTI_NEONATAL_EXIST', 'UTI_NEONATAL_SUS',
    'UTI_CORONARIANA_EXIST', 'UTI_CORONARIANA_SUS',
    'UTI_QUEIMADO_EXIST', 'UTI_QUEIMADO_SUS'
]

def CarregarDados(_ano):
    global ano, table, north, northeast, center , southeast, south
    ano = _ano

    print("Carregando dados...")
    work_dir = os.path.dirname(os.path.realpath(__file__))
    raw_data = open(os.path.join(work_dir, f'dados/Leitos_{ano}.json'), 'r').read()
    data = json.loads(raw_data)

    if ano == 2024:
        data = data['data']

    table = pd.DataFrame.from_dict(data)
    table.columns = table.columns.str.replace('_-_', '_')
    table.columns = table.columns.str.replace('EXISTENTES', 'EXISTENTE')
    table.drop(columns=filters, inplace=True)
    table = table[targets]

    north = table[table['REGIAO'] == 'NORTE']
    northeast = table[table['REGIAO'] == 'NORDESTE']
    center = table[table['REGIAO'] == 'CENTRO-OESTE']
    southeast = table[table['REGIAO'] == 'SUDESTE']
    south = table[table['REGIAO'] == 'SUL']

def Conclusão(index):
    output = ''
    match (index):
        case 1:
            highlight = (pd.to_numeric(north['UTI_TOTAL_EXIST']) + pd.to_numeric(north['UTI_TOTAL_SUS'])).idxmax()
            output = north.loc[highlight, targets[0]] + ' - ' + north.loc[highlight, targets[6]] + ' UTIs Regulares ' + north.loc[highlight, targets[7]] + ' UTIs SUS'
        case 2:
            sorted_table = center.sort_values('LEITOS_SUS', ascending=False)
            output = sorted_table.iat[0, 0] + ' - ' + sorted_table.iat[0, 5] + ' Leitos SUS'
        case 3:
            sorted_table = northeast.sort_values('LEITOS_EXISTENTE', ascending=False)
            output = sorted_table.iat[0, 0] + ' - ' + sorted_table.iat[0, 4] + ' Leitos Regulares'
        case 4:
            highlight = (pd.to_numeric(table['LEITOS_EXISTENTE']) - pd.to_numeric(table['LEITOS_SUS'])).abs().idxmax()
            output = table.loc[highlight, targets[0]] + ' - ' + table.loc[highlight, targets[4]] + ' Leitos Regulares ' + table.loc[highlight, targets[5]] + ' Leitos SUS'
        case 5:
            highlight = (pd.to_numeric(table['LEITOS_EXISTENTE']) + pd.to_numeric(table['LEITOS_SUS'])).idxmax()
            output = table.loc[highlight, targets[0]] + ' - ' + table.loc[highlight, targets[4]] + ' Leitos Regulares ' + table.loc[highlight, targets[5]] + ' Leitos SUS'
    return output + '\n'

def Grafico_LeitosPorRegião():
    fig, ax = plt.subplots(layout='constrained')
    leitos_regulares = np.divide([
        pd.to_numeric(north[targets[4]]).sum(),
        pd.to_numeric(northeast[targets[4]]).sum(),
        pd.to_numeric(center[targets[4]]).sum(),
        pd.to_numeric(southeast[targets[4]]).sum(),
        pd.to_numeric(south[targets[4]]).sum()], 1000)
    leitos_sus = np.divide([
        pd.to_numeric(north[targets[5]]).sum(),
        pd.to_numeric(northeast[targets[5]]).sum(),
        pd.to_numeric(center[targets[5]]).sum(),
        pd.to_numeric(southeast[targets[5]]).sum(),
        pd.to_numeric(south[targets[5]]).sum()], 1000)

    left_bars = ax.bar(np.arange(0.875, 5.875, 1), leitos_regulares, 0.25, label='Leitos Regulares', color='brown')
    right_bars = ax.bar(np.arange(1.125, 6.125, 1), leitos_sus, 0.25, label='Leitos SUS', color='cornflowerblue')

    ax.bar_label(left_bars, fmt='{:.0f}k', padding=2)
    ax.bar_label(right_bars, fmt='{:.0f}k', padding=2)

    ax.set_title(f'Relação Entre Leitos Regulares e Leitos SUS por Região ({ano})')
    ax.set_xticks(range(1, 6), ['Norte', 'Nordeste', 'Centro-Oeste', 'Sudeste', 'Sul'])
    ax.set_ylabel('N° de Leitos (Mil)')
    ax.legend()
    fig.savefig(f'Relação entre Leitos ({ano})')
    plt.show()

def Grafico_DistribuiçãoUTIs():
    fig, ax = plt.subplots()
    recursos = [0] * 5; nomes = [''] * 5
    for i in range(6, 18, 2):
        recursos[0] += pd.to_numeric(north[targets[i]]).sum(); nomes[0] = 'UTIs na região Norte'
        recursos[1] += pd.to_numeric(northeast[targets[i]]).sum(); nomes[1] = 'UTIs na região Nordeste'
        recursos[2] += pd.to_numeric(center[targets[i]]).sum(); nomes[2] = 'UTIs na região Centro-Oeste'
        recursos[3] += pd.to_numeric(south[targets[i]]).sum(); nomes[3] = 'UTIs na região Sul'
        recursos[4] += pd.to_numeric(southeast[targets[i]]).sum(); nomes[4] = 'UTIs na região Sudeste'

    ax.pie(recursos, labels=nomes, autopct='%.1f%%')
    ax.set_title(f'Disparidade da Quantidade de UTIs entre as regiões ({ano})')
    plt.savefig(f"Disparidade UTIs ({ano})")
    plt.show()