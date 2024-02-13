import time
from tqdm import tqdm

# Número total de iteraciones
total_iterations = 100

# Crear una barra de progreso

# Simular una tarea que toma tiempo
for i in tqdm(range(total_iterations)):
    # Simular el trabajo
    time.sleep(0.1)
    
    # Actualizar la barra de progreso

# Cerrar la barra de progreso al finalizar

print("Tarea completada!")
