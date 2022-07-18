import pandas as pd
from pandas import DataFrame
from datetime import date


def get_dataset() -> DataFrame:
    path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month if date.today().day > 1 else date.today().month - 1}-01_sigesguarda_-_Base_de_Dados.csv"
    try:
        return pd.read_csv(path, encoding='latin-1', sep=';', low_memory=False)
    except:
        path = f"https://mid.curitiba.pr.gov.br/dadosabertos/Sigesguarda/{date.today().year}-{'0' if date.today().month < 10 else None}{date.today().month - 2}-01_sigesguarda_-_Base_de_Dados.csv"
        return pd.read_csv(path, encoding='latin-1', sep=';', low_memory=False)


if __name__ == "__main__":
    df = get_dataset()
    print(df.head())
