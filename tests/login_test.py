# import os
import time
import pytest
from pages import login_page

@pytest.fixture
def login(driver): # deixou de receber o request e recebe diretamente driver
    return login_page.LoginPage(driver) # instanciando a classe LoginPage e passando o Selenium

    # Como eram os passos do jeito simples
'''
def old_login_valido(driver):
    driver.get('https://the-internet.herokuapp.com/login')
    driver.find_element(By.ID, 'username').send_keys('tomsmith')
    driver.find_element(By.ID, 'password').send_keys('SuperSecretPassword!')
    driver.find_element(By.CSS_SELECTOR, 'button.radius').click()
    assert driver.find_element(By.CSS_SELECTOR, 'div.flash.success').is_displayed()
'''
def testar_login_com_sucesso(login):
    # preencher o usuário, a senha e clicar no botão
    login.com_('tomsmith', 'SuperSecretPassword!')
    # validar a mensagem
    assert login.vejo_mensagem_de_sucesso()
    time.sleep(2)

def testar_login_com_usuario_invalido(login):
    # preencher o usuário, a senha e clicar no botão
    login.com_('asdfgasdfg', 'SuperSecretPassword!')
    # validar a mensagem
    assert login.vejo_mensagem_de_falha()
    time.sleep(2)

def testar_login_com_senha_invalida(login):
    # preencher o usuário, a senha e clicar no botão
    login.com_('tomsmith', 'xpto12345')
    # validar a mensagem
    assert login.vejo_mensagem_de_falha()
    time.sleep(2)