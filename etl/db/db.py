from abc import ABC, abstractmethod


class DB(ABC):

    def __init__(self):
        print('Opeing DB connection...', end='')
        self._db_connection = None
        print('done!')
        self._dataset = None

    @abstractmethod
    def open_dataset(self):
        pass

    @abstractmethod
    def save_dataset(self):
        pass

