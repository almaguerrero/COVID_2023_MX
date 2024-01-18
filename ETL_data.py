# -*- coding: utf-8 -*-
"""
Created on Thu Jan 18 13:10:09 2024

@author: eliza
"""

import pandas as pd


df = pd.read_csv('COVID19MEXICO.csv',dtype=object)

columnas_a_ignorar = ['FECHA_INGRESO','FECHA_SINTOMAS','FECHA_DEF','PAIS_NACIONALIDAD']

# Iterar sobre las columnas del DataFrame
for columna in df.columns:
    # Convertir a tipo entero si no está en la lista de columnas a ignorar
    if columna not in columnas_a_ignorar:
        df[columna] = pd.to_numeric(df[columna], errors='coerce').astype('Int64')
        
df['FECHA_INGRESO'] = pd.to_datetime(df['FECHA_INGRESO'], format='%d/%m/%Y', dayfirst=True,errors='coerce')
df['FECHA_SINTOMAS'] = pd.to_datetime(df['FECHA_SINTOMAS'], format='%d/%m/%Y', dayfirst=True,errors='coerce')
df['FECHA_DEF'] = pd.to_datetime(df['FECHA_DEF'], format='%d/%m/%Y', dayfirst=True,errors='coerce')
df['PAIS_NACIONALIDAD'] = pd.to_datetime(df['PAIS_NACIONALIDAD'],errors='coerce').astype(str)

df.to_csv("covid_file_format.csv", index=False)