import cx_Oracle

connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

cursor = connection.cursor()
try:

    miSueldoMinimo = input("Introduce sueldo mínimo:")
    miSueldoMaximo = input("Introduce sueldo máximo:")
    consulta = ("SELECT apellido,oficio, salario FROM emp where SALARIO BETWEEN :p1 AND :p2")
    cursor.execute(consulta, (miSueldoMinimo, miSueldoMaximo))
    # Si en un único parámetro tenemos que poner ',' a continuación del valor de la variable
    resultado = False
    for ape, ofi , sal  in cursor:
        print("Apellido: ", ape)
        print("Oficio: ", ofi)
        print("Salario: ", str(sal))
        resultado = True
    if resultado==False:
       print ("Sin resultados")



except connection.Error as error:
    print("Error: ", error)

connection.close()
