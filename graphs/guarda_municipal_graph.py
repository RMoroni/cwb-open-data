import pandas as pd
import seaborn as sns

from .graph import Graph

LOCAL_PATH = 'graphs/images/'


class GuardaMunicipalGraph(Graph):

    def __init__(self):
        super().__init__('guarda_municipal', 'datasets/local/')
        self._load_dataset()
        self._generate_graphs()
        self._save_graphs()

    def _load_dataset(self):
        self._dataset = pd.read_parquet(f'{self._dataset_path}{self._name}_clean_dataset.parquet')

    def _generate_graphs(self):
        robbery_count_by_year = self._dataset[self._dataset['NATUREZA1_DESCRICAO'] == 'Roubo']['ATENDIMENTO_ANO']\
            .value_counts().sort_index()
        self._graph_list.append(
            {
                'title': 'robbery_count_by_year',
                'plot': sns.barplot(x=robbery_count_by_year.index, y=robbery_count_by_year)
            }
        )

    def _save_graphs(self):
        print('Saving graphs...', end='')
        for graph in self._graph_list:
            graph['plot'].get_figure().savefig(f"{LOCAL_PATH}{self._name}/{graph['title']}.png")
        print('done!')

    def show_graphs(self):
        pass
