import random

def probabilidad(num_lanzamientos,num_caras):
   
   resultados=[random.choice([0,1]) for _ in range(num_lanzamientos)]
   
   prob=resultados.count(1)/num_lanzamientos
   return prob

num_lanzamientos=10
num_caras=6

prob=probabilidad(num_lanzamientos,num_caras)
print(f"La probabilidad de obtener {num_caras} caras en {num_lanzamientos} es prob{prob:.4f}")