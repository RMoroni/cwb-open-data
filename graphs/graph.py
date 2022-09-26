from abc import ABC, abstractmethod


class Graph(ABC):

    def __init__(self, graph_name: str, dataset_path: str):
        self._name = graph_name
        self._dataset_path = dataset_path
        self._dataset = None
        self._graph_list = []

    @abstractmethod
    def _load_dataset(self):
        pass

    @abstractmethod
    def _generate_graphs(self):
        pass

    @abstractmethod
    def _save_graphs(self):
        pass

