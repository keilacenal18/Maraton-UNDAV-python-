# -*- coding: cp1252 -*-

def validar_genero(genero):
    '''toma por parametro un valor del tipo cadena y valida entre
    Masculino y Femenino en el formato (M) o (F) excluyente. Caso contrario
    pide el reingreso del valor y lo devuelve a la funcion principal'''
    while genero!="M" and genero!="F":
        genero=raw_input("Vuelva a ingresar el genero: ")
    return genero

def convert_seg_hms(seg):
    """La funcion convert_seg_hms toma por parametro un valor, el cual
    corresponde a los segundos que componen el horario. Los calcula
    y devuelve su resultado en horas, minutos y segundos"""
    h=seg/3600
    m=((seg-(h*3600))/60)
    s=seg-(h*3600+m*60)
    return h,m,s
def convert_hms_seg(h,m,s):
    '''La funcion convert_hms_seg toma por parametro 3 valores, los cuales
    corresponden a las horas, los minutos y segundos. Los calcula y
    devuelve su resultado en segundos'''
    total_seg=h*3600+m*60+s
    return total_seg

def validar_edad (num1):
    '''La funcion valida_edad recibe por parametro un numero, que representa la
    edad del participante, lo compara con los valores 18 y 65 para estar dentro
    de los mismos. De ser afirmativo devulve el num, caso contrario solicita
    su reingreso.'''
    while num1<18 or num1>65:
        num1=raw_input("La edad debe estar comprendida entre los 18 y 65 años.\nVuelva a ingresar la edad: ")
    return num1
