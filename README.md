# Proyecto de Clustering con Dataset AI4I

# Proyecto: Segmentación de Máquinas Industriales con Métodos No Supervisados (AI4I 2020)

## 🎯 Objetivo
Implementar y analizar modelos de aprendizaje no supervisado (K-Means, DBSCAN, PCA y t-SNE) para segmentar perfiles operativos en un entorno tecnológico industrial.
El propósito es identificar patrones, detectar anomalías y visualizar los resultados de forma clara y técnica.

---

## 📂 1. Preparación del entorno
El proyecto fue desarrollado en **Python 3.9+** usando Google Colab.

**Librerías utilizadas:**
- pandas
- numpy
- matplotlib
- seaborn
- scikit-learn

---

## 📊 2. Dataset

Se usó el dataset **AI4I 2020 Predictive Maintenance**, validado por el docente.

Link oficial:
https://archive.ics.uci.edu/dataset/601/ai4i+2020+predictive+maintenance+dataset

Variables utilizadas:
- Air temperature \[K\]
- Process temperature \[K\]
- Rotational speed \[rpm\]
- Torque \[Nm\]
- Tool wear \[min\]

Estas variables representan el comportamiento físico de las máquinas y permiten construir perfiles operativos.

---

## 🔍 3. Análisis Exploratorio (EDA)

Incluye:

- Estadísticos descriptivos
- Distribuciones y pairplots
- Heatmap de correlaciones
- Eliminación de columnas irrelevantes (UDI, Product ID, Type)
- Escalado con StandardScaler

Hallazgos:
- Fuerte correlación entre temperaturas del aire y del proceso
- Alta dispersión en torque y velocidad → ideal para clustering
- Diferencias operativas claras en desgaste de herramienta

---

## 🤖 4. Implementación de Modelos

### 🔹 4.1 K-Means
- Se evaluó k entre 2 y 10 (método del codo + índice silhouette).
- El mejor valor fue **k = 4**.
- Los clusters representan diferentes perfiles de operación industrial.

### 🔹 4.2 DBSCAN
- Ajuste mediante eps y min_samples
- Detectó:
  - 1 cluster principal
  - varios grupos pequeños
  - outliers catalogados como -1
- Útil para identificar máquinas con comportamiento anómalo.

### 🔹 4.3 PCA
- Reducción a 2 componentes principales
- Permite visualización global de los grupos

### 🔹 4.4 t-SNE
- Proyección no lineal
- Identifica microgrupos y estructura interna compleja

---

## 📈 5. Visualización de Resultados

Incluye:

- Comparación entre K-Means y DBSCAN
- PCA 2D coloreado por cluster
- t-SNE coloreado
- Tabla resumen de perfiles
- Identificación de centroides

---

## 🧩 6. Perfiles Detectados (K-Means)

### **Cluster 0 – Operación Estable**
- Alta velocidad
- Torque medio
- Desgaste moderado

### **Cluster 1 – Operación Ligera**
- Torque bajo
- Velocidad baja
- Mínimo desgaste

### **Cluster 2 – Operación Mixta**
- Velocidad media
- Torque variable

### **Cluster 3 – Uso Extremo**
- Alto torque
- Alto desgaste
- Riesgo potencial de falla

---

## 🔄 7. Comparación entre Métodos

### ✔ K-Means
- Grupos muy definidos
- Representación consistente
- Útil para clustering general

### ✔ DBSCAN
- Detecta outliers naturalmente
- Más sensible a parámetros
- Adecuado para identificar anomalías

---

## Conclusiones principales

1. **Estructura de cuatro clusters bien definida (K-Means)**  
   El método del codo y el índice Silhouette indicaron que *k = 4* es un valor adecuado.  
   Los clusters identifican patrones claros de operación de las máquinas, diferenciados
   principalmente por el torque aplicado, la velocidad de rotación y el desgaste de herramienta.

2. **Perfiles operativos diferenciados**
   - **Cluster 0 – Operación estable:**  
     Velocidad alta, torque medio y desgaste moderado. Corresponde a un régimen productivo
     normal y relativamente controlado.
   - **Cluster 1 – Operación ligera:**  
     Velocidad y torque bajos, con poco desgaste. Representa equipos en uso parcial,
     pruebas o baja carga de trabajo.
   - **Cluster 2 – Operación mixta:**  
     Condiciones intermedias y mayor variabilidad en torque, lo que sugiere cambios frecuentes
     de condiciones de operación.
   - **Cluster 3 – Uso extremo:**  
     Alto torque y alto desgaste de herramienta. Este grupo concentra la mayor probabilidad
     de riesgo operativo y necesidad de mantenimiento preventivo.

3. **DBSCAN complementa la detección de anomalías**  
   Mientras que K-Means ofrece una segmentación global, DBSCAN permitió identificar
   ejemplos etiquetados como *ruido (-1)*, asociados a combinaciones poco frecuentes
   de torque, velocidad y desgaste. Estos puntos son candidatos a revisión detallada
   por posible comportamiento anómalo.

4. **PCA y t-SNE mejoran la interpretación visual**  
   - **PCA 2D** conserva gran parte de la varianza y muestra que los cuatro clusters
     de K-Means se separan razonablemente bien en el espacio reducido.  
   - **t-SNE** revela microgrupos y transiciones suaves entre clusters, ayudando a
     entender que la frontera entre “operación estable” y “uso extremo” no es rígida,
     sino gradual.

5. **Los patrones de operación se alinean con la lógica del proceso industrial**  
   Las combinaciones de alto torque + alto desgaste coinciden con escenarios de mayor
   exigencia mecánica, mientras que bajos niveles de desgaste se relacionan con menor
   velocidad o menor torque, validando la coherencia del modelo con el dominio del problema.

 ## Recomendaciones

- Los modelos actuales se basan únicamente en variables físicas (temperatura, torque,
  velocidad y desgaste). No se consideraron variables de contexto (operador, turno,
  tipo de pieza trabajada).
- K-Means asume clusters aproximadamente esféricos y puede no capturar estructuras
  más complejas.
- t-SNE es muy útil para visualización, pero no debe usarse para decisiones numéricas
  directas.

Como trabajo futuro se recomienda incorporar más características, evaluar otros algoritmos
de clustering (por ejemplo, Gaussian Mixture Models o HDBSCAN) y conectar estos resultados
con indicadores de negocio como disponibilidad (OEE), tiempos de parada y costos de reparación

---

## ⚠️ Limitaciones

- PCA pierde estructura no lineal
- t-SNE requiere ajuste fino
- DBSCAN depende de eps y min_samples
- K-Means requiere elegir k previamente

---

## 📁 Estructura del repositorio
Proyecto-Clustering-AI4I/
│
├── data/
├── notebooks/
├── src/
├── figures/
├── results/
├── README.md
└── requirements.txt


## 🚀 Instrucciones de uso

Instalar dependencias:

pip install -r requirements.txt

## 👤 Autor
Angel Yambay M
