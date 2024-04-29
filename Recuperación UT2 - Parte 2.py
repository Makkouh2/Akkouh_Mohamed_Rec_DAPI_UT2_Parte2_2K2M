def create_email(nombre, apellido):
    """Función que me crea un email dependiendo del nombre y apellido 
            -Parámetros:
                nombre: nombre del nombre
                apellido: apellido del alumno
            -Salida
                Devuelve el email creado a partir del nombre y apellido"""
    
    correo = nombre[0].lower() + apellido[:5].lower()+ "@educacion.navarra.es"
    return correo
nombre = "Mohamed"
apellido = "Akkouh"
print(create_email(nombre,apellido))
