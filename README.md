# Taller de Calidad - Pruebas Unitarias y Documentación

Proyecto desarrollado para aplicar buenas prácticas de estructura, documentación, pruebas unitarias y control de versiones en Python.

## Objetivo

Implementar una función para calcular métricas básicas de ventas a partir de un DataFrame de Pandas y validar su funcionamiento mediante pruebas unitarias con Pytest.

## Estructura del proyecto

```text
taller_calidad_semana15/
├── data/
├── src/
│   ├── __init__.py
│   └── procesamiento.py
├── tests/
│   ├── __init__.py
│   └── test_procesamiento.py
├── .github/
│   └── workflows/
│       └── tests.yml
├── .gitignore
├── README.md
└── requirements.txt
```

## Requisitos

- Python 3.12
- pandas
- pytest

## Instalación

Instalar las dependencias del proyecto con:

```bash
pip install -r requirements.txt
```

## Ejecución de pruebas

Para ejecutar las pruebas unitarias:

```bash
pytest -v
```

El proyecto incluye pruebas para:

- Cálculo correcto de las métricas de ventas.
- Validación de un DataFrame vacío.
- Validación de columnas obligatorias.

## Función principal

La función principal se encuentra en:

```text
src/procesamiento.py
```

y se llama:

```python
calcular_metricas_ventas(dataframe)
```

La función calcula:

- Total de ventas.
- Cantidad de registros.
- Promedio de venta.

## Desarrollo en la nube

El proyecto fue desarrollado y probado utilizando GitHub Codespaces.

También se configuró GitHub Actions para ejecutar automáticamente las pruebas con Pytest cada vez que se envían cambios a la rama principal.