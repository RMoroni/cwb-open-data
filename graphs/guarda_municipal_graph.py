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

        robbery_count_by_year = self._dataset[self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo']['ATENDIMENTO_ANO'].value_counts().sort_index()
        robbery_count_by_hour = self._dataset[self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo']['HORA'].str[:2].value_counts().sort_index()

        sns.barplot(x=robbery_count_by_year.index, y=robbery_count_by_year).get_figure().savefig(f"{LOCAL_PATH}{self._name}/robbery_count_by_year.png")
        sns.barplot(x=robbery_count_by_hour.index, y=robbery_count_by_hour).get_figure().savefig(f"{LOCAL_PATH}{self._name}/robbery_count_by_hour.png")

        print('done!')
