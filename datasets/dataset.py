from abc import ABC, abstractmethod
from pandas import DataFrame


class Dataset(ABC):

    def __init__(self, dataset_name: str):
        self._name = dataset_name
        self._raw_data = None
        self._clean_data = None

    @abstractmethod
    def _load_raw_data(self):
        pass

    @property
    def raw_data(self) -> DataFrame:
        return self._raw_data

    @abstractmethod
    def load_clean_data(self):
        pass

    @property
    def clean_data(self) -> DataFrame:
        return self._clean_data

    @abstractmethod
    def save_dataset(self):
        pass

    @property
    @abstractmethod
    def name(self) -> str:
        pass
