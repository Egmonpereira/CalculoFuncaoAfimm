import os 

if __name__ == "__main__":
    os.system("clear")
    x = int(input(Valor de X: ))
    y = int(input(Valor de Y: ))
    
    cx = int(input(Coeficiente de X: ))
    cy = int(input(Coeficiente de Y: ))
    
    print(cx * x + cy * y)
