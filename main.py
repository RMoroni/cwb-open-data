from datasets.guarda_municipal_dataset import GuardaMunicipalDataset
from graphs.guarda_municipal_graph import GuardaMunicipalGraph

if __name__ == '__main__':
    teste = GuardaMunicipalDataset()
    # print(teste.raw_data.head())
    teste.load_clean_data()
    teste.save_dataset()
    gmc_graphs = GuardaMunicipalGraph()
