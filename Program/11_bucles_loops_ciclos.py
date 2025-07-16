"""BUCLES / LOOPS / CICLOS"""
# LOOPS

"""PYTHON WHILE LOOPS"""
# WHILE LOOP
# El while es como un if infinito y por ello podemos colocarle un else.
my_condition = 0

while my_condition < 10:
    print(my_condition) # Lo que se ejecuta, despes de esto colocamos el incremento.
    my_condition += 4 # Aumento de la condicion, cada que sale del while
else: 
    print("Ya despues de este numero superamos la codicion del while")
print("--> Aqui estamos fuera del While y seguimos ejecutando el programa")

# the while loop
# with the while loop we can execute a set of statements as log as a condition is true

# Exercise
# print i as long as i is less than 6

i = 1
while i < 6:
    print(i)
    i += 1
# 1
# 2
# 3
# 4
# 5
print('continue with more exercise from while loops...')

# The while loop requires relevant variales to be ready, in this example we need to define an indexing variable, i, which we set to 1.

"""The break statement"""
# With the break statement we can stop the loop even if the while condition is true:
i = 1
while i < 6:
    print(i)
    if i == 3: 
        break  # Esto detiene la ejecucion del while al llegar a cumplirse al condicion.
    i += 1
# 1
# 2
# 3
print('continue with more exercise from while loops...')


"""The continue Statement"""
i = 0 
while i < 6:
    i += 1
    if i == 3:
        continue  # Esto indica que al cumplirse la condicion, se salta el valor indicado en if, es decir, cuando i == 3, saltara y continua con la ejecucion sin incluir a este en el resultado final del while.
    print(i) 
# 1
# 2
# 4
# 5
# 6   
print('continue with more exercise from while loops...')


"""The else statement"""
# with the else statement, we can run a block of code once when the condition no longer is true

# example
# Print a message once the condition is false:
i = 1
while i < 6:
    print(i)
    i = i + 1
else:
    print("i is no longer less than 6")
# 1
# 2
# 3
# 4
# 5
# i is no longer less than 6
print('continue with more exercise from while loops...')