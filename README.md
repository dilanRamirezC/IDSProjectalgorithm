Proyecto Algoritmo de Detección de Ataques DDoS con Random Forest

Este proyecto implementa un sistema de detección de intrusos (IDS) orientado a ataques **DDoS** utilizando un algoritmo de **Random Forest**. Fue desarrollado y probado en **Google Colab**, con tráfico real extraído desde archivos `.pcap`, procesado y analizado para inferencia.

## Descripción

La solución toma archivos `.pcap` capturados en entornos simulados de ataque, extrae características relevantes y ejecuta un modelo previamente entrenado para clasificar el tráfico como `DDoS` o `BENIGN`.  
Está basado en el dataset [CIC-IDS2017](https://www.kaggle.com/datasets) publicado en Kaggle.

---

##  Estructura del repositorio

 Documentacion → Información del proyecto, conceptos y explicación técnica
 GraficaAnalisis → Análisis exploratorio y visualizaciones
 SniferV1 → Sniffer adaptado para leer archivos .pcap y generar features


---

## Funcionalidades implementadas

-  Lectura de archivos `.pcap` con PyShark
-  Extracción de features personalizados por flujo (bidireccionales)
-  Modelo de predicción con Random Forest
-  Gráficas comparativas y análisis de variables
-  Exportación de resultados a `.csv`
-  Trabajo totalmente en **Google Colab**

---

## Requisitos

Este proyecto se ejecuta únicamente en **Google Colab**, por lo que no necesitas configuraciones locales complejas.

### Bibliotecas necesarias:
- `pandas`
- `pyshark`
- `joblib`
- `sklearn`
- `matplotlib`
- `seaborn`
- `nest_asyncio` *(para evitar errores de bucles en Colab)*
  
---

Modelo
Algoritmo: RandomForestClassifier

Dataset de entrenamiento: CIC-IDS2017 (Kaggle)

Features principales:

-Flow_Duration

-Total_Fwd_Packets

-Total_Backward_Packets

-Fwd_IAT_Mean

-SYN_Flag_Count

-Fwd_Packet_Length_Mean

-Down/Up_Ratio

---


Resultado final
-Métricas obtenidas: Accuracy, Precision, Recall, F1-score

-Matriz de confusión generada y evaluada

-Predicciones exportadas a CSV con etiquetas

---

Créditos
Dataset: Kaggle - CIC-IDS2017

Autor: Anónimo por seguridad

Proyecto educativo con fines de formación en análisis SOC y ciberseguridad


