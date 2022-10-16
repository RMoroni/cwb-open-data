import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

from .graph import Graph


class GuardaMunicipalGraph(Graph):

    def __init__(self):
        super().__init__('guarda_municipal', 'datasets/local/')
        self._load_dataset()
        self._generate_graphs()
        # self._save_graphs()

    def _load_dataset(self):
        self._dataset = pd.read_parquet(f'{self._dataset_path}{self._name}_clean_dataset.parquet')

    def _generate_graphs(self):
        count_by_year_for_robbery = self._dataset[self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo']['ATENDIMENTO_ANO']\
            .value_counts().sort_index()
        sns.barplot(x=count_by_year_for_robbery.index,
                    y=count_by_year_for_robbery)
        plt.show()

    def _save_graphs(self):
        pass

    def show_graphs(self):
        pass
