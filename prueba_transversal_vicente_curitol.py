#productos = {modelo: [marca, pantalla, RAM, disco, GB de DD, Procesador, video]}

productos = {"8475HD": ["HP", 15.6, "8GB", "DD", "1T", "Intel core i5", "Nvidia GTX1050"],
             "2175HD": ["Acer", 14, "4GB", "SSD","512GB", "Intel core i5", "Nvidia GTX1050"],
             "JjfFHD": ["Asus", 14, "16GB", "SSD","256GB", "Intel core i7", "Nvidia RTX2080Ti"],
             "UWU131HD": ["Dell", 15.6, "8GB", "DD","1T", "AMD Ryzen 3", "Nvidia GTX1050"]
             }

#stock = {modelo: [precio, stock],}

stock = {"8475HD": [387990, 10],
        "2175HD": [327990, 4],
        "JjfFHD": [424990, 1],
        "UWU131HD": [349990, 1]
        }
def buscar_marca(marca:str):
    for i in productos:
        #print(productos[i][0])
        if productos[i][0].upper() == marca.upper():
            return i
        else:
            return None

#print(buscar_marca("hp"))


def buscar_stock_marca(marca:str):
    for i in stock:
        #print(stock[i][1])
        if i == buscar_marca(marca):
            return stock[i][1]
        else:
            return None
    


#print(buscar_stock_marca("hp"))

def validar_texto(texto:str):
    if len(texto.strip()) != 0:
        return texto
    print("El texto no debe de estar vacio")

#print(validar_texto("miau"))

def validar_numero_entero_positivo(numero:int):
    while True:
        try:
            if numero <= 0:
                print("el numero no puede ser negatico o igual a 0")
            else:
                return numero
        except ValueError:
            print("debe ingresar un numero entero positivo")
        
        

#print(validar_numero_entero_positivo("miau"))


def busqueda_precio(p_min:int, p_max:int):
    validar_numero_entero_positivo(p_min)
    validar_numero_entero_positivo(p_max)
    if p_min >= p_max:
        print("el rango minimo no puede ser mayor o igual al rango positivo")
    else:
        for i in stock:
            if stock[i][0] < p_min and stock > p_max:
                return None
            else:
                return stock[i][0] >= p_min and stock <= p_max
            
#print(busqueda_precio(320000, 390000))

def buscar_por_codigo(codigo:str):
    for i in productos:
        if productos[i] == codigo:
            return codigo

def menu():
    while True:    
        print("****MENU PRINCIPAL****")
        print("[1] -- Stock marca")
        print("[2] -- Busqueda por precio")
        print("[3] -- Eliminar Producto")
        print("[4] -- Salir")    
        op = int(input("ingrese un opcion: "))
        validar_numero_entero_positivo(op)
        if op == 1:
            while True:
                marca = input("ingrese marca a consultar: ")
                validar_texto(marca)
                if buscar_stock_marca(marca) == None:
                    print("La marca no esta registrada, vuelva a intentarlo")
                    continue
                else:
                    print(f"el stock es: {buscar_stock_marca(marca)}")
                    break
        elif op == 2:
            p_min = int(input("ingrese el limite inferior: "))
            p_max = int(input("ingrese el limite superior: "))
            if busqueda_precio(p_min, p_max) != None:
                buscar_marca (busqueda_precio)
        elif op == 3:
            modelo_actualizar = input("ingrese el modelo a actualizar: ")
            if buscar_por_codigo(modelo_actualizar) == None:
                print("el producto no existe")
            else:
                productos.remove(modelo_actualizar)
                opcion_adicional = input("desea eliminar otro[si] [no]: ")
                validar_texto(opcion_adicional)
                if opcion_adicional == "si":
                    continue
                else:
                    break
        elif op == 4:
            print("hasta luego...")
            break
        else:
            print("opcion no valida, debe ingresar entre la opcion 1 al 4")


menu()
