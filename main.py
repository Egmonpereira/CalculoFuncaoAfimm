import os

def conversor(n):
    a = ""
    aux = 0
    for i in n:
        if i == "/":
            b = int(n[aux + 1])
            break
        else:
            a = (a + i)
        aux = aux + 1
    try:
        return int(a)/int(b)
    except:
        return int(n)


if __name__ == "__main__":
    os.system("clear")
    n = input('Coeficiente de X: ')
    cx = conversor(n)
    n = input('Valor de X: ')
    x = conversor(n)
    n = input('Coeficiente de Y: ')
    cy = conversor(n)
    n = input('Valor de Y: ')
    y = conversor(n)


    
    print(cx * x + cy * y)
