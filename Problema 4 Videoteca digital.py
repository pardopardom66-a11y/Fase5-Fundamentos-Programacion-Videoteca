# Matriz con informacion de las peliculas
# Nombre del estudiante:Mary Alexandra Pardo Pardo
# Grupo: 2204
# Programa: Ingenieria de Sistemas
# Codigo Fuente: autoria propia

peliculas = [
    ["El viaje", 2022, 9, "Aventura"],
    ["La sombra", 2018, 8, "Suspenso"],
    ["Mundo magico", 2024, 7, "Fantasia"],
    ["Camino al futuro", 2021, 8, "Ciencia ficcion"],
    ["El secreto", 2019, 10, "Drama"],
    ["Estrellas", 2023, 9, "Romance"],
    ["La ultima mision", 2020, 6, "Accion"]
]

# Criterios de busqueda
calificacion_minima = 8
anio_limite = 2020

# Funcion para contar los titulos que cumplen los criterios
def contar_peliculas(matriz, calificacion, anio):
    contador = 0

    for pelicula in matriz:
        if pelicula[2] >= calificacion and pelicula[1] >= anio:
            contador = contador + 1

    return contador

# Llamar a la funcion
total = contar_peliculas(peliculas, calificacion_minima, anio_limite)

# Mostrar el resultado
print("Cantidad de peliculas que cumplen los criterios:", total)

