from pandas import DataFrame

COLUMNS_TO_DROP = ['NATUREZA1_DEFESA_CIVIL', 'NATUREZA2_DEFESA_CIVIL', 'NATUREZA2_DESCRICAO', 'NATUREZA3_DEFESA_CIVIL',
                   'NATUREZA3_DESCRICAO', 'NATUREZA4_DESCRICAO', 'NATUREZA5_DEFESA_CIVIL', 'NATUREZA5_DESCRICAO',
                   'NATUREZA4_DEFESA_CIVIL', 'OPERACAO_DESCRICAO', 'NUMERO_PROTOCOLO_156', 'SUBCATEGORIA2_DESCRICAO',
                   'SUBCATEGORIA3_DESCRICAO', 'SUBCATEGORIA4_DESCRICAO', 'SUBCATEGORIA5_DESCRICAO', 'OCORRENCIA_ANO',
                   'OCORRENCIA_CODIGO', 'ORIGEM_CHAMADO_DESCRICAO', 'SITUACAO_EQUIPE_DESCRICAO', 'SERVICO_NOME',
                   'SECRETARIA_SIGLA', 'SECRETARIA_NOME']
DICT_YES_NO = {'NÃO': 0, 'SIM': 1}
DICT_DAYS_OF_WEEK = {'DOMINGO': 1, 'SEGUNDA': 2, 'TERÇA': 3, 'QUARTA': 4, 'QUINTA': 5, 'SEXTA': 6, 'SÁBADO': 7}
NO_REGION = 'SB'
NO_REGION_LIST = ['-----------------------', 'BAIRRO FICTÍCIO', 'BAIRRO NAO INFORMADO', 'BAIRRO NÃO LOCALIZAD',
                  'INDICAÇÕES CANCELADA', 'NAN', 'NF', 'NI', 'NÃO ENCONTRADO', 'NÃO INFORMADO', 'SEM DADOS', 'SB']


def drop_columns(df: DataFrame, columns=COLUMNS_TO_DROP) -> DataFrame:
    return df.drop(labels=columns, axis=1, inplace=True)


def drop_rows(df: DataFrame, rows: dict) -> DataFrame:
    pass


def fill_invalid_records(df: DataFrame) -> DataFrame:
    # fill not mapped flags with NO flag
    df['FLAG_EQUIPAMENTO_URBANO'] = df['FLAG_EQUIPAMENTO_URBANO'].apply(
        lambda x: 'NÃO' if x not in DICT_YES_NO.keys() else x)
    df['FLAG_FLAGRANTE'] = df['FLAG_FLAGRANTE'].apply(
        lambda x: 'NÃO' if x not in DICT_YES_NO.keys() else x)

    # fill no mapped region with NO_REGION
    df['BAIRRO_NOME'] = df['BAIRRO_NOME'].apply(
        lambda x: NO_REGION if x in NO_REGION_LIST else x)

    return df


def transform_columns(df: DataFrame) -> DataFrame:
    # convert datetime fields in hour, date and year
    df['HORA'] = df['OCORRENCIA_HORA'].str[:5]
    df['DATA'] = df['OCORRENCIA_DATA'].str[:10]

    # add integer flags instead of literal names
    df['FLAG_INT_EQUIPAMENTO_URBANO'] = df['FLAG_EQUIPAMENTO_URBANO'].map(DICT_YES_NO)
    df['FLAG_INT_FLAGRANTE'] = df['FLAG_FLAGRANTE'].map(DICT_YES_NO)
    df['FLAG_INT_OCORRENCIA_DIA_SEMANA'] = df['OCORRENCIA_DIA_SEMANA'].map(DICT_DAYS_OF_WEEK)

    # fix some literals diff like: spaces and upper/lower case
    df['BAIRRO_NOME'] = df['ATENDIMENTO_BAIRRO_NOME'].str.strip()
    df['BAIRRO_NOME'] = df['BAIRRO_NOME'].str.upper()

    return df
'''
TODO: 
    gerar datetime baseado nos campos de data e hora
    separar transformação em duas etapas:
        1: ajustar as colunas sem realizar mudanças significativas no DF
        2: gerar outros DFs com agrupamentos
'''