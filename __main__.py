
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

def list_files_in_directory(directory):
    
    while True:
    
      try:
          # List all files in the specified directory
          file_list = os.listdir(directory)
          
          # Iterate through the list and print each file name
          for file_name in file_list:
              print(file_name)
      
      except FileNotFoundError:
          print(f"The directory '{directory}' was not found.")
      except PermissionError:
          print(f"Permission denied while accessing '{directory}'.")


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
       return dict_menu.get(int(seleccion))[1]()
     
     except ValueError:
       print ("Ingrese una opcion valida.")
       print("Menu:")
       for value in dict_menu.values():
          print(value[0])

     except TypeError:
       print("Ingrese una opcion valida.")
       for value in dict_menu.values():
          print(value[0])

def busqueda_mes():

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
      
      solicitar_ruta()

      list_files_in_directory(solicitar_ruta())

      file_path = input("Ingrese la ruta del archivo: \n")

      if os.path.isabs(file_path) and os.path.exists(file_path):
          print(f"Ruta ingresada correctamente: {file_path}")
          break
      
      else:
          print("Ruta invalida, intentelo nuevamente: ")

  
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