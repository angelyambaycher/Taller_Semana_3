
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
