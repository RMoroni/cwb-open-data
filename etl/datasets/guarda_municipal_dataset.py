from datetime import date
from pandas import DataFrame

import pandas as pd

from dataset import Dataset


class GuardaMunicipalDataset(Dataset):

    def __init__(self):
        super().__init__(self.__class__.__name__)
        self._load_raw_data()

    def _load_raw_data(self):
        path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month if date.today().day > 1 else date.today().month - 1}-01_sigesguarda_-_Base_de_Dados.csv"
        try:
            self._raw_data = pd.read_csv(path, encoding='latin-1', sep=';', low_memory=False)
        except:
            path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month - 2}-01_sigesguarda_-_Base_de_Dados.csv"
            self._raw_data = pd.read_csv(path, encoding='latin-1', sep=';', low_memory=False)

    @property
    def raw_data(self) -> DataFrame:
        return self._raw_data if self._raw_data is not None else pd.DataFrame()

    def _load_clean_data(self):
        print('Cleaning dataset...')
        self._drop_columns()
        self._drop_rows()
        self._fill_invalid_records()
        self._create_flag_columns()
        self._transform_columns()
        print('Clean dataset done!')

    @property
    def clean_data(self) -> DataFrame:
        return self._clean_data

    def save_dataset(self):
        # TODO: create dir for datasets files
        if self._raw_data is not None:
            print(f'Saving {self.name} raw dataset...')
            self._raw_data.to_parquet(f'{self.name}_raw_dataset.parquet')
        if self._clean_data is not None:
            print(f'Saving {self.name} clean dataset...')
            self._clean_data.to_parquet(f'{self.name}_clean_dataset.parquet')

    @property
    def name(self) -> str:
        return self._name

    def _drop_columns(self):
        pass

    def _drop_rows(self):
        pass

    def _fill_invalid_records(self):
        pass

    def _create_flag_columns(self):
        pass

    def _transform_columns(self):
        pass


if __name__ == '__main__':
    teste = GuardaMunicipalDataset()
    print(teste.name)
    print(teste.raw_data.head())
    teste.save_dataset()
