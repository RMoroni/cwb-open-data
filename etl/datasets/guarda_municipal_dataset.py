from datetime import date
from urllib.error import URLError
from os.path import exists
from pandas import DataFrame

import pandas as pd

from dataset import Dataset

COLUMNS_TO_DROP = ['NATUREZA1_DEFESA_CIVIL', 'NATUREZA2_DEFESA_CIVIL', 'NATUREZA2_DESCRICAO', 'NATUREZA3_DEFESA_CIVIL',
                   'NATUREZA3_DESCRICAO', 'NATUREZA4_DESCRICAO', 'NATUREZA5_DEFESA_CIVIL', 'NATUREZA5_DESCRICAO',
                   'NATUREZA4_DEFESA_CIVIL', 'OPERACAO_DESCRICAO', 'NUMERO_PROTOCOLO_156', 'SUBCATEGORIA2_DESCRICAO',
                   'SUBCATEGORIA3_DESCRICAO', 'SUBCATEGORIA4_DESCRICAO', 'SUBCATEGORIA5_DESCRICAO', 'OCORRENCIA_ANO',
                   'OCORRENCIA_CODIGO', 'ORIGEM_CHAMADO_DESCRICAO', 'SITUACAO_EQUIPE_DESCRICAO', 'SERVICO_NOME',
                   'SECRETARIA_SIGLA', 'SECRETARIA_NOME']
DICT_YES_NO = {'NÃO': 0, 'SIM': 1}
DICT_DAYS_OF_WEEK = {'DOMINGO': 1, 'SEGUNDA': 2, 'TERÇA': 3, 'QUARTA': 4, 'QUINTA': 5, 'SEXTA': 6, 'SÁBADO': 7}
NO_REGION = 'NR'
NO_REGION_LIST = ['-----------------------', 'BAIRRO FICTÍCIO', 'BAIRRO NAO INFORMADO', 'BAIRRO NÃO LOCALIZAD',
                  'INDICAÇÕES CANCELADA', 'NAN', 'NF', 'NI', 'NÃO ENCONTRADO', 'NÃO INFORMADO', 'SEM DADOS', 'SB']


def _fill_year(row):
    if row['ATENDIMENTO_ANO'] is None:
        row['ATENDIMENTO_ANO'] = date.fromisoformat(row['OCORRENCIA_DATA'][:10]).year
    return row


class GuardaMunicipalDataset(Dataset):

    def __init__(self):
        super().__init__('guarda_municipal')
        self._load_raw_data()

    def _load_raw_data(self):
        print('Loading raw dataset...', end='')
        if exists(f'{self.name}_raw_dataset.parquet'):
            print('loading local raw dataset...', end='')
            self._raw_data = pd.read_parquet(f'{self.name}_raw_dataset.parquet')
            print('done!')
            return
        path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month if date.today().day > 1 else date.today().month - 1}-01_sigesguarda_-_Base_de_Dados.csv"
        try:
            self._raw_data = pd.read_csv(path, encoding='latin-1', sep=';', low_memory=False)
            print('done!')
        except URLError:
            path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month - 2}-01_sigesguarda_-_Base_de_Dados.csv"
            self._raw_data = pd.read_csv(path, encoding='latin-1', sep=';', low_memory=False)
            print('done!')
        except Exception as e:
            print(f'unable to load raw data: {e}')

    def load_clean_data(self):
        self._clean_data = self._raw_data.copy()
        print('Cleaning dataset...', end='')
        self._drop_columns()
        self._drop_rows()
        self._fill_invalid_records()
        self._create_flag_columns()
        self._transform_columns()
        print('done!')
        print('Clean Dataset Null Values:')
        print(self._clean_data.isna().sum())

    def save_dataset(self):
        # TODO: create dir for datasets files
        if self._raw_data is not None:
            print(f'Saving {self.name} raw dataset...', end='')
            self._raw_data.to_parquet(f'{self.name}_raw_dataset.parquet')
            print('done!')
        if self._clean_data is not None:
            print(f'Saving {self.name} clean dataset...', end='')
            self._clean_data.to_parquet(f'{self.name}_clean_dataset.parquet')
            print('done!')

    @property
    def name(self) -> str:
        return self._name

    def _drop_columns(self):
        self._clean_data.drop(labels=COLUMNS_TO_DROP, axis=1, inplace=True)

    def _drop_rows(self):
        self._clean_data.drop([0, 0], inplace=True)  # the first line is invalid

    def _fill_invalid_records(self):
        self._clean_data['FLAG_EQUIPAMENTO_URBANO'] = self._clean_data['FLAG_EQUIPAMENTO_URBANO'].apply(
            lambda x: 'NÃO' if x not in DICT_YES_NO.keys() else x)

        self._clean_data['FLAG_FLAGRANTE'] = self._clean_data['FLAG_FLAGRANTE'].apply(
            lambda x: 'NÃO' if x not in DICT_YES_NO.keys() else x)

        # fill no mapped region with NO_REGION
        self._clean_data['ATENDIMENTO_BAIRRO_NOME'] = self._clean_data['ATENDIMENTO_BAIRRO_NOME'].apply(
            lambda x: NO_REGION if x in NO_REGION_LIST else x)
        self._clean_data['ATENDIMENTO_BAIRRO_NOME'].fillna(value=NO_REGION, inplace=True)

        self._clean_data['REGIONAL_FATO_NOME'] = self._clean_data['REGIONAL_FATO_NOME'].apply(
            lambda x: NO_REGION if x == '--------------------' else x)
        self._clean_data['REGIONAL_FATO_NOME'].fillna(value=NO_REGION, inplace=True)

        self._clean_data.apply(_fill_year, axis=1)

    def _create_flag_columns(self):
        self._clean_data['FLAG_INT_EQUIPAMENTO_URBANO'] = self._clean_data['FLAG_EQUIPAMENTO_URBANO'].map(DICT_YES_NO)
        self._clean_data['FLAG_INT_FLAGRANTE'] = self._clean_data['FLAG_FLAGRANTE'].map(DICT_YES_NO)
        self._clean_data['FLAG_INT_OCORRENCIA_DIA_SEMANA'] = self._clean_data['OCORRENCIA_DIA_SEMANA'].map(
            DICT_DAYS_OF_WEEK)

    def _transform_columns(self):
        self._clean_data['HORA'] = self._clean_data['OCORRENCIA_HORA'].str[:5]
        self._clean_data['DATA'] = self._clean_data['OCORRENCIA_DATA'].str[:10]

        self._clean_data['BAIRRO_NOME'] = self._clean_data['ATENDIMENTO_BAIRRO_NOME'].str.strip()
        self._clean_data['BAIRRO_NOME'] = self._clean_data['BAIRRO_NOME'].str.upper()


if __name__ == '__main__':
    teste = GuardaMunicipalDataset()
    # print(teste.raw_data.head())
    teste.load_clean_data()
    # teste.save_dataset()
