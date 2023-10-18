import random
opcion = 1
intentos = 3
departamentos = {}

def agregarDepartamentos(): 
    departamentos["Amazonas"]="Leticia"
    departamentos["Antioquia"]="Medellín"
    departamentos["Boyaca"]="Tunja"
    departamentos["Caldas"]="Manizales"
    departamentos["Cundinamarca"]="Bogotá"
    departamentos["Tolima"]="Ibagué"
    departamentos["Valle del Cauca"]="Cali"
    
departamentos1=['Amazonas','Antioquia','Boyaca','Caldas','Cundinamarca','Tolima','Valle del Cauca']
num = random.randint(0, 6)
departamento=departamentos1[num]  

if __name__=="__main__": 
    agregarDepartamentos()
    print("Ingrese la capital correcta del departamento dado para ganar. Ingrese 'Salir' para terminar el programa.")
    while opcion ==1 or opcion == 2 or opcion == 3 or opcion == 4 :
        if opcion == 1:
            intentos = intentos-1
            respuesta=input(f"Capital de {departamento}: ")
            if respuesta in departamentos.values():
                opcion = 2
            
            if respuesta == "Salir" or respuesta == "salir":
                break
            
            if intentos == 0:
                print("Hasta luego, sigue intentando en otra oportunidad.")
                break
        elif opcion == 2:
            print("Correcto")
            break