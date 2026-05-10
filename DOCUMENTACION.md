# DOCUMENTACIÓN DEL PROYECTO

# Preprocesamiento Ciencia de Datos

## Autor
Dayana Guaranga 

---

# Introducción

Este proyecto tiene como objetivo aplicar técnicas de preprocesamiento de datos utilizando Python y Pandas, además de implementar el uso de Git y GitHub para el control de versiones y automatización de procesos.

---

# Objetivo

Desarrollar un sistema de preprocesamiento de datos que permita:

- Eliminar valores nulos.
- Eliminar datos duplicados.
- Codificar variables categóricas.
- Normalizar datos numéricos.
- Automatizar la ejecución mediante GitHub Actions.

---

# Estructura del Proyecto

```plaintext
preprocesamiento-cienciadatos
│
├── data
│   ├── dataset.csv
│   └── dataset_limpio.csv
│
├── preprocesamiento.py
├── README.md
├── DOCUMENTACION.md
├── .gitignore
│
└── .github
    └── workflows
        └── python-app.yml
```

---

# Funcionalidades Implementadas

## Eliminación de valores nulos

Se utilizó:

```python
df.dropna()
```

para eliminar registros incompletos.

---

## Eliminación de duplicados

Se utilizó:

```python
df.drop_duplicates()
```

para eliminar filas repetidas.

---

## Codificación de variables categóricas

Se aplicó:

```python
pd.get_dummies(df)
```

para convertir variables categóricas a numéricas.

---

## Normalización de datos

Se utilizó:

```python
MinMaxScaler()
```

para normalizar los datos entre 0 y 1.

---

# Comandos Git Utilizados

## Inicializar repositorio

```bash
git init
```

## Agregar archivos

```bash
git add .
```

## Crear commit

```bash
git commit -m "mensaje"
```

## Subir cambios a GitHub

```bash
git push
```

## Crear rama

```bash
git checkout -b feature-preprocesamiento
```

---

# Pull Request

Se creó una Pull Request para fusionar la rama:

```plaintext
feature-preprocesamiento
```

con la rama principal:

```plaintext
main
```

Posteriormente se realizó el merge y eliminación de la rama.

---

# Automatización con GitHub Actions

Se implementó un workflow utilizando el archivo:

```plaintext
.github/workflows/python-app.yml
```

El workflow realiza automáticamente:

1. Clonación del repositorio.
2. Configuración de Python.
3. Instalación de dependencias.
4. Ejecución del script `preprocesamiento.py`.

---

# Evidencias

Se incluyen capturas de pantalla de:

- Comandos Git ejecutados.
- Creación de ramas.
- Pull Request.
- Merge realizado.
- Ejecución correcta de GitHub Actions.
- Ejecución del script Python.

---

# Conclusiones

El proyecto permitió aplicar conocimientos de Git, GitHub y Python para el desarrollo de procesos de preprocesamiento de datos y automatización básica utilizando GitHub Actions.

---

# Repositorio GitHub

https://github.com/natalimancero984-boop/preprocesamiento-cienciadatos