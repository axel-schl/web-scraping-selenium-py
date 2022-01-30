# web-scraping-selenium-py

## Resumen
Script para realizar web-scraping de metadata de series y películas de **https://www.starz.com/ar/es**.

![img](https://i.imgur.com/vXIk7w9.png)
## Tecnologías Utilizadas
* [Selenium](https://www.selenium.dev/selenium/docs/api/py/index.html): The selenium package is used to automate web browser interaction from Python..
* [Pandas](https://pandas.pydata.org/docs/): pandas is an open source, BSD-licensed library providing high-performance, easy-to-use data structures and data analysis tools for the Python programming language.


## Instalación
* Se debe tener Python instalado globalmente en tu sistema. Sí no lo tienes: [aquí](https://www.python.org").
* También debes tener instalado virtualenv para crear el entorno virtual. En caso contrario, ejecuta en la terminal:
    ```bash
        $ pip install virtualenv
    ```
* Luego clona el repositorio:
    ```bash
        $ git clone https://github.com/axel-schl/web-scrapping-selenium-py.git
    ```

* #### Dependencias
    1. Cd el repositorio clonado:
        ```bash
            $ cd web-scrapping-selenium-py
        ```
    2. Crea y activa el entorno virtual:
        ```bash
            $ virtualenv  venv -p python3
            $ source venv/bin/activate
        ```
    3. Instala los requerimientos:
        ```bash
            $ pip install -r requirements.txt
        ```
        
    El ejecutable chromedriver.exe es necesario para la navegación interactiva de Selenium mediante Chrome. El .exe que se encuentra
    en este repositorio es compatible para la versión **97.0** de Chrome para Windows.
    De tener otros requerimientos descargar el driver correspondiente en: **https://chromedriver.chromium.org/downloads**
   

* #### Ejecuta el script y a scrapear!

    Ejecuta el scrapper:
    ```bash
        $ python scrap.py 
    ```
    Por defecto el scraper extraerá metadata de las urls: **https://www.starz.com/ar/es/view-all/blocks/1523534** para películas
    y **https://www.starz.com/ar/es/view-all/blocks/1523514** para series.
    
    Se puede enviar las urls a scrapear como argumentos al main de scrap.py en caso de que las rutas se hayan modificado o se busque extraer la información de otra sección. 
    El script tomará el primer arg como la url de las películas y el segundo como la url de las series. Por ejemplo :
    ```bash
        $ python scrap.py https://www.starz.com/ar/es/view-all/blocks/1523536 https://www.starz.com/ar/es/view-all/blocks/1523517
    ```
    Con ese comando sólo obtendremos la info de las películas de acción y las series de época (urls de Enero de 2022)
   
    
    
   
    
 * #### Resultados
  
 En este mismo repositorio se puede encontrar los resultados de toda la información extraída de las peliculas y series del sitio(Enero 2021) luego de ejecutar el script.
 
 * Películas: starz_peliculas.csv
 * Series: starz_series.csv
 
 También estan disponibles  algunas visualizaciones básicas con *pandas* y *seaborn* de los resultados en *Jupyter Notebook* en **visualizacion.ipynb**


**Muchas gracias por visitar mi repositorio!**
