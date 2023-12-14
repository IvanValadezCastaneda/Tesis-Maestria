from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException 
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime

# Inicializar el navegador
driver = webdriver.Chrome()  # Asegúrate de tener el driver de Chrome instalado

# Abrir la página web
url = "https://articulo.mercadolibre.com.mx/MLM-2253779926-tableta-goodtel-g2-android-rom-de-64-gb-con-teclado-y-funda-_JM?quantity=1&variation_id=178574551221"
driver.get(url)
time.sleep(1)

url2 = "https://articulo.mercadolibre.com.mx/MLM-2253779926-tableta-goodtel-g2-android-rom-de-64-gb-con-teclado-y-funda-_JM?quantity=1&variation_id=178574551221"
driver.get(url)

time.sleep(1) 

# Obtener el tamaño de la ventana del navegador
window_size = driver.get_window_size()
window_height = window_size["height"]

while True:
    # Scroll hacia abajo
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)  # Esperar a que se carguen más elementos
    
    # Obtener posición actual del scroll
    current_scroll = driver.execute_script("return window.scrollY")
    # Si no hay más desplazamiento posible, salir del bucle
    if current_scroll + window_height >= driver.execute_script("return document.body.scrollHeight"):
        break

show_more_button = driver.find_element(By.XPATH, '//*[@id="reviews_capability_v3"]/div/section/div/div[2]/div[3]/button').click()

driver.switch_to.frame(driver.find_element(By.XPATH, '//*[@id="ui-pdp-iframe-reviews"]'))

for num_elemento in range(2, 7):  # Iterar desde 1 hasta 5 (ambos inclusive)
    try:
        xpath_boton = '//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[1]/div[2]/div/button'
        boton = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_boton)))
        boton.click()
    except NoSuchElementException:
        print("No se encontró el botón")

    time.sleep(2) 

    # Actualizar el número de elemento en el XPath del elemento
    xpath_elemento = f'//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[1]/div[2]/div[2]/ul/li[{num_elemento}]'

    try:
        elemento = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, xpath_elemento)))
        elemento.click()
    except NoSuchElementException:
        print("No se encontró el elemento")

    time.sleep(1) 

    while True:
        previous_height = driver.execute_script("return document.body.scrollHeight")
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
        time.sleep(1)
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == previous_height:
            break

    time.sleep(1)

    # Contar el número de elementos article
    elementos_article = driver.find_elements(By.XPATH, '//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[2]/div/div/div/article')

    for i, element_article in enumerate(elementos_article, start=1):
        
        xpath_calificacion = f'//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[2]/div/div/div/article[{i}]/div[1]/div/div/p'
        xpath_fecha = f'//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[2]/div/div/div/article[{i}]/div[1]/div/span'
        xpath_resena = f'//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[2]/div/div/div/article[{i}]/p'
        xpath_imagenes = f'//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[2]/div/div/div/article[{i}]/div[2]/section/div[2]/div'

        hay_imagenes = True
        
        if hay_imagenes :
            x = 3
        else:
            x = 2

        xpath_utilidad = f'//*[@id="reviews-capability.desktop"]/section/div/div[2]/div[2]/div[2]/div/div/div/article[{i}]/div[{x}]/div[1]/button[1]/span/p'

        element_calificacion = driver.find_element(By.XPATH, xpath_calificacion)
        element_fecha = driver.find_element(By.XPATH, xpath_fecha)
        element_resena = driver.find_element(By.XPATH, xpath_resena)
        element_utilidad = driver.find_element(By.XPATH, xpath_utilidad)
        
        calificacion_text = element_calificacion.text
        fecha_text = element_fecha.text
        resena = element_resena.text
        utilidad =  element_utilidad.text

        # Procesar la cadena para extraer el número de calificación
        calificacion_numero = calificacion_text.split()[1]  # Obtener el segundo elemento (el número) de la cadena dividida por espacios
    
        print(f"Elemento {i}")
        print("Calificación: ", calificacion_numero)
        print("Fecha:", fecha_text)
        print("Reseña:", resena)
        print("Utilidad:", utilidad)
        print()

    time.sleep(1)

# Cerrar el controlador de Selenium
driver.quit()

