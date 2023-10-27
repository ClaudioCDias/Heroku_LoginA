# 1 - Bibliotecas
from selenium.webdriver.common.by import By

# 2 - Classe

class LoginPage():
   # 2.1 - Mapeamento dos Elementos da Página
   _username_input = {'by': By.ID, 'value': 'username'}
   _password_input = {'by': By.ID, 'value': 'password'}
   _login_button = {'by': By.CSS_SELECTOR, 'valor': 'button.radius'}

 # 2.2 - Inicializador / Construtor (Java)
   def __init__(self):
      self.driver.get('https://the-internet.herokuapp.com/login')

 # 2.3 - Ações Realizáveis
