print("hola")

print("mundo")

for i in range (8):
    print(i)

a=2
b=3
c=5

def suma():
    print("suma", a+b+c)
suma()

import matplotlib.pyplot as plt

def graficar_ventas(dia, ventas):
    plt.figure(figsize=(8,4))
    plt.plot(dia, ventas, marker="o", linestyle="-", color="blue")
    plt.title("ventas diarias")
    plt.xlabel("dia")
    plt.ylabel("ventas")
    plt.grid(True)
    plt.show()
def main_fronland():
    dias=["lun", "m","mi", "jue", "vier"]
    ventas=[120,23,43,65,42]
    graficar_ventas(dias,ventas)
main_fronland()


print("fin del programa")
print("fin del programa")
print("fin del programa")               