from selenium import webdriver
from time import sleep
import pyper
import pyautoguiq


# objeto com os comandos a ser executado
class firefoxAuto:
    # abre o firefoxpip
    def __init__(self):
        self.firefox = webdriver.Firefox()

        self.firefox.get('https://www.messenger.com/login/')

    def faz_login(self):
        try:
            clicar_login = self.firefox.find_element_by_id('email')
            clicar_senha = self.firefox.find_element_by_id('pass')
            btm_entra = self.firefox.find_element_by_id('loginbutton')
            sleep(5)
            clicar_login.send_keys('email')
            sleep(1)
            clicar_senha.send_keys('senha')
            sleep(1)
            btm_entra.click()
        except Exception as e:
            print('erro ao fazer login', e)

    def acessar_perfil(self):
        try:
            sleep(5)
            input_nome_user = self.firefox.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div/div/div/label/input')
            input_nome_user.click()
            nome = 'nome' #nome da pessoa que deseja enviar mensagem
            pyperclip.copy(nome)
            sleep(3)
            pyautogui.hotkey('ctrl', 'v')
            sleep(5)
            nome_user = self.firefox.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div/div[1]/ul/li[1]/ul/li[2]/div/a/div/div[2]/div/div/span/span/span')
            nome_user.click()
        except Exception as e:
            print('Erro ao clicar no perfil', e)

    def enviar_mensager(self, n):
        try:
            mensagem = f'tede de automação, mensagem de número {n}'
            pyperclip.copy(mensagem)
            pyautogui.hotkey('ctrl', 'v')
            btn_enviar = self.firefox.find_element_by_css_selector(
                'span.tojvnm2t:nth-child(4) > div:nth-child(1) > svg:nth-child(1) > path:nth-child(1)')
            sleep(1)
            btn_enviar.click()

        except Exception as e:
            print('Erro ao enviar a mensagem', e)

    def sair(self):
        self.firefox.quit()

    def arquivar(self):
        try:
            sleep(5)
            pyautogui.click(295, 321)
            sleep(5)
            pyautogui.click(295, 321)
            sleep(5)
            pyautogui.click(201, 624)
            sleep(5)
        except Exception as e:
            print('erro ao arquivar', e)


firefox = firefoxAuto()
firefox.faz_login()
sleep(15)
for n in range(40):
    firefox.arquivar()

firefox.sair()
