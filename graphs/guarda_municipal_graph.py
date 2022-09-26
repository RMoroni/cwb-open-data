from .graph import Graph


class GuardaMunicipalGraph(Graph):

    def __init__(self):
        super().__init__('guarda_municipal', 'datasets/local/')
        self._load_dataset()
        # self._generate_graphs()
        # self._save_graphs()

    def _load_dataset(self):
        pass

    def _generate_graphs(self):
        pass

    def _save_graphs(self):
        pass

    def show_graphs(self):
        pass
