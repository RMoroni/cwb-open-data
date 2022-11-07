from datasets.guarda_municipal_dataset import GuardaMunicipalDataset
from graphs.guarda_municipal_graph import GuardaMunicipalGraph

if __name__ == '__main__':
    guarda_municipal_dataset = GuardaMunicipalDataset()
    # print(guarda_municipal_dataset.raw_data.head())
    guarda_municipal_dataset.load_clean_data()
    # guarda_municipal_dataset.save_dataset()
    gmc_graphs = GuardaMunicipalGraph()
    # gmc_graphs.generate_graphs()
    gmc_graphs.print_general_statistics()
