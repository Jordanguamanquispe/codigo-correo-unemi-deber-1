def mayor(e): 
    edad = 2024 - e 
    if edad >= 18 : 
        print(f"tienes {edad} eres mayor de edad ")
    else:
        print(f"tu edad es {edad} no eres mayor de edad ")
        
    return edad
    
def generar_correo(nombre, apellido1, apellido2):
    ig = nombre[0]  
    ap1 = apellido1  
    ap2 = apellido2[0]  
    correo_institucional = f"{ig}{ap1}{ap2}@unemi.edu.ec"
    return correo_institucional

def generar_contraseña(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation 
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

nombre = input("escriba su nombre: ")
apellido1= input("ingrese su primer apellido : ")
apellido2 =input("escriba su segundo apellido: ")
fechaDenacimiento = int (input("ingrese el año de nacimiento: "))
edad = mayor(fechaDenacimiento )


correo = generar_correo(nombre, apellido1, apellido2)
print("Tu correo institucional es:", correo)

import random
import string
longitud_contraseña = 15  # Puedes ajustar la longitud según tus necesidades
contraseña_generada = generar_contraseña(longitud_contraseña)
print(f"Su contraseña es: {contraseña_generada}")
