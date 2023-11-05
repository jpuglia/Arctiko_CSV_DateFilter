
from sys import exit
import csv
import os


def solicitar_ruta():
   while True:
      
      path_directory = input('Ingrese la ruta de la carpeta: \n')

      if os.path.exists(path_directory) is True:
         return path_directory
      
      else:
         print('Ruta erronea, intente nuevamente.')

def list_files_in_directory(path_directory):
        
    while True:
    
      try:
          # List all files in the specified directory
          file_list = os.listdir(path_directory)
          file_list = [archivo for archivo in file_list if archivo.endswith(".txt")]

          enum = []

          i = 0

          for item in file_list:
             enum.append(i)
             i += 1

          file_list_dict = {enum : file_list for enum, file_list in zip(enum, file_list)}

          for index, archivo in file_list_dict.items():
            print(index, ' - ',archivo)

          
          return file_list_dict

      except FileNotFoundError:
          print(f"La carpeta '{path_directory}' no fue encontrada.")
      except PermissionError:
          print(f"No se tiene permiso para acceder a la carpeta: '{path_directory}'.")


def main():

  dict_menu = {
    
    1:("1. Busqueda por mes", busqueda_mes),
    2:("2. Salir", exit)
    
    }
  
  print("Menu:")
  for value in dict_menu.values():
    print(value[0])

  while True:
     
     seleccion =input("Selecciona una opcion: \n")

     try:
       print("Ha seleccionado:", dict_menu.get(int(seleccion))[0])
       dict_menu.get(int(seleccion))[1]()
     
     except ValueError:
       print ("Ingrese una opcion valida.")
       main()

     except TypeError:
       print("Ingrese una opcion valida.")
       main()
       

def busqueda_mes():
  
  dir_path = solicitar_ruta()

  dir_list = list_files_in_directory(dir_path)

  meses = {
     "01":"Enero",
     "02":"Febrero",
     "03":"Marzo",
     "04":"Abril",
     "05":"Mayo",
     "06":"Junio",
     "07":"Julio",
     "08":"Agosto",
     "09":"Setiembre",
     "10":"Octubre",
     "11":"Noviembre",
     "12":"Enero"
  }

  while True:
     nom_file = input('Seleccione el numero del archivo que desea abrir: \n')

     try:
        file_path = "\\".join([dir_path, dir_list.get(float(nom_file))])
        print(file_path)
        break      

     except ValueError:
        print('Seleccione un valor dentro del listado')

     except KeyError: 
        print('Ingrese un valor valido')

     except TypeError:
        print('Ingrese un valor valido')

  
  mes_deseado = input("Introduce el mes (formato mm): \n")
  equipo = input("Introduce el codigo del equipo: \n")

  archivo_salida = f' {meses.get(mes_deseado)}_{equipo}.txt'

  filas_seleccionadas = []

  with open(file_path, "r", newline= '') as entrada, open(archivo_salida,'w', newline='') as salida:
    lector_txt = csv.reader(entrada, delimiter = "\t")
    escritor_txt = csv.writer(salida, delimiter= "\t")

    next(lector_txt)

    segunda_fila = next(lector_txt)
    escritor_txt.writerow(segunda_fila)

    tercera_fila = next(lector_txt)
    escritor_txt.writerow(tercera_fila)

    for fila in lector_txt:
          
          fecha_hora = fila[2]
          
          if fecha_hora[5:7] == mes_deseado:
            filas_seleccionadas.append(fila)
      
    escritor_txt.writerows(filas_seleccionadas)

    print('Su archivo fue procesado con exito, lo encontrara en la carpeta de condiciones ambientales')

    salida()




def salida():

  while True:
  
    opcion = input("Gracias por utilizar el programa. Desea realizar una nueva busqueda? (y/n)\n")

    if opcion == "y":
      main()
      break

    elif opcion == "n":
      exit()

    else:
      print("Escriba 'y' o 'n'\n")




if __name__ == "__main__":
   main()