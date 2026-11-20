import pandas as pd
import pytest

from src.procesamiento import calcular_metricas_ventas


def test_calcular_metricas_ventas_correctamente():
    """Verifica que las métricas se calculen correctamente."""
    dataframe = pd.DataFrame(
        {
            "Cantidad": [2, 3],
            "PrecioUnitario": [10, 20],
        }
    )

    resultado = calcular_metricas_ventas(dataframe)

    assert resultado["total_ventas"] == 80
    assert resultado["cantidad_registros"] == 2
    assert resultado["promedio_venta"] == 40


def test_dataframe_vacio():
    """Verifica que se genere un error si el DataFrame está vacío."""
    dataframe = pd.DataFrame(
        columns=["Cantidad", "PrecioUnitario"]
    )

    with pytest.raises(
        ValueError,
        match="El DataFrame está vacío."
    ):
        calcular_metricas_ventas(dataframe)


def test_columnas_requeridas():
    """Verifica que se genere un error si faltan columnas obligatorias."""
    dataframe = pd.DataFrame(
        {
            "Cantidad": [1, 2, 3]
        }
    )

    with pytest.raises(
        ValueError,
        match="El DataFrame no contiene las columnas requeridas."
    ):
        calcular_metricas_ventas(dataframe)