from selenium.webdriver.support.ui import WebDriverWait as wait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import time


def get_links(driver,url):
  '''Función auxiliar que recibe el objeto Webdriver y la url a scrapear, y retorna
  una lista con los links de cada película/serie'''
  driver.get(url)
  time.sleep(2) 
  driver.maximize_window()
  driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

  lista = wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-title'))) #peliculas/series cargadas
  while True:
    driver.execute_script('arguments[0].scrollIntoView();', lista[-1]) #se scrollea hasta el último elemento
    
    try:
        # Espera
        wait(driver, 15).until(lambda driver: len(wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-title'))) > len(lista)))
        # Actualiza lista con los nuevos elementos cargados
        lista = wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'content-title')))
    except:
        # Rompe el loop sí ya no hay nuevos elementos
        break
  
  virtual_scroller = driver.find_element(By.TAG_NAME, 'virtual-scroller') 
  titulos = virtual_scroller.find_elements(By.CLASS_NAME, 'content-title') #Todas las peliculas/series ya cargadas


  '''Se obtienen los links(href) de cada película/serie'''
  links = [] 
  for titulo in titulos: 
    link = titulo.find_element(By.TAG_NAME, 'a').get_attribute('href')
    if link not in links: # verifica que no se repitan peliculas/series
        links.append(link)
  
  return links

def get_ep_links(driver):
    '''Función auxiliar que recibe el objeto Webdriver, y retorna
    una lista con los links de cada episodio de la serie'''
 
    lista = wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'episode-link'))) #episodios cargados
    while True:
      driver.execute_script('arguments[0].scrollIntoView();', lista[-1]) #se scrollea hasta el último elemento
    
      try:
        # Espera
        wait(driver, 15).until(lambda driver: len(wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'episode-link'))) > len(lista)))
        # Actualiza lista con los nuevos elementos cargados
        lista = wait(driver, 15).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'episode-link')))
      except:
        # Rompe el loop sí ya no hay nuevos elementos
        break
  
    


    '''Se obtienen los links(href) de cada episodio'''
    links = [] 
    for element in lista: 
      ''' los href de cada episodio llevan al sitio en ingles, se debe
      completar con /ar/es para seguir scrapeando el sitio en cuestión'''
      false_link = element.get_attribute('href')
      index = false_link.find('/series')
      link = false_link[:index] + '/ar/es' + false_link[index:]
            
      if link not in links: # verifica que no se repitan episodios
        links.append(link)
  
    return links
    