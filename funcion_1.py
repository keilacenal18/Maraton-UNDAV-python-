def validar_hora(h1,m1,s1,h2,m2,s2):
    '''recibe 6 valores por parametro. comprueba que sean horarios reales
    caso contrario, pide el reingreso del valor erroneo. en el segundo
    ciclo verifica los datos de h2, m2 y s2 para devolver los valores correctos
    a la funcion principal.'''
    while h2>23 or m2>59 or s2>59:
            h2=(input("hora erronea. reingrese: "))
            m2=(input("minutos erroneos. reingrese: "))
            s2=(input("segundos erroneos. reingrese: "))
    while (h1==h2 and m1==m2 and s1>s2) or (h1==h2 and m1>m2) or (h1>h2):
            h2=input("Reingrese la hora: ")
            m2=input("Reingrese los minutos: ")
            s2=input("Reingrese los segundos: ")
    return h2,m2,s2
