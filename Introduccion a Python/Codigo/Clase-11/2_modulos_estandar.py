# import random as rd

# print(rd.random())


import random

def lanzar_dados():
    dado1 = random.randint(1, 6)
    dado2 = random.randint(1, 6)
    suma = dado1 + dado2
    print(f"Lanzaste un {dado1} y un {dado2}. La suma es {suma}.")

lanzar_dados()



