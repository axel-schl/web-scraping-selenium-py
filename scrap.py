from selenium import webdriver
import pandas as pd
import sys 
from scrap_functions import peliscrap, seriescrap

'''EJECUTAR DESDE LA TERMINAL: python scrap.py url1 url2
con url1: url de películas, url2: url de series. 
Se puede ejecutar simplemente python scrap.py y se utilizarán las urls por defecto'''

def main():
   
    '''scrap de peliculas'''

    # si el usuario no ingresa 1er url, se usa el por defecto
    if len(sys.argv)>1:
       url = sys.argv[1]
    else:
        url = 'https://www.starz.com/ar/es/view-all/blocks/1523534'
    
    driver = webdriver.Chrome('./chromedriver')
    metadata_p = peliscrap(driver,url)

    path_peliculas = './starz_peliculas.csv'
    
    try:
        df_pelis = pd.DataFrame(metadata_p) #Dataframe con la metadata para crear el .csv final
        df_pelis.to_csv(path_peliculas, columns=["Titulo", "Sinopsis", "Año", "Duracion(min)", "Calificacion", "Genero", "Sonido"],encoding='utf8', index= False) 

        print(f'Los datos fueron guardados exitosamente como: {path_peliculas}')

    except Exception as e:
        print(f'Hubo un error en la descarga de los datos: {e}')

    '''scrap de series'''

    # si el usuario no ingresa 2do url, se usa el por defecto
    if len(sys.argv)>2:
        url = sys.argv[2]
    else:
        url = 'https://www.starz.com/ar/es/view-all/blocks/1523514'
    
    
    metadata_s = seriescrap(driver,url)

    path_series = './starz_series.csv'
    
    driver.close()
      
    try:
        df_series = pd.DataFrame(metadata_s) #Dataframe con la metadata para crear el .csv final
        df_series.to_csv(path_series, columns=["Titulo", "Sinopsis", "Año", "Episodios", "Calificacion", "Genero", "Temporadas", "info_episodios"],encoding='utf8', index= False) 

        print(f'Los datos fueron guardados exitosamente como: {path_series}')

    except Exception as e:
        print(f'Hubo un error en la descarga de los datos: {e}')


if __name__ == "__main__":
    main()















