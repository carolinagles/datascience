# Modelo de Clasificación de Planes para Megaline

## **Descripción del Proyecto**
Megaline busca optimizar la asignación de planes telefónicos para sus clientes. El objetivo es desarrollar un modelo de clasificación que analice el comportamiento mensual de los clientes y recomiende uno de los dos nuevos planes: **Smart** o **Ultra**. Este modelo ayudará a identificar patrones en el uso de llamadas, mensajes y datos móviles para maximizar la satisfacción del cliente y la eficiencia operativa.

---

## **Estructura del Proyecto**

### **1. Exploración de Datos**
- **Archivo de entrada:** `datasets/users_behavior.csv`
- **Descripción de las columnas:**
  - `calls`: Número total de llamadas realizadas en el mes.
  - `minutes`: Duración total de las llamadas en minutos.
  - `messages`: Número de mensajes enviados.
  - `mb_used`: Uso total de datos móviles en MB.
  - `is_ultra`: Etiqueta binaria del plan actual:
    - **1:** Ultra.
    - **0:** Smart.

### **2. Segmentación de los Datos**
- División del conjunto de datos en:
  - **Entrenamiento (60%)**: Para entrenar el modelo.
  - **Validación (20%)**: Para ajustar los hiperparámetros.
  - **Prueba (20%)**: Para evaluar la calidad final del modelo.

### **3. Desarrollo del Modelo**
- **Tarea:** Crear un modelo de clasificación supervisado para predecir el plan (`is_ultra`).
- **Algoritmos evaluados:**
  - Árboles de decisión.
  - Bosques aleatorios (*Random Forest*).
  - Regresión logística.
- **Optimización de hiperparámetros:**
  - Profundidad de árboles.
  - Número de estimadores.
  - Parámetros de regularización.

### **4. Evaluación del Modelo**
- **Métrica de desempeño:** Exactitud (*accuracy*).
- **Umbral mínimo:** 0.75 en el conjunto de prueba.
- Realización de pruebas de cordura para asegurar la confiabilidad del modelo en datos reales.

---
