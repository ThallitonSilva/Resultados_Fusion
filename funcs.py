import io
import pandas as pd


def ler_TM(table):
    tr = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=0)
    mt = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=1)

    map_tr = {'Occurences of enzymes/compounds': 'Occurences of Transcripts'}
    map_mt = {'Occurences of enzymes/compounds': 'Occurences of Metabolites'}

    tr.rename(columns=map_tr, inplace=True)
    mt.rename(columns=map_mt, inplace=True)

    j1 = pd.merge(left=tr, right=mt, on=['Pathway', 'Pathway id'], how='outer')
    j1.fillna(0, inplace=True)

    j1['Total'] = j1['Occurences of Transcripts'] + j1['Occurences of Metabolites']

    j1.sort_values('Total', ascending=False, inplace=True)

    return j1


def ler_PM(table):
    pr = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=0)
    mt = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=1)

    map_pr = {'Occurences of enzymes/compounds': 'Occurences of Proteins'}
    map_mt = {'Occurences of enzymes/compounds': 'Occurences of Metabolites'}

    pr.rename(columns=map_pr, inplace=True)
    mt.rename(columns=map_mt, inplace=True)

    j1 = pd.merge(left=pr, right=mt, on=['Pathway', 'Pathway id'], how='outer')
    j1.fillna(0, inplace=True)

    j1['Total'] = j1['Occurences of Proteins'] + j1['Occurences of Metabolites']

    j1.sort_values('Total', ascending=False, inplace=True)

    return j1


def ler_TP(table):
    tr = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=0)
    pr = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=1)

    map_tr = {'Occurences of enzymes/compounds': 'Occurences of Transcripts'}
    map_pr = {'Occurences of enzymes/compounds': 'Occurences of Proteins'}

    tr.rename(columns=map_tr, inplace=True)
    pr.rename(columns=map_pr, inplace=True)

    j1 = pd.merge(left=tr, right=pr, on=['Pathway', 'Pathway id'], how='outer')
    j1.fillna(0, inplace=True)

    j1['Total'] = j1['Occurences of Transcripts'] + j1['Occurences of Proteins']

    j1.sort_values('Total', ascending=False, inplace=True)

    return j1


def ler_TPM(table):
    tr = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=0)
    pr = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=1)
    mt = pd.read_excel('/content/Resultado_Fusion.xlsx', sheet_name=2)

    map_tr = {'Occurences of enzymes/compounds': 'Occurences of Transcripts'}
    map_pr = {'Occurences of enzymes/compounds': 'Occurences of Proteins'}
    map_mt = {'Occurences of enzymes/compounds': 'Occurences of Metabolites'}

    tr.rename(columns=map_tr, inplace=True)
    pr.rename(columns=map_pr, inplace=True)
    mt.rename(columns=map_mt, inplace=True)

    j1 = pd.merge(left=tr, right=pr, on=['Pathway', 'Pathway id'], how='outer')
    j1.fillna(0, inplace=True)

    j2 = pd.merge(left=j1, right=mt, on=['Pathway', 'Pathway id'], how='outer')
    j2.fillna(0, inplace=True)

    j2['Total'] = j2['Occurences of Transcripts'] + j2['Occurences of Proteins'] + \
                  j2['Occurences of Metabolites']

    j2.sort_values('Total', ascending=False, inplace=True)

    return j2


def make_excel(table):
    buffer = io.BytesIO()

    with pd.ExcelWriter(buffer, engine='xlsxwriter') as writer:
        table.to_excel(writer, sheet_name=f'Teste_Primers', index=False)

    return buffer
