from sklearn.preprocessing import OneHotEncoder, LabelEncoder, StandardScaler

# Remoção de colunas do dataframe
def limpezaDados(dataframe, rem_colunas):
    # Remoção de colunas irrelevantes
    df = dataframe.drop(rem_colunas, axis=1, inplace=True)

    return df

# Transformação OneHotEncoder
def transforma_onehot(dataframe, colunas_onehot):
    oneHot = OneHotEncoder()
    dataframe[colunas_onehot] = oneHot.fit_transform(dataframe[colunas_onehot])

# Tranformação LabelEncoder
def transforma_labelencoder(dataframe, colunas_label):
    label = LabelEncoder()
    dataframe[colunas_label] = label.fit_transform(dataframe[colunas_label])

# Escalando as colunas em StandardScaler
def standardScaler(dataframe, colunas_standard):
    scaler = StandardScaler()
    dataframe[colunas_standard] = scaler.fit_transform(dataframe[StandardScaler])