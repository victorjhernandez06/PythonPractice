###FUNCTIONS###




# Exercises (simple)
def my_function():
    print('this is a function')
    
my_function() #Esta es la llamada a la funcion, con esto aparece en pantalla: 'esto es una funcion'


def sum_two_values (first_num,  second_num):
    print(first_num + second_num) #hace una suma entre dos parametros.
    
sum_two_values(23, 21) #ejecuta la funcion e imprime la suma dentro de la funcion.

def sum_a_b (a, b):
    return(a+b)

print(sum_a_b(2,2)) #  --> devuelve e imprime la suma de 2+2 = 4
print(sum_a_b(1.4,22.8)) # --> 24.2 


# Al tipado no funciona aqui.
# Aqui he tipado el numero, pero al indicar que son string los datos, no toma en cuenta este tipado. NO sirve de nada por el tiempo de ejecucion, pues tomara los datos que le metamos datos. 
def function_2(numb1:int, numb2:int): #aqui probamos tipando los parametros
    return(numb1+numb2)
print(function_2('22','20'))

###
def sum_two_val (a, b):
    return(a + b)

my_result = sum_two_val(2,3)
print(my_result) #-->5

### Usando el retorn 
def sum1(a,b):
    my_sum = a + b
    return my_sum

operation = sum1(2,32)
print(operation) #--> 34

def print_name(name, surname):
    print(f"{name} {surname}")

print_name('Victor','Hernandez') #--> Victor Hernandez
print_name(surname="Hernandez",name='Victor') #aqui reordene el nombre, indicando el valor de los parametros en la llamada. ##--> Victor Hernandez


### Aqui utilizamos parametros definidos dentro de la funcion, sin usar el constructor.
def print_name_with_default(name,surname, alias = 'Sin Alias'):
    print(f"{name} {surname} {alias}")
    
print_name_with_default('Victor','Hernandez','Victordev06') #--> Victor Hernandez Victordev06
print_name_with_default('Victor','Hernandez') #--> Victor Hernandez Sin Alias

###
def print_texts(*text):
    print(text)
    
print_texts('Hola')

