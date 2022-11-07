import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns

from .graph import Graph

LOCAL_PATH = 'graphs/images/'


class GuardaMunicipalGraph(Graph):

    def __init__(self):
        super().__init__('guarda_municipal', 'datasets/local/')
        self._load_dataset()

    def _load_dataset(self):
        self._dataset = pd.read_parquet(f'{self._dataset_path}{self._name}_clean_dataset.parquet')

    def generate_graphs(self):
        print('Creating and saving graphs...', end='')

        sns.set(rc={'figure.figsize': (30, 20)})

        robbery_df = self._dataset[self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo']
        top_types_count_by_region_df = self._dataset[
            self._dataset['NATUREZA1_DESCRICAO'].isin(self._dataset['NATUREZA1_DESCRICAO'].value_counts().index[:10])]

        robbery_count_by_year = robbery_df['ATENDIMENTO_ANO'].value_counts().sort_index()
        robbery_count_by_hour = robbery_df['HORA'].str[:2].value_counts().sort_index()
        count_by_type = self._dataset['NATUREZA1_DESCRICAO'].value_counts()

        sns.barplot(x=robbery_count_by_year.index, y=robbery_count_by_year).get_figure().savefig(
            f"{LOCAL_PATH}{self._name}/robbery_count_by_year.png")
        plt.clf()

        sns.barplot(x=robbery_count_by_hour.index, y=robbery_count_by_hour).get_figure().savefig(
            f"{LOCAL_PATH}{self._name}/robbery_count_by_hour.png")
        plt.clf()

        sns.countplot(x=robbery_df["OCORRENCIA_DIA_SEMANA"]).get_figure().savefig(
            f"{LOCAL_PATH}{self._name}/robbery_count_by_weekday.png")
        plt.clf()

        count_by_type.plot(kind='pie').get_figure().savefig(
            f"{LOCAL_PATH}{self._name}/count_by_type.png")
        plt.clf()

        sns.countplot(data=top_types_count_by_region_df, x='REGIONAL_FATO_NOME',
                      hue='NATUREZA1_DESCRICAO').get_figure().savefig(
            f"{LOCAL_PATH}{self._name}/region_count_by_type.png")
        plt.clf()

        print('done!')

    def print_general_statistics(self):
        print('Quantidade de roubos por RUA no CENTRO a partir de 2018')
        print(self._dataset[(self._dataset['ATENDIMENTO_BAIRRO_NOME'] == 'CENTRO') & (
                self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo') & (
                                    self._dataset['ATENDIMENTO_ANO'] == '2021')][
                  'LOGRADOURO_NOME'].value_counts()[:20])

        print('Quantidade de roubos por local público')
        print(self._dataset[self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo']['EQUIPAMENTO_URBANO_NOME'].value_counts()[
              0:10])

        print('Quantidade de roubos em 2020 no Cristo Rei separado por hora')
        print(self._dataset[
                  (self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo') & (self._dataset['ATENDIMENTO_ANO'] == '2020') & (
                              self._dataset['ATENDIMENTO_BAIRRO_NOME'] == 'CRISTO REI')]['OCORRENCIA_HORA'].str[
              0:2].value_counts()[0:15])
