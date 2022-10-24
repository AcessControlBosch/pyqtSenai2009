##################### IMPORTANDO AS BIBLIOTECAS E FUNÇÕES ################################
import sys
import datetime
import requests
from datetime import datetime
import time
from time import sleep
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QAbstractItemView, QPushButton, QLabel, QLineEdit, QTableWidget
from PyQt5.QtGui import QIcon, QPixmap

import sqlite3

"""banco = sqlite3.connect("Banco.db")
cursor = banco.cursor()"""

"""""
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)
led_vermelha = 12
led_verde = 16
GPIO.setup(led_verde, GPIO.OUT)
GPIO.setup(led_vermelha, GPIO.OUT)

GPIO.output(led_verde, False)
GPIO.output(led_vermelha, True)
"""""

##################### IMPORTANDO AS CLASSES DOS ARQUIVOS DE TELAS ################################
from Menu01 import Ui_Menu01
from Menu01Aprendiz import Ui_Menu01Aprendiz
from Menu02 import Ui_Menu02
from Caderno_Verde_Atencao import Ui_Atencao
from Liberação_Segurança import Ui_Liberacao_Seguranca
from Liberação_Meio_Ambiente import Ui_Liberacao_Meio_Ambiente
from Documentos_Menu import Ui_documentos_menu
from Documentos_Documentos_de_pecas_menuu import Ui_documentos_documentos_de_pecas_menu
from documentos_documentos_de_pecas_1 import Ui_peca01
from documentos_documentos_de_pecas_2 import Ui_peca02
from documentos_documentos_de_pecas_3 import  Ui_peca03
from documentos_diagrama_eletrico_imagens import  Ui_documentos_diagrama_eletrico
from Documentos_mapa_de_risco import Ui_mapa_de_riscos
from Aviso_liberacao import Ui_Aviso_Liberacao
from Interface_didatica_menu import Ui_interface_didatica_menu
from Interface_didatica_menu_botoes_botoeira import Ui_interface_didatica_menu_botoes
from Interface_didatica_finalidade import  Ui_interface_didatica_finalidade
from Interface_didatica_menu_botao_emergencia import Ui_interface_didatica_menu_botao_emergencia
from Registros_menu import Ui_Registros_menu
from Cadastros_menu import Ui_cadastros_menu
from Cadastros_menu_adicionar import Ui_cadastros_classes
from Cadastros_adicionar_ficha01 import Ui_cadastros_adicionar_ficha01
from Usuario_registrado import Ui_Usuario_registrado
from Editar_cadastro import Ui_Editar_cadastro
from aproxime_cracha import Ui_Aproxime_cartao
from Registros_historico_utilizacao import Ui_cadastros_historico_utilizacao
from standby import Ui_Standby
from Menu01_skill2 import Ui_Menu01_skill2
from Relatos_liberacao import Ui_Relatos_liberacao
from leitor import Ui_leitor

colaborador = "Dorigon" #cursor.execute("SELECT Nome FROM Dados WHERE ID = 2")
#banco.commit()
edv = "92896201"
verifica = bool
# hoje = datetime.date.today()
# print(hoje)
tag = "011"
globals()


#voltar em liberacao_de_maquina depois
#inconformidades


class Connection:

    #Construtor da class faz a conexão
    def __init__(self, db):
        self.url = 'http://localhost:8000/'
        self.banco = sqlite3.connect(db)
        self.nameColadorador = ''
        self.idColadorador = ''
        self.idCardColadorador = ''
        self.idReleaseMachine = ''
        # self.requisitosMaquina()
        # self.registros()
        self.requisitosMaquinaMeioAmb()
        self.requisitosMaquinaSeguranca()

    #Veriica se o usuario esta no banco de dados
    def pesquisar_colaborador(self, idcard):
        print(idcard)
        self.json_response = requests.get(self.url + 'associates/' + idcard)

        if (self.json_response.status_code == 500):
            print('usuário não cadastro')
            standby.hide()
            standby.show()

        if(self.json_response.status_code==200):
            print('usuário cadastrado')
            # self.todosUsers()

            return self.tipo_colaborador(self.json_response.json())

    def requisitosMaquinaSeguranca(self):
        self.reqSeguranca= requests.get(self.url + 'greenbooks/1/1/').json()
        self.listreqSeguranca = list(self.reqSeguranca)
        self.listreqSeguranca2 = []
        for x in range(len(self.listreqSeguranca)):
            self.listreqSeguranca2.append(self.listreqSeguranca[x]['question'])
            # print(self.listreqSeguranca[x]['question'])

        print('seg:', self.listreqSeguranca2)

    def requisitosMaquinaMeioAmb(self):
        self.reqMeioAmb= requests.get(self.url + 'greenbooks/1/2/').json()

        self.listreqMeioAmb = list(self.reqMeioAmb)
        self.listreqMeioAmb2 = []
        for x in range(len(self.listreqMeioAmb)):
            self.listreqMeioAmb2.append(self.listreqMeioAmb[x]['question'])
            # print(self.listreqMeioAmb2[x]['question'])

        print('meioAmb:', self.listreqMeioAmb2)

    # def requisitosMaquina(self):
    #     self.reqMeioAmb= requests.get(self.url + 'greenbooks/1/2/').json()
    #
    #     self.reqSeg= requests.get(self.url + 'greenbooks/1/1/').json()
    #
    #     self.listreqMeioAmb = list(self.reqMeioAmb)
    #     self.listreqSeg = list(self.reqSeg)
    #     self.listreq = []
    #     for x in range(len(self.listreqMeioAmb)):
    #         self.listreq.append(self.listreqMeioAmb[x]['question'])
    #         print(self.listreqMeioAmb[x]['question'])
    #
    #     for x in range(len(self.listreqSeg)):
    #         self.listreq.append(self.listreqSeg[x]['question'])
    #         print(self.listreqSeg[x]['question'])
    #
    #     print('requisitos:', self.listreq)

    def registrosList(self):
        try:
            self.registros = requests.get(self.url + 'getreleasemachines/').json()
            return self.registros
        except ValueError:
            print(ValueError)

    def registrosList2(self):
        try:
            self.registros2 = requests.get(self.url + 'getreleasemachines/').json()

            return self.registros2
        except ValueError:
            print(ValueError)


    def todosUsers(self):
        # TODOS OS USUÁRIOS
        self.json_responseUser = requests.get(self.url + 'getassociates/')
        print('self.json_responseUser',self.json_responseUser)
        if(self.json_responseUser.status_code == 200):
            print('oiiiii',str(self.json_responseUser.status_code))
            print('len todo user:', len(list(self.json_responseUser.json())))
            return list(self.json_responseUser.json())

        else:
            # print(self.json_responseUser)
            print("deu erro na aquisição")

    def tipo_colaborador(self, dadosJson):
        # APRENDIZ
        print('dadosJsonp:', dadosJson)
        print('----------- Dados Colaborador -----------')
        print(dadosJson)
        self.nameColadorador = dadosJson['name']
        self.idColadorador = str(dadosJson['id'])
        self.edvColadorador = dadosJson['EDV']
        self.idCardColadorador = dadosJson['id_card']
        self.adminU = dadosJson['adminU']
        self.dataNascColaborador = dadosJson['birth']
        self.jobposition = dadosJson['jobposition']
        self.skill = dadosJson['skill']
        self.skill2 = dadosJson['skill2']

        global idGlobal
        idGlobal = self.idColadorador
        print(self.nameColadorador)
        print(self.idColadorador)
        print(self.edvColadorador)
        print(self.idCardColadorador)
        print(self.adminU)
        print(self.dataNascColaborador)
        print(self.adminU)
        print(self.skill)
        print(self.skill2)
        print('id position:',self.jobposition)
        print(idGlobal)

        self.dataNascFormat = datetime.strptime(self.dataNascColaborador, '%Y-%m-%d')
        print(type(self.dataNascFormat))
        self.dataNascFormat2 = datetime.strftime(self.dataNascFormat, '%d/%m/%Y')
        print(type(self.dataNascFormat2))
        # # self.data = datetime.strptime(f'{self.data_nascimento}', '%d/%m/%Y').date()
        print(self.dataNascFormat2)

        #---------------- TIPOS DE USUÁRIOS -------------

        # --------------- users com skill2
        if self.jobposition == 1 and self.skill2 == True or self.jobposition == 4 and self.skill2 == True:
            return ['n2', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        # elif self.jobposition['typeJob'] == "Meio Oficial" and self.skill2 == True:
        #     return ['moskill2', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        #-------------- users com skill1
        elif self.jobposition == 1 or self.jobposition == 4:
            return ['n1', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        # elif self.jobposition['typeJob'] == "Meio Oficial":
        #     return ['mo', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        #------------ adm e manutentor
        elif self.jobposition == 2:
            return ['ma', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        elif self.jobposition == 3:
            return ['adm', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

        # elif self.jobposition['typeJob'] == "Instrutor":
        #     return ['adm', self.idCardColadorador, self.edvColadorador, self.nameColadorador, self.dataNascFormat2]

    def adicionar_cadastro(self, tag_cartao, nome, classe, edv, datanasc):
        cursor = self.banco.cursor()
        self.cargo = 0
        skilladd: False
        skill2add: False
        self.adminU: False
        print('--------- CLASSE: -------', classe)
        print('1:', type(datanasc))
        dataNascFormat = datetime.strptime(datanasc, '%d/%m/%Y').date()
        print('2:', type(dataNascFormat))
        dataNascFormat = datetime.strftime(dataNascFormat, '%Y-%m-%d')
        print('2:', type(dataNascFormat))
        print('3:', dataNascFormat)

        if classe == 'Aprendiz':
            self.cargo = 1
            cadastro.cadastrarColaborador(tag_cartao, nome,self.cargo,edv,dataNascFormat, True, False, False)

        if classe == 'Meio_Oficial':
            self.cargo = 4
            cadastro.cadastrarColaborador(tag_cartao, nome, self.cargo, edv, dataNascFormat, True, False, False)

        elif classe == 'Responsável':
            self.cargo = 3
            cadastro.cadastrarColaborador(tag_cartao, nome, self.cargo, edv, dataNascFormat, True, True, True)

        elif classe == 'Manutentor':
            self.cargo = 2
            cadastro.cadastrarColaborador(tag_cartao, nome, self.cargo, edv, dataNascFormat,True, True, False)

class Adicionar():
    def cadastrarColaborador(self, tag_cartao, nome, classe, edv, dataNascFormat, skilladd, skill2add, adminU):
        path = 'associates/'

        body = [{
            "jobposition": classe,
            "name": nome,
            "EDV": edv,
            "id_card": tag_cartao,
            "skill": skilladd,
            "skill2": skill2add,
            "adminU": adminU,
            "birth": dataNascFormat,

        }]
        try:
            urlPost = banco_dados.url + path
            print(urlPost)

            post = requests.post(urlPost, json=body)

            if post.status_code == 200:
                print('post realizado', post.status_code)

            else:
                print('post NÃO realizado', post.status_code)
        except:
            print("error")

class Standby(QMainWindow, Ui_Standby):  # primeira tela que faz a validação da tag do crachá
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.lineEdit_tag.setFocus()
        self.lineEdit_tag.returnPressed.connect(self.comeca)
        self.lineEdit_tag.setText("")
        self.botao_imagem.clicked.connect(self.mousePressEvent)

    # Função caso clique na tela, ainda garante que a tag seja escrita na lineEdit_tag.

    def mousePressEvent(self, e):
        self.lineEdit_tag.setFocus()
        print("Cliquei")

    # Função que é chamada para fazer a verificação da tag do usuário após passar o crachá sobre o leitor/ENTER for pressionado.
    def comeca(self):
        tag = self.lineEdit_tag.text()
        print('valor tag:', tag)

        self.colaboradorB = banco_dados.pesquisar_colaborador(tag)

        #SE o coladorador tiver aptidão continua o programa
        if(self.colaboradorB  != None):
            self.classeColaborador = self.colaboradorB[0]
            self.colaborador2 = self.colaboradorB[3].split(" ")
            print('colaborador', self.colaboradorB)
            print('colaborador2', self.colaborador2)
            self.configurar()
            # standby.hide()
            # Menu01Aprendiz.show()

        else:
            self.lineEdit_tag.setFocus()
            self.lineEdit_tag.setText("")
            self.label_titulo.setText("ERRO DE LEITURA\nTENTE NOVAMENTE")
            print("Cliquei")
            pass

    def configurar(self):
        if (self.colaboradorB[0] == 'n2'):
            Menu01_skill2.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu01_skill2.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            standby.hide()
            Menu01_skill2.show()

        elif (self.colaboradorB[0] == 'n1'):
            Menu01Aprendiz.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu01Aprendiz.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            standby.hide()
            Menu01Aprendiz.show()

        else:
            Menu01.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu01.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            Menu02.Label_Colaborador.setText(f'COLABORADOR: {self.colaborador2[0]} {self.colaborador2[-1]}')
            Menu02.Label_EDV.setText(f"EDV: {self.colaboradorB[2]}")
            standby.hide()
            Menu01.show()

    def sairMenu(self):
        if (self.colaboradorB[0] == 'n1'):
             Menu01Aprendiz.hide()
             standby.show()

        elif(self.colaboradorB[0] == 'n2'):
             Menu01_skill2.hide()
             standby.show()

        else:
            Menu02.hide()
            standby.show()

    def homeShow(self):
        if (self.colaboradorB[0] == 'n1'):
             Menu01Aprendiz.show()

        elif(self.colaboradorB[0] == 'n2'):
             Menu01_skill2.show()

        else:
            Menu01.show()

    def homeHide(self):
        if (self.colaboradorB[0] == 'n1'):
             Menu01Aprendiz.hide()

        elif(self.colaboradorB[0] == 'n2'):
             Menu01_skill2.hide()

        else:
            Menu01.show()

class Sair():
    def sair(self):
        if (standby.classeColaborador == 'n1'):
            if (Menu01Aprendiz.maquina_liberada == False):
                standby.sairMenu()
            else:
                self.sairBanco()

        if (standby.classeColaborador == 'n2'):
            if (Menu01_skill2.maquina_liberada == False):
                standby.sairMenu()

            else:
                self.sairBanco()

        else:
            if(Menu01.maquina_liberada == False):
                standby.sairMenu()
            else:
                self.sairBanco()

    def sairBanco(self):
        url = banco_dados.url + 'releasemachines/' + str(banco_dados.idReleaseMachine) + '/'

        print('url sair banco', url)
        try:
            hora = datetime.today().strftime('%H:%M:%S:%f')

            url = banco_dados.url + 'releasemachines/' + str(banco_dados.idReleaseMachine) + '/'

            print('url sair banco',url )
            patch = {
                "FinishHour": hora,
            }

            urlpost = requests.patch(url, patch)

            print('patch sair release machine:', urlpost.status_code)

            if (urlpost.status_code == 200):
                try:

                    urlMachine = banco_dados.url + 'machines/1/'

                    patch2 = {
                        "status": False,
                    }

                    urlPut = requests.patch(urlMachine, patch2)

                    print('patch Desl', urlPut.status_code)

                    if (urlPut.status_code == 200):
                        standby.lineEdit_tag.setText("")
                        standby.sairMenu()
                        # standby.show()
                except:
                    print(urlPut.status_code)
        except:
            print(urlpost.status_code)

##################### MENU 01 ################################
class Primeiro_Menu(QMainWindow, Ui_Menu01):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.maquina_liberada = False
        self.Botao_Seta_Direita.clicked.connect(self.proxima_tela)
        self.Botao_Liberar_Maquina.clicked.connect(self.liberacao_de_maquina)
        self.Botao_Interface_Didatica.clicked.connect(self.interface_didatica)
        self.Botao_Documentos.clicked.connect(self.menu_documentos)
        self.Botao_Registros.clicked.connect(self.menu_registros)

    # ******************************* FUNÇÕES DA CLASSE *******************************

    def proxima_tela(self): #FUNÇÃO QUE CHAMA O MENU 02.

        Menu02.show()
        Menu01.hide()

    def liberacao_de_maquina(self): #FUNÇÃO QUE INICIA O PROCESSO DE LIBERAÇÃO DE MÁQUINA.
        print('AQUIIIIIIII HELP')
        if self.maquina_liberada == False:
            liberacao_atencao.show()
            Menu01.hide()

        else:
            pass

    def menu_documentos(self): # FUNÇÃO QUE CHAMA A TELA DE MENU DE DOCUMENTOS
        documentos_menu.show()
        Menu01.hide()

    # Função que chama a tela de Interface Didática Menu.
    def interface_didatica(self):
        interface_menu.show()
        Menu01.hide()

    # Função que chama a tela de Menu de Registros.
    def menu_registros(self):
        registros_menu.show()
        Menu01.hide()

class Primeiro_MenuSkill(QMainWindow, Ui_Menu01_skill2):
    def __init__(self): #FUNÇÃO QUE INICIA A TELA E DECLARA OS BOTÕES,LABELS,ETC.
        super().__init__() #COMANDO PARA INICIAR A TELA.
        super().setupUi(self) #COMANDO PARA INICIAR A TELA.
        self.maquina_liberada = False
        self.Botao_Liberar_Maquina.clicked.connect(self.liberacao_de_maquina) #DEFINE A FUNÇÃO QUE SERÁ CHAMADA QUANDO O BOTÃO DE LIBERAR A MÁQUINA FOR CLICADO.
        self.Botao_Interface_Didatica.clicked.connect(self.interface_didatica)
        self.Botao_Documentos.clicked.connect(self.menu_documentos) #DEFINE A FUNÇÃO QUE SERÁ CHAMADA QUANDO O BOTÃO DE DOCUMENTOS FOR CLICADO.
        self.Botao_Registros.clicked.connect(self.menu_registros)
        self.Botao_Sair.clicked.connect(self.sairFunc)
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")

        # self.Label_Colaborador.setText(f"COLABORADOR: {colaborador}") #DEFINE A LABEL COM O NOME DO COLABORADOR.
        # self.Label_EDV.setText(f"EDV: {edv}") #DEFINE A LABEL COM O EDV DO COLABORADOR.

    def proxima_tela(self): #FUNÇÃO QUE CHAMA O MENU 02.
        Menu02.show()
        Menu01_skill2.hide()

    def liberacao_de_maquina(self): #FUNÇÃO QUE INICIA O PROCESSO DE LIBERAÇÃO DE MÁQUINA.
        print('AQUIIIIIIII HELP')
        if self.maquina_liberada == False:
            aviso_liberacao.label_texto.setText("<html><head/><body><p align=\"center\">O(s) seguinte(s) item(s) de Segurança não foram </p><p align=\"center\">marcado(s), o que significa que ele(s) apresenta(m) </p><p align=\"center\">não conformidade:</p></body></html>")
            liberacao_atencao.show()

            Menu01_skill2.hide()

        else:
            print(" ")

    def menu_documentos(self): # FUNÇÃO QUE CHAMA A TELA DE MENU DE DOCUMENTOS
        documentos_menu.show()
        Menu01_skill2.hide()

    def interface_didatica(self):
        interface_menu.show()
        Menu01_skill2.hide()

    def menu_registros(self):
        registros_menu.show()
        Menu01_skill2.hide()

    def sairFunc(self):
        sairDef.sair()
        Menu01Aprendiz.maquina_liberada = False
        self.clear_checkboxes()
        standby.lineEdit_tag.setText("")
        standby.label_titulo.setText("APROXIME O CRACHÁ\nSOBRE O LEITOR")
        """""  
        GPIO.output(Alimentacao_maquina, False) 
        GPIO.output(led, True)   
        """""

    def clear_checkboxes(self):
        Menu01Aprendiz.maquina_liberada = False
        self.checkboxes = [liberacao_seguranca.checkBox_1, liberacao_seguranca.checkBox_2,
                           liberacao_seguranca.checkBox_3,
                           liberacao_seguranca.checkBox_4, liberacao_seguranca.checkBox_5,
                           liberacao_seguranca.checkBox_6,
                           liberacao_seguranca.checkBox_7, liberacao_seguranca.checkBox_8,
                           liberacao_seguranca.checkBox_9,
                           liberacao_meio_ambiente.checkBox_1]
        for i in self.checkboxes:
            i.setChecked(False)
        Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.cadeado_fechado)

##################### MENU 01 APRENDIZ ################################
class Primeiro_MenuAPRENDIZ(QMainWindow, Ui_Menu01Aprendiz):
    def __init__(self): #FUNÇÃO QUE INICIA A TELA E DECLARA OS BOTÕES,LABELS,ETC.
        super().__init__() #COMANDO PARA INICIAR A TELA.
        super().setupUi(self) #COMANDO PARA INICIAR A TELA.
        self.maquina_liberada = False

        self.Botao_Liberar_Maquina.clicked.connect(self.liberacao_de_maquina) #DEFINE A FUNÇÃO QUE SERÁ CHAMADA QUANDO O BOTÃO DE LIBERAR A MÁQUINA FOR CLICADO.
        self.Botao_Interface_Didatica.clicked.connect(self.interface_didatica)
        self.Botao_Documentos.clicked.connect(self.menu_documentos) #DEFINE A FUNÇÃO QUE SERÁ CHAMADA QUANDO O BOTÃO DE DOCUMENTOS FOR CLICADO.
        self.Botao_Registros.clicked.connect(self.menu_registros)
        self.Botao_Sair.clicked.connect(self.sairFunc)
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")
        # self.Label_Colaborador.setText(f"COLABORADOR: {colaborador}") #DEFINE A LABEL COM O NOME DO COLABORADOR.
        # self.Label_EDV.setText(f"EDV: {edv}") #DEFINE A LABEL COM O EDV DO COLABORADOR.

    def liberacao_de_maquina(self):  # FUNÇÃO QUE INICIA O PROCESSO DE LIBERAÇÃO DE MÁQUINA.
        print('AQUIIIIIIII HELP')
        if self.maquina_liberada == False:
            aviso_liberacao.label_texto.setText(
                "<html><head/><body><p align=\"center\">O(s) seguinte(s) item(s) de Segurança não foram </p><p align=\"center\">marcado(s), o que significa que ele(s) apresenta(m) </p><p align=\"center\">não conformidade:</p></body></html>")
            liberacao_atencao.show()

            Menu01Aprendiz.hide()

        else:
            print(" ")

    def menu_documentos(self):  # FUNÇÃO QUE CHAMA A TELA DE MENU DE DOCUMENTOS
        documentos_menu.show()
        Menu01Aprendiz.hide()

    def interface_didatica(self):
        interface_menu.show()
        Menu01Aprendiz.hide()

    def menu_registros(self):
        registros_menu.show()
        Menu01Aprendiz.hide()

    def sairFunc(self):
        sairDef.sair()
        Menu01Aprendiz.maquina_liberada = False
        self.clear_checkboxes()
        standby.lineEdit_tag.setText("")
        standby.label_titulo.setText("APROXIME O CRACHÁ\nSOBRE O LEITOR")
        """""  
        GPIO.output(Alimentacao_maquina, False) 
        GPIO.output(led, True)   
        """""
        # sairDef.sair()

    def clear_checkboxes(self):
        Menu01Aprendiz.maquina_liberada = False
        self.checkboxes = [liberacao_seguranca.checkBox_1, liberacao_seguranca.checkBox_2,
                           liberacao_seguranca.checkBox_3,
                           liberacao_seguranca.checkBox_4, liberacao_seguranca.checkBox_5,
                           liberacao_seguranca.checkBox_6,
                           liberacao_seguranca.checkBox_7, liberacao_seguranca.checkBox_8,
                           liberacao_seguranca.checkBox_9,
                           liberacao_meio_ambiente.checkBox_1]
        for i in self.checkboxes:
            i.setChecked(False)
        Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.cadeado_fechado)

class Segundo_Menu(QMainWindow, Ui_Menu02):  # SEGUNDO MENU
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.Botao_Seta_Esquerda.clicked.connect(self.tela_anterior)
        self.Botao_Cadastros.clicked.connect(self.cadastros)
        self.Botao_Sair.clicked.connect(self.sair)
        self.cadeado_fechado = QIcon("imagens/CADEADO_FECHADO.png")
        self.Label_Colaborador.setText(f"COLABORADOR: {colaborador}")
        self.Label_EDV.setText(f"EDV: {edv}")

    def tela_anterior(self):
        print(colaborador)
        Menu01.show()
        Menu02.hide()

    def cadastros(self):
        cadastros_menu.load_tabela()
        cadastros_menu.show()
        Menu02.hide()

    def sair(self):
        # standby.mousePressEvent.connect(standby.mousePressEvent())
        sairDef.sair()
        Menu01.maquina_liberada = False
        self.clear_checkboxes()
        standby.lineEdit_tag.setText("")
        standby.label_titulo.setText("APROXIME O CRACHÁ\nSOBRE O LEITOR")
        """""  
        GPIO.output(Alimentacao_maquina, False) 
        GPIO.output(led, True)   
        """""

        standby.show()

    def clear_checkboxes(self):
        Menu01.maquina_liberada = False
        self.checkboxes = [liberacao_seguranca.checkBox_1, liberacao_seguranca.checkBox_2,
                           liberacao_seguranca.checkBox_3,
                           liberacao_seguranca.checkBox_4, liberacao_seguranca.checkBox_5,
                           liberacao_seguranca.checkBox_6,
                           liberacao_seguranca.checkBox_7, liberacao_seguranca.checkBox_8,
                           liberacao_seguranca.checkBox_9,
                           liberacao_meio_ambiente.checkBox_1]
        for i in self.checkboxes:
            i.setChecked(False)
        Menu01.Botao_Liberar_Maquina.setIcon(self.cadeado_fechado)

################################ TELA DE INSTRUÇÕES PARA LIBERAÇÃO ################################
#Tela de advertência sobre o processo de libreação de máquina.
class Liberacao_atencao(QMainWindow, Ui_Atencao):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_continuar.clicked.connect(self.tela_de_seguranca)
        self.botao_home.clicked.connect(self.home)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    # Função que avança para a Liberação_Segurança.
    def tela_de_seguranca(self):
        print('SEGURANÇAAAAAAAAAAAAAAAA')
        liberacao_seguranca.show()
        liberacao_atencao.hide()

    # Função que retorna para o Menu01 (HOME).
    def home(self):
        liberacao_atencao.hide()
        standby.configurar()

################################ TELA DE LIBERAÇÃO DOS REQUISITOS DE SEGURANÇA ################################
#Tela que o usuário verifica os requisitos de segurança.
class Liberacao_seguranca(QMainWindow, Ui_Liberacao_Seguranca):
    def __init__(self):
        print('---------- TO AQUI ---------')
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_continuar.clicked.connect(self.tela_meio_ambiente)
        self.allcheckBox = [self.checkBox_1, self.checkBox_2, self.checkBox_3, self.checkBox_4, self.checkBox_5,
                            self.checkBox_6, self.checkBox_7, self.checkBox_8, self.checkBox_9]

        # ******************************* VARIÁVEIS *******************************

        self.liberacao_seguranca = False
        self.lista_real = []  # Lista de Check_Boxes checados.
        self.lista_erros = []  # Lista de Check_Boxes não checados.
        self.texto = []  # Texto  indicando os Check_boxes não checados.
        self.contador = 0  # Contador auxiliar.
        self.inconformidades = []

        self.string_da_lista = ""

        # ******************************* FUNÇÕES DA CLASSE *******************************

    def verifica_checkBox(self):
        self.lista_real = []
        self.contador = 0

        for i in self.allcheckBox:
            print('allcheckBox:', i)
            if i.isChecked():
                self.contador = self.contador + 1
                self.lista_real.append(self.contador)
                print('list_real', self.lista_real)

            else:
                # self.lista_real.remove(self.contador)
                self.contador = self.contador + 1

        for reqs in range(len(banco_dados.listreqSeguranca2)):
            if banco_dados.listreqSeguranca2[reqs] not in self.lista_real:
                inconformidade = "\n" + banco_dados.listreqSeguranca2[reqs]
                self.inconformidades.append(inconformidade)

        print('inconformidades', self.inconformidades)

    def verifica_check_boxes_seguranca(self):
        for i in range(1, 10):
            print('cb:',i)
            if i not in self.lista_real:
                self.lista_erros.append(i)

        if len(self.lista_erros) != 0:
            self.texto = str(self.lista_erros)
            return False
        else:
            return True


    def home(self):
        standby.configurar()
        # Menu01.show()
        liberacao_seguranca.hide()

    # Função que passa para a tela de meio-ambiente caso todos os checkboxes de segurança estiverem checados.

    def tela_meio_ambiente(self):
        self.verifica_checkBox()
        if self.verifica_check_boxes_seguranca() == True:
            self.liberacao_seguranca = True
            aviso_liberacao.label_itens_seguranca.setText("OK")

        else:
            aviso_liberacao.label_itens_seguranca.setText(f"<html><head/><body><p align=\"center\">{self.texto}")
            self.liberacao_seguranca = False

        liberacao_meio_ambiente.show()
        liberacao_seguranca.hide()

        # Função qeu chama a tela de relatar incidente.
    def relatos_liberacao(self):
        relatos_liberacao.lineEdit_descricao.setFocus()
        liberacao_seguranca.string_da_lista = " ".join(liberacao_seguranca.inconformidades)

        print(liberacao_seguranca.string_da_lista)

        relatos_liberacao.label_itens_nao_conformes.setText(liberacao_seguranca.string_da_lista)

        relatos_liberacao.show()
        aviso_liberacao.hide()

class Aviso_liberacao(QMainWindow, Ui_Aviso_Liberacao):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_voltar.clicked.connect(self.voltar_check_list)
        self.botao_relatar_problema.clicked.connect(self.relatos_liberacao)

    # ******************************* FUNÇÕES DA CLASSE *******************************

    #Função que retorna para os Checkboxes da respectiva tela de liberação.
    def voltar_check_list(self):
        if liberacao_seguranca.liberacao_seguranca == False:
            liberacao_seguranca.lista_erros = []
            relatos_liberacao.label_itens_nao_conformes.clear()
            liberacao_seguranca.string_da_lista = " "
            liberacao_seguranca.inconformidades.clear()

            liberacao_seguranca.show()
            aviso_liberacao.hide()

        else:
            #self.label_itens_seguranca.setText("OK")
            liberacao_meio_ambiente.show()
            aviso_liberacao.hide()

    #Função qeu chama a tela de relatar incidente.
    def relatos_liberacao(self):
        relatos_liberacao.lineEdit_descricao.setFocus()
        liberacao_seguranca.string_da_lista = " ".join(liberacao_seguranca.inconformidades)

        print(liberacao_seguranca.string_da_lista)

        relatos_liberacao.label_itens_nao_conformes.setText(liberacao_seguranca.string_da_lista)

        relatos_liberacao.show()
        aviso_liberacao.hide()

class Relatos_liberacao(QMainWindow, Ui_Relatos_liberacao):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.lineEdit_descricao.clear()
        self.lineEdit_descricao.setPlaceholderText("Digite aqui uma breve descrição sobre o incidente ou anomalia encontrada.")
        self.botao_cancelar.clicked.connect(self.voltar)
        self.botao_finalizar.clicked.connect(self.salvar)


    def salvar(self):
        self.label_itens_nao_conformes.clear()





    def voltar(self):
        self.label_itens_nao_conformes.clear()
        liberacao_seguranca.string_da_lista = " "
        liberacao_seguranca.inconformidades.clear()
        liberacao_seguranca.lista_erros = []
        print(liberacao_seguranca.lista_real)
        print(liberacao_seguranca.lista_erros)

        liberacao_seguranca.show()
        relatos_liberacao.hide()



class Liberacao_meio_ambiente(QMainWindow, Ui_Liberacao_Meio_Ambiente):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_home.clicked.connect(self.home)
        self.botao_continuar.clicked.connect(self.Verifica_checkboxes)

        # ******************************* VARIÁVEIS *******************************
        self.liberacao_meio_ambiente = False
        self.img2 = QIcon("imagens/CADEADO_ABERTO.png")
        self.cadeado_manutencao = QIcon("imagens/CADEADO_MANUTENCAO.png")
        self.allcheckBox = [self.checkBox_1]


    def home(self):
        liberacao_meio_ambiente.hide()
        standby.configurar()
        # Menu01.show()

    # Função que verifica os Chechboxes de meio-ambiente e envia o sinal de uma porta analógica da Raspberry para comutar o contator elétrico caso o status da liberação seja OK.
    # Se a liberação for "Não OK" e o colaborador identificar algum problema na integridade e funcionamento da máquina, abre-se uma ficha para que o incidente seja relatado.
    def Verifica_checkboxes(self):

        if self.checkBox_1.isChecked():
            #classeColaborador é o variável da classe standby
            if (standby.classeColaborador == 'n1'):
                Menu01Aprendiz.maquina_liberada = True
                aviso_liberacao.label_itens_meio_ambiente.setText("OK")


            elif (standby.classeColaborador == 'n2'):
                Menu01_skill2.maquina_liberada = True
                aviso_liberacao.label_itens_meio_ambiente.setText("OK")


            else:
                Menu01.maquina_liberada = True
                aviso_liberacao.label_itens_meio_ambiente.setText("OK")

        else:
            inconformidade = "\n" + banco_dados.listreqMeioAmb2[0]

            liberacao_seguranca.inconformidades.append(inconformidade)

            self.liberacao_meio_ambiente = False
            aviso_liberacao.label_itens_meio_ambiente.setText(f"<html><head/><body><p align=\"center\">1")

        if self.checkBox_1.isChecked() and (liberacao_seguranca.liberacao_seguranca == True):
            data = datetime.today().strftime('%Y-%m-%d')
            hora = datetime.today().strftime('%H:%M:%S:%f')
            print('global idGlobal:', idGlobal)

            url = banco_dados.url + 'releasemachines/'

            body = [{
                "date": data,
                "InitialHour": hora,
                "FinishHour": None,
                "idMachineFK": "1",
                "idAssociateFK": idGlobal,
                "examA": 'A',
                "examB": 'B',
                "result": 'OK'
            }]

            try:
                urlpost = requests.post(url, json = body)

                print(urlpost.status_code)

                if(urlpost.status_code==200):
                    try:
                        urlID = urlpost.json()
                        print(urlID[0]['id'])

                        banco_dados.idReleaseMachine = urlID[0]['id']

                        urlMachine = banco_dados.url + 'machines/1/'
                        patch = {
                            "status": True,
                        }

                        urlPut = requests.patch(urlMachine, json=patch)

                        print('put', urlPut.status_code)

                        if(urlPut.status_code==200):
                            if (standby.classeColaborador == 'n1'):
                                Menu01Aprendiz.Botao_Liberar_Maquina.setIcon(self.img2)
                                liberacao_meio_ambiente.hide()
                                Menu01Aprendiz.show()

                            elif (standby.classeColaborador == 'n2'):
                                Menu01_skill2.Botao_Liberar_Maquina.setIcon(self.img2)
                                liberacao_meio_ambiente.hide()
                                Menu01_skill2.show()

                            else:
                                Menu01.Botao_Liberar_Maquina.setIcon(self.img2)
                                liberacao_meio_ambiente.hide()
                                Menu01.show()
                    except:
                        print(urlPut.status_code)
            except:
                print(urlpost.status_code)

        else:
            # aviso_liberacao.label_texto.setText("<html><head/><body><p align=\"center\">O(s) seguinte(s) item(s) de Meio Ambiente não foram </p><p align=\"center\"> marcado(s), o que significa que ele(s) apresenta(m)</p><p align=\"center\"> não conformidade:</p></body></html>")
            # aviso_liberacao.label_itens_desmarcados.setText(f"<html><head/><body><p align=\"center\">1")
            aviso_liberacao.show()
            liberacao_meio_ambiente.hide()

class Documentos_menu(QMainWindow, Ui_documentos_menu):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)
        self.botao_documentos_de_pecas01.clicked.connect(self.documentos_de_pecas)
        self.botao_documentos_de_pecas02.clicked.connect(self.documentos_de_pecas)
        self.botao_diagrama_eletrico01.clicked.connect(self.diagrama_eletrico)
        self.botao_diagrama_eletrico02.clicked.connect(self.diagrama_eletrico)
        self.botao_mae01.clicked.connect(self.mapa_de_riscos)
        self.botao_mae02.clicked.connect(self.mapa_de_riscos)

    def home(self):
        standby.homeShow()
        # Menu01.show()
        documentos_menu.hide()

    def documentos_de_pecas(self):
        documentos_de_pecas_menu.show()
        documentos_menu.hide()

    def diagrama_eletrico(self):
        diagrama_eletrico.show()
        documentos_menu.hide()

    def mapa_de_riscos(self):
        mapa_de_riscos.show()
        documentos_menu.hide()

class Documentos_documentos_de_pecas_menu(QMainWindow, Ui_documentos_documentos_de_pecas_menu):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)
        self.botao_peca01_1.clicked.connect(self.peca01)
        self.botao_peca01_2.clicked.connect(self.peca01)
        self.botao_peca02_1.clicked.connect(self.peca02)
        self.botao_peca02_2.clicked.connect(self.peca02)
        self.botao_peca03_1.clicked.connect(self.peca03)
        self.botao_peca03_2.clicked.connect(self.peca03)

    def home(self):
        documentos_menu.show()
        documentos_de_pecas_menu.hide()

    def peca01(self):
        peca01.show()
        documentos_de_pecas_menu.hide()

    def peca02(self):
        peca02.show()
        documentos_de_pecas_menu.hide()

    def peca03(self):
        peca03.show()
        documentos_de_pecas_menu.hide()

class Documentos_de_peca_peca01(QMainWindow, Ui_peca01):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)

    def home(self):
        documentos_de_pecas_menu.show()
        peca01.hide()

class Documentos_de_peca_peca02(QMainWindow, Ui_peca02):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)

    def home(self):
        documentos_de_pecas_menu.show()
        peca02.hide()

class Documentos_de_peca_peca03(QMainWindow, Ui_peca03):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)

    def home(self):
        documentos_de_pecas_menu.show()
        peca03.hide()

class diagrama_eletrico(QMainWindow, Ui_documentos_diagrama_eletrico):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.contador = 1

        self.botao_home.clicked.connect(self.home)
        self.botao_seta_direita.clicked.connect(self.proxima_pagina)
        self.botao_seta_esquerda.clicked.connect(self.pagina_anterior)

        self.pagina1 = QPixmap("imagens/cachorro.png")
        self.pagina2 = QPixmap("imagens/jacare.png")
        self.pagina3 = QPixmap("imagens/MANUTENCAO.png")
        self.label_imagem.setPixmap(self.pagina1)

        if self.botao_seta_esquerda.clicked:
            print("oi")

    def home(self):
        documentos_menu.show()
        diagrama_eletrico.hide()

    def proxima_pagina(self):
        if self.contador < 3:
            self.contador += 1

        if self.contador == 2:
            self.label_imagem.setPixmap(self.pagina2)
            self.label_paginas.setText("PÁGINA 02/03")

        if self.contador == 3:
            self.label_imagem.setPixmap(self.pagina3)
            self.label_paginas.setText("PÁGINA 03/03")

    def pagina_anterior(self):
        if self.contador > 1:
            self.contador -= 1

        if self.contador == 1:
            self.label_imagem.setPixmap(self.pagina1)
            self.label_paginas.setText("PÁGINA 01/03")

        if self.contador == 2:
            self.label_imagem.setPixmap(self.pagina2)
            self.label_paginas.setText("PÁGINA 02/03")

class Mapa_de_riscos(QMainWindow, Ui_mapa_de_riscos):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)

    def home(self):
        documentos_menu.show()
        mapa_de_riscos.hide()

class Interface_menu(QMainWindow, Ui_interface_didatica_menu):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_botoes.clicked.connect(self.botoes)
        self.botao_finalidades.clicked.connect(self.finalidade)
        self.botao_home.clicked.connect(self.home)

    def finalidade(self):
        interface_menu_finalidade.show()
        interface_menu.hide()

    def botoes(self):
        interface_menu_botoes.show()
        interface_menu.hide()

    def home(self):
        standby.homeShow()
        # Menu01.show()
        interface_menu.hide()

class Interface_botoes(QMainWindow, Ui_interface_didatica_menu_botoes):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_1.clicked.connect(self.botao_01)
        self.botao_2.clicked.connect(self.botao_02)
        self.botao_3.clicked.connect(self.botao_03)
        self.botao_4.clicked.connect(self.botao_04)
        self.botao_5.clicked.connect(self.botao_05)
        self.botao_home.clicked.connect(self.home)
        self.botao_seta_dirteita.clicked.connect(self.botao_emergencia)

    def botao_01(self):
        self.label_indicacao.setText("1")
        self.label_titulo.setStyleSheet(
            "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n""border-width:6px;\n""\n""\n""font: 75 30pt \"Bosch Sans Bold\";\n""background-color: rgb(0,0,0);")
        self.label_titulo.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">BOTÃO LIGA A SERRA</span></p></body></html>")
        self.label_caixa_de_texto.setText(
            "             Botão responsável por iniciar o processo de \ncorte do perfil se a porta estiver trancada e a peça \ntravada. \n")

    def botao_02(self):
        self.label_titulo.setStyleSheet(
            "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n""border-width:6px;\n""\n""\n""font: 75 30pt \"Bosch Sans Bold\";\n""background-color: rgb(0,0,0);")
        self.label_indicacao.setText("2")
        self.label_titulo.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">CHAVE SELETORA DE PERFIL 30/45</span></p></body></html>")
        self.label_caixa_de_texto.setText(
            "             Chave seletora responsável por definir se o \nperfil a ser cortado é de 30 ou 45 para estabelecer a \ndistância que a serra deverá cortar para ultrapassar o \nperfil de 30/45 completamente.")

    def botao_03(self):
        self.label_indicacao.setText("3")
        self.label_titulo.setStyleSheet(
            "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n""border-width:6px;\n""\n""\n""font: 75 28pt \"Bosch Sans Bold\";\n""background-color: rgb(0,0,0);")
        self.label_titulo.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">CHAVE SELETORA DE PORTA TRANCADA</span></p></body></html>")
        self.label_caixa_de_texto.setText(
            "             Chave seletora responsável por garantir o \ntravamento da porta.\n\n")

    def botao_04(self):
        self.label_indicacao.setText("4")
        self.label_titulo.setStyleSheet(
            "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n""border-width:6px;\n""\n""\n""font: 75 30pt \"Bosch Sans Bold\";\n""background-color: rgb(0,0,0);")
        self.label_titulo.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">BOTÃO PARA TRAVAR PEÇA</span></p></body></html>")
        self.label_caixa_de_texto.setText(
            "             Ao pressionar o botão, dois pistões pneumáticos \ntravam a peça na posição estabelecida pelo usuário.\n\n")

    def botao_05(self):
        self.label_indicacao.setText("5")
        self.label_titulo.setStyleSheet(
            "border-style: outset;\n" "border-color: rgb(0, 0, 0);\n""border-width:6px;\n""\n""\n""font: 75 30pt \"Bosch Sans Bold\";\n""background-color: rgb(0,0,0);")
        self.label_titulo.setText(
            "<html><head/><body><p align=\"center\"><span style=\" color:#FFC000;\">BOTÃO RESET</span></p></body></html>")
        self.label_caixa_de_texto.setText(
            "             Botão necessário para reiniciar os processos da \nmáquina caso ocorra alguma falha, como a tentativa de \nabrir as portas de segurança durante a operação, ou ao \npressionar o botão de emergência.")

    def botao_emergencia(self):
        interface_menu_botao_emergencia.show()
        interface_menu_botoes.hide()

    def home(self):
        interface_menu.show()
        interface_menu_botoes.hide()

class Interface_botao_emergencia(QMainWindow, Ui_interface_didatica_menu_botao_emergencia):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)
        self.botao_seta_esquerda.clicked.connect(self.botoeira)

    def home(self):
        interface_menu.show()
        interface_menu_botao_emergencia.hide()

    def botoeira(self):
        interface_menu_botoes.show()
        interface_menu_botao_emergencia.hide()

class Interface_finalidade(QMainWindow, Ui_interface_didatica_finalidade):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_home.clicked.connect(self.home)

    def home(self):
        interface_menu.show()
        interface_menu_finalidade.hide()

class Registros_menu(QMainWindow, Ui_Registros_menu):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        # ******************************* AÇÕES *******************************
        self.botao_home.clicked.connect(self.home)
        self.botao_historico_utilizacao_01.clicked.connect(self.resgistros_de_uso)
        self.botao_historico_utilizacao_02.clicked.connect(self.resgistros_de_uso)

        # ******************************* FUNÇÕES DA CLASSE *******************************

    # Função que volta para o menu
    def home(self):
        standby.configurar()
        # Menu01.show()
        registros_menu.hide()

    # Função que abre o histórico de utilização
    def resgistros_de_uso(self):
        registro_historico_utilizacao.load_registros()
        registro_historico_utilizacao.show()
        registros_menu.hide()

class Registro_historico_utilizacao(QMainWindow, Ui_cadastros_historico_utilizacao):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        # ******************************* AÇÕES *******************************

        self.botao_voltar.clicked.connect(self.voltar)

        # ******************************* CONFIGURAÇÕES *******************************

        # self.load_registros()

        # ******************************* FUNÇÕES DA CLASSE *******************************

    #Função que carrega as configurações e dados da tabela de utilização.
    def load_registros(self):
        self.tabela_utilizacao.setColumnCount(6)

        self.tabela_utilizacao.setColumnWidth(0, 360)
        self.tabela_utilizacao.setColumnWidth(1, 150)
        self.tabela_utilizacao.setColumnWidth(2, 170)
        self.tabela_utilizacao.setColumnWidth(3, 180)
        self.tabela_utilizacao.setColumnWidth(4, 120)
        self.tabela_utilizacao.setColumnWidth(5, 200)

        self.tabela_utilizacao.setHorizontalHeaderLabels(["NOME", "EDV", "DATA", "HORA", "EXAME", "RESULTADO"])
        self.tabela_utilizacao.setSelectionBehavior(QAbstractItemView.SelectRows)

        try:
            registros = banco_dados.registrosList()
        except:
            registros = banco_dados.registrosList2()
            print("deu erro aq")

        print('type registro',type(registros))
        # registros = banco_dados.chama_registros()
        registros = list(registros)
        self.tabela_utilizacao.setRowCount(len(registros))
        row = 0

        for x in range(len(registros)):
            # print(registros[x])
            name = registros[x]['idAssociateFK']['name'].split(" ")
            name = name[0] + " " + name[-1]
            dataNascFormat = datetime.strptime(registros[x]['date'], '%Y-%m-%d')
            dataNascFormat2 = datetime.strftime(dataNascFormat, '%d/%m/%Y')
            horaInicial = registros[x]['InitialHour'].split(':')
            try:
                horaFinal = registros[x]['FinishHour'].split(':')
                horaFinal = horaFinal[0] + ":" + horaFinal[1]
            except:
                horaFinal = " "
            horaInicial = horaInicial[0] + ":" + horaInicial[1]

            hora = horaInicial + ' - ' + horaFinal
            exame = registros[x]['examA'] + ',' + registros[x]['examB']
            self.tabela_utilizacao.setItem(row, 0, QTableWidgetItem(name))
            try:
                self.tabela_utilizacao.setItem(row, 1, QTableWidgetItem(str((registros[x]['idAssociateFK']['EDV']))))
            except Exception as erro:
                print(f"{erro} AQUI02")
            self.tabela_utilizacao.setItem(row, 2, QTableWidgetItem(dataNascFormat2))
            self.tabela_utilizacao.setItem(row, 3, QTableWidgetItem(hora))
            self.tabela_utilizacao.setItem(row, 4, QTableWidgetItem((exame)))
            self.tabela_utilizacao.setItem(row, 5, QTableWidgetItem((registros[x]['result'])))
            #
            row = row + 1



        # row = 0

        # self.tabela_utilizacao.setItem(row, 0, QTableWidgetItem(0,str(self.hoje)))

    def voltar(self):
        # self.load_registros()
        registros_menu.show()
        registro_historico_utilizacao.hide()

class Cadastros_menu(QMainWindow, Ui_cadastros_menu):

    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.imagem_aprendiz2 = QPixmap("imagens\Aprendiz_03.png")
        self.imagem_meio_oficial2 = QPixmap("imagens\Meio_oficial_03.png")
        self.imagem_manutentor2 = QPixmap("imagens\Manutentor_03.png")
        self.imagem_responsavel2 = QPixmap("imagens\Responsavel_03.png")

        self.nome = ""
        self.edv = ""
        self.classe = ""

        self.botao_voltar.clicked.connect(self.home)
        self.botao_adicionar.clicked.connect(self.escolher_classe)
        self.botao_editar.clicked.connect(self.editar)
        self.load_tabela()

    def editar(self):
        self.load_tabela()

        try:
            index = (self.tabela.selectionModel().currentIndex())
            print(index)
            value = index.sibling(index.row(), index.column()).data()
            print(value)

            row = self.tabela.currentItem().row()
            print("row=", row)
            col = self.tabela.currentItem().column()
            print("col=", col)
            item = self.tabela.horizontalHeaderItem(col).text()
            print("item=", item)

            value_02 = index.sibling(row + 1, index.column()).data()
            print(value_02)

            self.nome = index.sibling(row, 0).data()
            self.edv = index.sibling(row, 1).data()
            self.classe = index.sibling(row, 2).data()
            self.ID = banco_dados.edvColadorador
            self.Data_Nasciento = banco_dados.dataNascFormat
            # self.ID = str(banco_dados.ID_User(self.edv))

            # self.ID = str(standby.colaboradorB[2])
            # self.Data_Nasciento = standby.colaboradorB[4]

            # self.Data_Nasciento = banco_dados.Data_nascimento(self.ID)

            print(self.nome)
            print(self.edv)
            print(self.classe)
            print(self.ID)
            print(self.Data_Nasciento)

            cadastros_menu_adicionar.alterar_classe = True
            self.ficha()

        except:
            pass

    def ficha(self):
        if self.classe == "Aprendiz":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_aprendiz2)

        if self.classe == "Meio_Oficial":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_meio_oficial2)

        if self.classe == "Responsável":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_responsavel2)

        if self.classe == "Manutentor":
            cadastros_menu_editar.label_imagem_patente.setPixmap(self.imagem_manutentor2)

        cadastros_menu_editar.lineEdit_nome.setText(self.nome)
        cadastros_menu_editar.lineEdit_edv.setText(self.edv)
        cadastros_menu_editar.lineEdit_data_nascimento.setText(str(self.Data_Nasciento))

        cadastros_menu_editar.show()
        cadastros_menu.hide()

        print("Nãooo")

    def load_tabela(self):

        self.tabela.setColumnCount(3)
        self.tabela.setColumnWidth(0, 480)
        self.tabela.setColumnWidth(1, 150)
        self.tabela.setColumnWidth(2, 200)

        self.tabela.setHorizontalHeaderLabels(["NOME", "EDV", "CLASSE"])
        self.tabela.setSelectionBehavior(QAbstractItemView.SelectRows)
        print('banco_dados.todosUsers()',banco_dados.todosUsers())

        listUser = banco_dados.todosUsers()
        self.tabela.setRowCount(len(listUser))

        row = 0

        print('--------------- LOAD LIST ---------')
        for x in listUser:
            print('x',x)
            print('name', x['name'])
            print('edv', x['EDV'])
            print('classe', x['jobposition']['typeJob'])
            self.tabela.setItem(row, 0, QTableWidgetItem(x['name']))
            self.tabela.setItem(row, 1, QTableWidgetItem(x['EDV']))
            self.tabela.setItem(row, 2, QTableWidgetItem(x['jobposition']['typeJob']))

            row = row + 1

    def escolher_classe(self):
        print('escolher classee')
        cadastros_menu_leitor.adicionar = True
        cadastros_menu_adicionar.alterar_classe = False
        cadastros_menu_adicionar.show()
        cadastros_menu.hide()

    def home(self):
        Menu02.show()
        cadastros_menu.hide()

class Cadastros_menu_editar(QMainWindow, Ui_Editar_cadastro):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_cancelar.clicked.connect(self.home)
        self.botao_alterar_tag_cartao.clicked.connect(self.leitor)
        self.botao_atualizar.clicked.connect(self.atualizar)
        self.botao_alterar_classe.clicked.connect(self.mudar_classe)

        self.lineEdit_nome.setText("")
        self.lineEdit_data_nascimento.setText("")
        self.lineEdit_edv.setText("")
        self.lineEdit_nome.setPlaceholderText("NOME COMPLETO")
        self.lineEdit_edv.setPlaceholderText("EDV")
        self.lineEdit_data_nascimento.setPlaceholderText("DATA DE NASCIMENTO")

    def leitor(self):
        cadastros_menu_leitor.adicionar = False
        cadastros_menu.ficha()
        cadastros_menu_leitor.opcao = False
        cadastros_menu_leitor.show()
        cadastros_menu_editar.hide()

    def home(self):
        cadastros_menu.show()
        cadastros_menu_editar.hide()

    def mudar_classe(self):
        cadastros_menu_adicionar.show()
        cadastros_menu_editar.hide()

    def atualizar(self):
        self.nome = self.lineEdit_nome.text()
        self.data_nascimento = self.lineEdit_data_nascimento.text()
        self.edv = self.lineEdit_edv.text()
        #self.data = datetime.strptime(f'{self.data_nascimento}', '%d/%m/%Y').date()
        #print(self.data, type(self.data))
        #self.dataFormatada = self.data.strftime('%d/%m/%Y')
        #print(self.dataFormatada, type(self.dataFormatada))
        banco_dados.atualizar_cadastro(self.nome, self.data_nascimento, self.edv, cadastros_menu.ID)

class Cadastros_menu_leitor(QMainWindow, Ui_Aproxime_cartao):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.adicionar = bool
        self.lineEdit_tag_cartao.setText("")
        self.lineEdit_tag_cartao.setFocus()
        self.botao_cancelar.clicked.connect(self.voltar)
        self.botao_registrar.clicked.connect(self.registrar)
        self.tag_cartao = " "

    def voltar(self):
        if self.adicionar == True:
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_leitor.hide()

        else:
            cadastros_menu_editar.show()
            cadastros_menu_leitor.hide()

    def registrar(self):
        self.tag_cartao = self.lineEdit_tag_cartao.text()
        print(self.adicionar)
        # self.adicionar = True
        if not self.tag_cartao == "":
            if self.adicionar == True:
                cadastros_menu_leitor.hide()
                print('------------ ADICIONAR == TRUE -----------')
                print(self.tag_cartao, cadastros_menu_adicionar_ficha_01.nome, cadastros_menu_adicionar_ficha_01.classe, cadastros_menu_adicionar_ficha_01.edv, cadastros_menu_adicionar_ficha_01.data_nascimento )
                banco_dados.adicionar_cadastro(self.tag_cartao, cadastros_menu_adicionar_ficha_01.nome, cadastros_menu_adicionar_ficha_01.classe, cadastros_menu_adicionar_ficha_01.edv, cadastros_menu_adicionar_ficha_01.data_nascimento)
                # usuario_registrado.show()
                # time.sleep(3)
                # usuario_registrado.hide()
                # AQUI FALTA O DELAY ENTRE AS TELAS
                cadastros_menu.show()
                self.lineEdit_tag_cartao.setText("")
                cadastros_menu_adicionar_ficha_01.lineEdit_edv.setText("")
                cadastros_menu_adicionar_ficha_01.lineEdit_nome.setText("")
                cadastros_menu_adicionar_ficha_01.lineEdit_data_nascimento.setText("")
                # usuario_registrado.hide()
                cadastros_menu_leitor.hide()
                cadastros_menu.load_tabela()
                self.lineEdit_tag_cartao.setFocus()

            else:
                self.lineEdit_tag_cartao.setFocus()
                banco_dados.update_tag(self.tag_cartao, )

        else:
            print("Tente novamente")

class Cadastros_menu_adicionar(QMainWindow, Ui_cadastros_classes):
    def __init__(self):
        super().__init__()
        super().setupUi(self)
        self.botao_voltar.clicked.connect(self.home)
        self.botao_aprendiz.clicked.connect(self.aprendiz)
        self.botao_meio_oficial.clicked.connect(self.meio_oficial)
        self.botao_manutentor.clicked.connect(self.manutentor)
        self.botao_responsavel.clicked.connect(self.responsavel)
        self.imagem_aprendiz = QPixmap("imagens\Aprendiz_02.png")
        self.imagem_meio_oficial = QPixmap("imagens\Meio_oficial_02.png")
        self.imagem_manutentor = QPixmap("imagens\Manutentor_02.png")
        self.imagem_responsavel = QPixmap("imagens\Responsavel_02.png")
        self.alterar_classe = False

    def aprendiz(self):
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Aprendiz"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_aprendiz)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                # banco_dados.alterar_classe("Aprendiz",cadastros_menu_editar.lineEdit_edv.text())
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_aprendiz2)
                cadastros_menu_editar.show()
                cadastros_menu_adicionar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def meio_oficial(self):
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Meio_Oficial"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_meio_oficial)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                # banco_dados.alterar_classe("Meio Oficial", cadastros_menu_editar.lineEdit_edv.text())
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_meio_oficial2)
                cadastros_menu_editar.show()
                cadastros_menu_adicionar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def manutentor(self):
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Manutentor"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_manutentor)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                # banco_dados.alterar_classe("Manutentor", cadastros_menu_editar.lineEdit_edv.text())
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_manutentor2)
                cadastros_menu_editar.show()
                cadastros_menu_adicionar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def responsavel(self):
        if self.alterar_classe == False:
            cadastros_menu_adicionar_ficha_01.classe = "Responsável"
            cadastros_menu_adicionar_ficha_01.label_imagem_classe.setPixmap(self.imagem_responsavel)
            cadastros_menu_adicionar_ficha_01.show()
            cadastros_menu_adicionar.hide()

        else:
            try:
                # banco_dados.alterar_classe("Responsável", cadastros_menu_editar.lineEdit_edv.text())
                cadastros_menu_editar.label_imagem_patente.setPixmap(cadastros_menu.imagem_responsavel2)
                cadastros_menu_editar.show()
                cadastros_menu_editar.hide()
                cadastros_menu.load_tabela()

            except Exception as erro:
                print(erro)

    def home(self):
        cadastros_menu.show()
        cadastros_menu_adicionar.hide()

class Cadastros_menu_adicionar_ficha01(QMainWindow, Ui_cadastros_adicionar_ficha01):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

        self.botao_cancelar.clicked.connect(self.home)
        self.botao_avancar.clicked.connect(self.cadastro01)
        self.classe = " "
        self.data_nascimento = " "
        self.edv = " "
        self.nome = " "

        self.lineEdit_nome.setText("")
        self.lineEdit_data_nascimento.setText("")
        self.lineEdit_edv.setText("")
        self.lineEdit_nome.setPlaceholderText("NOME COMPLETO")
        self.lineEdit_edv.setPlaceholderText("EDV")
        self.lineEdit_data_nascimento.setPlaceholderText("DATA DE NASCIMENTO")

    def cadastro01(self):
        self.nome = self.lineEdit_nome.text()
        self.edv = str(self.lineEdit_edv.text())
        self.data_nascimento = self.lineEdit_data_nascimento.text()

        if (self.nome == "") or (self.edv == "") or (self.data_nascimento == ""):
            print("Tente novamente")

        else:
            cadastros_menu_leitor.opcao = True
            print(self.nome)
            print(self.edv)
            print(self.classe)
            cadastros_menu_leitor.show()
            cadastros_menu_adicionar_ficha_01.hide()

    def home(self):
        cadastros_menu_adicionar.show()
        cadastros_menu_adicionar_ficha_01.hide()

class Usuario_registrado(QMainWindow, Ui_Usuario_registrado):
    def __init__(self):
        super().__init__()
        super().setupUi(self)

ap = QApplication(sys.argv)
ap.setStyle("Fusion")
banco_dados = Connection("Banco.db")
Menu01 = Primeiro_Menu()
Menu02 = Segundo_Menu()
Menu01Aprendiz = Primeiro_MenuAPRENDIZ()
Menu01_skill2 = Primeiro_MenuSkill()
liberacao_seguranca = Liberacao_seguranca()
liberacao_atencao = Liberacao_atencao()
liberacao_meio_ambiente = Liberacao_meio_ambiente()
documentos_menu = Documentos_menu()
documentos_de_pecas_menu = Documentos_documentos_de_pecas_menu()
peca01 = Documentos_de_peca_peca01()
peca02 = Documentos_de_peca_peca02()
peca03 = Documentos_de_peca_peca03()
diagrama_eletrico = diagrama_eletrico()
mapa_de_riscos = Mapa_de_riscos()
aviso_liberacao = Aviso_liberacao()
interface_menu = Interface_menu()
interface_menu_botoes = Interface_botoes()
interface_menu_finalidade = Interface_finalidade()
interface_menu_botao_emergencia = Interface_botao_emergencia()
registros_menu = Registros_menu()
cadastros_menu = Cadastros_menu()
cadastros_menu_editar = Cadastros_menu_editar()
cadastros_menu_leitor = Cadastros_menu_leitor()
cadastros_menu_adicionar = Cadastros_menu_adicionar()
cadastros_menu_adicionar_ficha_01 = Cadastros_menu_adicionar_ficha01()
usuario_registrado = Usuario_registrado()
registro_historico_utilizacao = Registro_historico_utilizacao()
sairDef = Sair()
relatos_liberacao = Relatos_liberacao()
cadastro = Adicionar()
standby = Standby()
standby.show()
sys.exit(ap.exec())