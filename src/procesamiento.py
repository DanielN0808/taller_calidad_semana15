import pandas as pd


def calcular_metricas_ventas(dataframe):
    """Calcula métricas básicas de ventas a partir de un DataFrame.

    Args:
        dataframe (pandas.DataFrame): DataFrame que debe contener
            las columnas "Cantidad" y "PrecioUnitario".

    Returns:
        dict: Diccionario con el total de ventas, la cantidad de
        registros y el promedio de venta.

    Raises:
        ValueError: Si el DataFrame está vacío.
        ValueError: Si faltan las columnas requeridas.
    """
    columnas_requeridas = ["Cantidad", "PrecioUnitario"]

    if dataframe.empty:
        raise ValueError("El DataFrame está vacío.")

    if not all(
        columna in dataframe.columns
        for columna in columnas_requeridas
    ):
        raise ValueError(
            "El DataFrame no contiene las columnas requeridas."
        )

    ventas = (
        dataframe["Cantidad"]
        * dataframe["PrecioUnitario"]
    )

    metricas = {
        "total_ventas": ventas.sum(),
        "cantidad_registros": len(dataframe),
        "promedio_venta": ventas.mean(),
    }

    return metricas