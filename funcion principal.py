# -*- coding: cp1252 -*-
'''la funcion importa las operaciones de los modulos descriptos, solicita el
ingreso de los datos a utilizar e imprime los valores devueltos por las
funciones utilizadas para al final calcular y mostrar el porcentale de
corredores que finalizaron la carrera y su respectivo promedio de edades'''
from funcion_1 import validar_hora
from funciones_2 import validar_inscripcion, calc_marca, valida_numero
from funciones_3 import validar_edad, validar_genero
def main():
    competidores={}
    dic_edades={}
    hic=valida_numero(raw_input("A continuación ingrese el horario de inicio de la competencia. \nIngrese la hora: "))
    mic=valida_numero(raw_input("Ingrese los minutos: "))
    sic=valida_numero(raw_input("Ingrese los segundos: "))
    hic,mic,sic=validar_hora(8,0,0,hic,mic,sic)
    cant_competidores=valida_numero(raw_input("\nIngrese la cantidad de competidores inscriptos: "))
    finalistas=0
    menor_marca=(99,99,99)
    total_edades=0
    num_inscripcion=validar_inscripcion(valida_numero(raw_input("\nIngrese el número del competidor que finalizó el recorrido (o 0 para salir): ")))
    while num_inscripcion!=0:        
        competidores[num_inscripcion]=[]
        finalistas+=1
        apellido=raw_input("Ingrese el apellido: ")
        nombre=raw_input("Ingrese el primer nombre: ")
        edad=validar_edad(valida_numero(raw_input("Ingrese la edad (en años): ")))
        if not edad in dic_edades:
            dic_edades[edad]=1
        else:
            dic_edades[edad]+=1    
        competidores[num_inscripcion].append(apellido)
        competidores[num_inscripcion].append(nombre)
        total_edades+=edad
        genero=validar_genero(raw_input("Ingrese el género [M/F]: "))
        h_lar=valida_numero(raw_input("A continuacion ingrese el horario de largada\nIngrese la hora: "))
        m_lar=valida_numero(raw_input("Ingrese los minutos: "))
        s_lar=valida_numero(raw_input("Ingrese los segundos: "))
        h_lar,m_lar,s_lar=validar_hora(hic,mic,sic,h_lar,m_lar,s_lar)
        h_lleg=valida_numero(raw_input("A continuacion ingrese el horario de llegada\nIngrese la hora: "))
        m_lleg=valida_numero(raw_input("Ingrese los minutos: "))
        s_lleg=valida_numero(raw_input("Ingrese los segundos: "))
        h_lleg,m_lleg,s_lleg=validar_hora(h_lar+2,m_lar,s_lar,h_lleg,m_lleg,s_lleg)
        marca=calc_marca(h_lar,m_lar,s_lar,h_lleg,m_lleg,s_lleg)
        competidores[num_inscripcion].append(marca)
        if marca<menor_marca:
            menor_marca=marca
        print "\nDatos del competidor nº", num_inscripcion
        print "Apellido y nombre:", apellido,",", nombre
        print "Edad:", edad
        print "Genero:",genero
        print "Hora de largada:", h_lar,":",m_lar,":",s_lar
        print "Hora de llegada:", h_lleg,":",m_lleg,":",s_lleg
        print "Marca de tiempo:", marca[0],":",marca[1],":",marca[2]
        num_inscripcion=validar_inscripcion(valida_numero(raw_input("\nIngrese el número del competidor que finalizó el recorrido (o 0 para salir): ")))
    print "\nCantidad de competidores:",cant_competidores
    if finalistas==0:
        print "No hubo finalistas."
    else:
        print "El/los ganador/es de la competencia es/son: "
        for i in competidores:
            if menor_marca in competidores[i]:
                print "Competidor N°: ",i ,competidores[i][0], competidores[i][1]
        print "Menor marca registrada:",menor_marca[0],":",menor_marca[1],":",menor_marca[2]
        print "Porcentaje de competidores que terminaron el recorrido:", 100.0*finalistas/cant_competidores,"%"
        print "Promedio de edad de finalistas: ", 1.0*total_edades/finalistas
        for item in dic_edades:
            print "hubo", dic_edades[item], "corredor/es de ", item, "años"
