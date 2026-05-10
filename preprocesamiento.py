import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def cargar_datos(ruta):
    """
    Carga un archivo CSV y retorna un DataFrame.
    """
    return pd.read_csv(ruta)


def eliminar_nulos(df):
    """
    Elimina filas con valores nulos.
    """
    return df.dropna()


def eliminar_duplicados(df):
    """
    Elimina registros duplicados.
    """
    return df.drop_duplicates()


def codificar_categoricas(df):
    """
    Convierte variables categóricas a numéricas.
    """
    return pd.get_dummies(df)


def normalizar(df, columnas):
    """
    Normaliza columnas numéricas entre 0 y 1.
    """
    scaler = MinMaxScaler()

    df[columnas] = scaler.fit_transform(df[columnas])

    return df


def guardar_datos(df, ruta):
    """
    Guarda el DataFrame limpio.
    """
    df.to_csv(ruta, index=False)


if __name__ == "__main__":

    # Cargar dataset
    df = cargar_datos("data/dataset.csv")

    # Preprocesamiento
    df = eliminar_nulos(df)

    df = eliminar_duplicados(df)

    df = codificar_categoricas(df)

    # Seleccionar columnas numéricas
    columnas_numericas = df.select_dtypes(
        include=["int64", "float64"]
    ).columns

    # Normalizar
    df = normalizar(df, columnas_numericas)

    # Guardar resultados
    guardar_datos(df, "data/dataset_limpio.csv")

    print("Preprocesamiento completado correctamente")
    