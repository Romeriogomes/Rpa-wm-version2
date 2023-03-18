#Instalação da lib do Selenium
#pip3 install selenium
#Instalação BeautifulSoup
#pip3 install beautifulsoup4
#Instalação lxml
#pip3 install lxml
#Download do Geckodriver para Firefox ou ChromeDriver para Chrome
#https://github.com/mozilla/geckodriver/releases
#https://chromedriver.chromium.org/downloads
#Salvar dentro da pasta do python descompactado se der erro baixar a ultima verssão e salvar em C:\Users\PL-RV\AppData\Local\Programs\Python\Python311
#pip install webdriver-manager


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome import options
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep
from datetime import date
import pandas as pd
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


#driver = webdriver.Chrome(ChromeDriverManager().install())
headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
    (KHTML, like Gecko) Chrome / 86.0.4240.198Safari / 537.36"}


options = Options()
options.headless = True #executa de forma visivel ou não
#options.headless = add_argument("--headless=new")
navegador = webdriver.Chrome(options=options)
link = "https://app.wefleet.com.br/site/wmrastreamento/Account/Login?ReturnUrl=http://app.wefleet.com.br/site/wmrastreamento#/configuracoes/usuarios"
navegador.get(url=link)

data_Hoje = date.today()
data_Hotem = date.fromordinal(data_Hoje.toordinal()-1)
dataHotenFormat = data_Hotem.strftime("%d/%m/%Y")
inputuser = navegador.find_element(By.NAME,value="email")
inputuser.send_keys("performance@planaltocase.com.br")
inputuser = navegador.find_element(By.NAME,value="senha")
inputuser.send_keys("Planalto123")
sleep(1)
btn_login = navegador.find_element(By.NAME,value="empId")
btn_login.submit()
sleep(1)

wait = WebDriverWait(navegador, 1000)

link = "https://app.wefleet.com.br/site/wmrastreamento#/relatoriosv2/irregularidadesv3"
navegador.get(url=link)


periodo = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@class = "toggle-menu"]'))).click()

selecionar_periodo = wait.until(EC.element_to_be_clickable((By.LINK_TEXT,'Informar o período' ))).click()

data_anterior =wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="datepicker ini hasDatepicker"]'))).click()
data_anterior = navegador.find_element(By.XPATH,value='//*[@class="datepicker ini hasDatepicker"]').clear()
data_anterior = navegador.find_element(By.XPATH,value='//*[@class="datepicker ini hasDatepicker"]').send_keys(dataHotenFormat)
data_anterior =wait.until(EC.element_to_be_clickable((By.XPATH, '//*[@class="datepicker fim hasDatepicker"]'))).click()
data_anterior = navegador.find_element(By.XPATH,value='//*[@class="datepicker fim hasDatepicker"]').clear()
data_anterior = navegador.find_element(By.XPATH,value='//*[@class="datepicker fim hasDatepicker"]').send_keys(dataHotenFormat)

aplicar = navegador.find_element(By.CLASS_NAME,value="btn-apply-data")
aplicar.click()


Visualizar = navegador.find_element(By.XPATH,value='//*[@class="control"]/input').click()

esperar2 = wait.until(EC.visibility_of_element_located((By.XPATH,'//*[@class="pager-info"]/b[@data-bind="text: pageCount"]'))) #espera ate o elemento aparecer na tela


inforPage = navegador.find_element(By.XPATH,value='//*[@class="pager-info"]/b[@data-bind="text: pageCount"]')
inforPage = inforPage.text
ultimaPagina = int(inforPage)+1
print(ultimaPagina)
print(dataHotenFormat)

sleep(2)
dic_Linhas = {'placa':[]}
dic_Linhas1 = {'data':[]}
dic_Linhas2 = {'Descricao':[]}
dic_Linhas3 = {'Padrao':[]}
dic_Linhas4 = {'Valor':[]}
dic_Linhas5 = {'Velocidade':[]}
dic_Linhas6 = {'Endereco':[]}
dic_Linhas7 = {'Motorista':[]}


       
for i in range(1, int(ultimaPagina)):
    
    pageAtual= navegador.find_element(By.XPATH,value='//*[@data-bind="value: txtPage"]').send_keys(i)
    
    ok = navegador.find_element(By.XPATH,value='//*[@class="btn btn-round"]').click()
    sleep(5)
    placas = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: placa"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: placa"]')
    DataDia = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: data"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: data"]')
    Descricaos = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: desc"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: desc"]')
    Padraos = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: padrao"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: padrao"]')
    Valores = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: valor"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: valor"]')
    Velocidades = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: vel"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: vel"]')
    Enderecos = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: end"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: end"]')
    Motoristas = wait.until(EC.element_to_be_clickable((By.XPATH,'//*[@data-bind="text: motorista"]')))\
        .find_elements(By.XPATH,value='//*[@data-bind="text: motorista"]')
  
    
    data = DataDia[0] # ler cada elemento de todos 
    placa = placas[0]
    Descricao = Descricaos[0]
    Padrao = Padraos[0]
    Valor = Valores[0]
    Velocidade = Velocidades[0]
    Endereco = Enderecos[0]
    Motorista = Motoristas[0]


    sleep(2)
    for placa in placas : #loop para gravar cada elemento ao df
        dic_Linhas['placa'].append(placa.text)
        df1 = pd.DataFrame(dic_Linhas,columns=['placa'])
    for data in DataDia :
        dic_Linhas1['data'].append(data.text)
        df2 = pd.DataFrame(dic_Linhas1,columns=['data'])
    for Descricao in Descricaos :        
        dic_Linhas2['Descricao'].append(Descricao.text)
        df3 = pd.DataFrame(dic_Linhas2,columns=['Descricao'])
    for Padrao in Padraos :        
        dic_Linhas3['Padrao'].append(Padrao.text)
        df4 = pd.DataFrame(dic_Linhas3,columns=['Padrao'])     
    for Valor in Valores :        
        dic_Linhas4['Valor'].append(Valor.text)
        df5 = pd.DataFrame(dic_Linhas4,columns=['Valor'])   
    for Velocidade in Velocidades :        
        dic_Linhas5['Velocidade'].append(Velocidade.text) 
        df6 = pd.DataFrame(dic_Linhas5,columns=['Velocidade']) 
    for Endereco in Enderecos :        
        dic_Linhas6['Endereco'].append(Endereco.text) 
        df7 = pd.DataFrame(dic_Linhas6,columns=['Endereco'])        
    for Motorista in Motoristas :       
        dic_Linhas7['Motorista'].append(Motorista.text)   
        df8 = pd.DataFrame(dic_Linhas7,columns=['Motorista'])
    
    
   
dfb = pd.merge(df1, df2, left_index=True, right_index= True)
dfb1 = pd.merge(df3, df4, left_index=True, right_index= True)
dfb2 = pd.merge(df5, df6, left_index=True, right_index= True)
dfb3 = pd.merge(df7, df8, left_index=True, right_index= True)

dfbcsv1 =pd.merge(dfb,dfb1, left_index=True, right_index=True)
dfbcsv2 =pd.merge(dfb2,dfb3, left_index=True, right_index=True)
dfbcsvtotal =pd.merge(dfbcsv1,dfbcsv2, left_index=True, right_index=True)
    
  
dfbcsvtotal.to_csv('relatorio.csv', mode="a", encoding="utf-8", sep=';',index= False, header=None)
  

        
