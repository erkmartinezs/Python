# La fundación Renacer requiere un algoritmo para calcular la nota definitiva de cada uno de los estudiantes de decimo semestre de sistemas del corte 1 (22 estudiantes), las notas relacionadas durante el semestre por estudiante son. Apoyo a la presencialidad 25%, trabajo en clase 45%, primer parcial 20%, producto entregable 10%.

menu = """

Welcome to Renacer foundation

Items
    - Apoyo a la presencialidad 25%
    - Trabajo en clase 45%
    - Primer parcial 20%
    - Producto entregable 10%

choose an option

    1 - Enter student grades 
    2 - Exit

:"""

opcion = int(input(menu))
if opcion == 1:
    apoyoPresencialidad = float(
        input('Apoyo a la presencialidad 25%: ')) * 0.25
    trabajoClase = float(input('Trabajo en clase 45%: ')) * 0.45
    primerParcial = float(input('Primer parcial 20%: ')) * 0.20
    productoEntregable = float(input('Producto entregable 10%: ')) * 0.11
    print('\n results: \n')
    print('Apoyo a la presencialidad: ' + str(round(apoyoPresencialidad, 2)))
    print('Trabajo en clase: ' + str(round(trabajoClase, 2)))
    print('Primer parcial: ' + str(round(primerParcial, 2)))
    print('Producto entregable: ' + str(round(productoEntregable, 2)))
    print('\n Final score: ' + str(apoyoPresencialidad +
          trabajoClase + primerParcial + productoEntregable))

else:
    print('𝑮𝒐𝒐𝒅𝒃𝒚𝒆')
