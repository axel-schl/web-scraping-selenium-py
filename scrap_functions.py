from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.support import expected_conditions as EC
import time
from auxiliar import get_links, get_ep_links


def peliscrap(driver,url):
  '''Función que recibe el objeto WebDriver y la url a scrapear, y retorna una lista
  con la metadata de cada película'''
  
  print('Comienza la extracción de datos de películas')
  links = get_links(driver,url)

  metadata = [] #Lista donde se irá agregando la metadata de cada película
  contador = 0 # Se incializa contador para la cantidad de películas de las que se extrajo info

  for link in links: 
      driver.get(link)
      time.sleep(3) #Espera para la carga de la página

      #Clickear botón "Ver más" para obtener la sinopsis completa

      try: 
          driver.find_element(By.CLASS_NAME, 'more-link').click() 
      except:
          pass


      titulo = driver.find_element(By.CLASS_NAME, 'movie-title').text.replace('Ver ', '').replace(' online', '')
      sinopsis = driver.find_element(By.CLASS_NAME, 'logline').find_element(By.TAG_NAME, 'p').text.strip()
      ul = driver.find_element(By.XPATH, '//ul[@class="meta-list text-uppercase"]') #contenedor de la metadata
      items = ul.find_elements(By.TAG_NAME, 'li') # elementos de la metadata
    
      calificacion = items[0].text.strip()
      duracion_min = int(items[1].text.strip().lower().replace('min', ''))
      genero = items[2].text.strip()
      anio = int(items[3].text.strip())
      sonido = items[4].text.strip()
    
   
      metadata.append({"Titulo": titulo, 
      "Sinopsis": sinopsis,
      "Año": anio,
      "Duracion(min)": duracion_min,
      "Calificacion": calificacion,
      "Genero": genero,
      "Sonido": sonido})
    
      contador +=1

      if contador%25 == 0:
        print(f'Paciencia! ya se ha recoletado la información de {contador} películas.')


  print (f'Se extrajo exitosamente metadata de {contador} películas')
  return metadata



def seriescrap(driver,url):
  '''Función que recibe el objeto WebDriver y la url a scrapear, y retorna una lista
  con la metadata de cada serie'''
  
  print('Comienza la extracción de datos de series')
  links = get_links(driver,url)

  metadata = [] #Lista donde se irá agregando la metadata de cada película
  contador = 0 # Se incializa contador para la cantidad de películas de las que se extrajo info

  for link in links: 
      driver.get(link)
      time.sleep(3) #Espera para la carga de la página

      #Clickear botón "Ver más" para obtener la sinopsis completa

      try: 
          driver.find_element(By.CLASS_NAME, 'more-link').click() 
      except:
          pass


      titulo = driver.find_element(By.ID, 'seriesDetailsH1').text.strip()
      sinopsis = driver.find_element(By.CLASS_NAME, 'logline').find_element(By.TAG_NAME, 'p').text.strip()
      ul = driver.find_element(By.XPATH, '//ul[@class="meta-list text-uppercase"]') #contenedor de la metadata
      items = ul.find_elements(By.TAG_NAME, 'li') # elementos de la metadata
    
      calificacion = items[0].text.strip()
      episodios = int(items[1].text.strip().replace('EPISODIOS', ''))
      genero = items[2].text.strip()
      anio = items[3].text.strip()
      
      temporadas =  driver.find_elements(By.CLASS_NAME, 'season-number') 
      temp_links = [temp.find_element(By.TAG_NAME,'a').get_attribute('href') for temp in temporadas] #Link de cada temporada
      
      ''' la info de cada episodio se guardará en formato lista de diccionarios
      para ser disponible en caso de requerir ser consultada, sin duplicar info de cada serie'''
      ep_data = [] #lista donde se guardará la metadata de cada episodio
      contador_temporada = 0 #variable que servirá como metadata de n°temporada del episodio
      for temp in temp_links:
        contador_temporada += 1 
        driver.get(temp)
        
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);") 
        
        ep_links = get_ep_links(driver)
        
        for ep_link in ep_links: 
            driver.get(ep_link)
            
            try: 
                driver.find_element(By.CLASS_NAME,'more-link').click() 
                time.sleep(3)
            except:
                pass

           
            ep_titulo = wait(driver, 15).until(EC.presence_of_element_located((By.CLASS_NAME, 'episode-title'))).text.strip()
            

            if 'tráiler' not in ep_titulo.lower(): #no se extrae info de los tráilers

              ep_sinopsis = driver.find_element(By.CLASS_NAME, 'logline').find_element(By.TAG_NAME,'p').text.strip()
              ul = driver.find_element(By.XPATH, '//ul[@class="meta-list text-uppercase"]') #contenedor de la metadata
              items = ul.find_elements(By.TAG_NAME, 'li') # elementos de la metadata
    
              ep_calificacion = items[0].text.strip()
              ep_duracion_min = int(items[1].text.strip().lower().replace('min', ''))
              ep_anio = int(items[2].text.strip())

              if len(items)>3: #se verifica que el episodio contenga info del sonido
                ep_sonido = items[3].text.strip()
              else:
                ep_sonido = None
                
              ep_data.append({"Titulo": ep_titulo,
              "Sinopsis": ep_sinopsis,
              "Temporada": contador_temporada,
              "Año": ep_anio,
              "Duracion(min)": ep_duracion_min,
              "Calificacion": ep_calificacion,
              "Sonido": ep_sonido})
            
            else:
              pass
             
           
      metadata.append({"Titulo": titulo, 
      "Sinopsis": sinopsis,
      "Año": anio,
      "Episodios": episodios,
      "Calificacion": calificacion,
      "Genero": genero,
      "Temporadas" : contador_temporada,
      "info_episodios" : ep_data})
    
      contador +=1

      if contador%25 == 0:
        print(f'Paciencia! ya se ha recoletado la información de {contador} series.')


  print (f'Se extrajo exitosamente metadata de {contador} series')
  return metadata