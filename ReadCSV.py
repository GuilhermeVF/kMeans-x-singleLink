import pandas as pd

def read(path):
    #Leitura Data Frame
    df = pd.read_csv(path, skipinitialspace=True)

    #Tratamento dos dados 

    columns = df.columns

    #Passo para Ignorar elementos que não sejam númericos, caso se deseje utiliza-los, outros metodos devem ser utilizados, aqui no trabalho foi escolhido por ignora-los
    for i in columns:
        if type(df[i][0]) is str:
            try:
                df = df.drop(columns = [i])
            except:
                pass

    #Tenta deletar a coluna ID, por tentativa e erro, uma vez que não temos como ter certeza que a coluna é de ID atráves de seus números, mas apenas por seu nome.
    try:
        df = df.drop(columns=['Id'])
    except:
        pass

    try:
        df = df.drop(columns=['id'])
    except:
        pass

    try:
        df = df.drop(columns=['ID'])
    except:
        pass

    return df
