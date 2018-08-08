# -*- coding: cp1252 -*-
from funciones_3 import convert_seg_hms, convert_hms_seg
def calc_marca (h_lar,m_lar,s_lar,h_lleg,m_lleg,s_lleg):
    '''toma por parametro los valores ingresados en la funcion principal,
    invoca a la funcion del modulo Echegaray y realiza la resta entre los
    dos horarios para luego devolver el valor de la diferencia en la funcion
    principal'''
    larg_s=convert_hms_seg(h_lar,m_lar,s_lar)
    lleg_s=convert_hms_seg(h_lleg,m_lleg,s_lleg)
    marca=lleg_s-larg_s
    marca=convert_seg_hms(marca)    
    return marca

def validar_inscripcion(num):
    '''recibe por parametro un numero, realiza
    la comprobacion de que este sea postivo. De ser 0 pide confirmar
    dato. de ser negativo o no confirmarlo solicita su reingreso 
    y devuelve el numero confirmado a la funcion principal'''
    while num<=0:
        if num==0:
            rta=(raw_input("Desea confirmar el dato? [S/N]: "))
            if rta=="S":
                return num
            elif rta=="N":
                num=(input("Ingrese nuevamente el número de competidor: " ))
        elif num<0:
            num=(input("El numero no puede ser negativo. reingreselo: "))
    return num

def valida_numero (x):
    """ Recibe por parámetro un dato. Corrobora que sea numérico y en el caso de
    que no lo sea pide reingreso hasta que sea un número. Devuelve el número
    a la función principal"""
    while True:
        try:
            x=int(x)
        except ValueError:
            print "No ingresó un numero."
            x=raw_input("Por favor vuelva a ingresarlo: ")
        else:
            return x
