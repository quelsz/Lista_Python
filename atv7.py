numero = int(input("Diga um numero impar:"))

anterior = numero - 2
num_anterior = anterior * anterior

posterior = numero + 2
num_posterior = posterior * posterior

dif_anterior =  - numero 
dif_posterior = num_posterior - numero 

print(f"Diferenca do quadrado do anterior: {dif_anterior}.")
print(f"Diferenca do quadrado do posterior: {dif_posterior}.")
