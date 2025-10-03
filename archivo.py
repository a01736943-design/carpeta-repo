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

#hellp
print("hello")      
print("h")

# --- IGNORE ---
def generar_datos_ventas ():
    dias= ["Lunes", "Martes", "Miércoles", "Jueves", "Viernes", "Sábado", "Domingo"]
    ventas= [150, 200, 250, 300, 350, 400, 450]
    return dias, ventas
    return datos_ventas
def resumen_analitica():
    dias, ventas= generar_datos_ventas()
    total= sum(ventas)
    promedio= total/ len(ventas)
    return{
        "dias": dias,
        "ventas": ventas,
        "total": total,
        "promedio": promedio
    }
datos=resumen_analitica()
print(datos["total"])
print(datos["promedio"])

