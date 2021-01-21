from selenium import webdriver
import geckodriver_autoinstaller
import pdfkit
import re
def gerarHtml(stringDiv,titulo):
    var = '<html><meta charset="utf-8"/><body><h1>'+titulo+'</h1>'
    var +='<div>'
    var +=stringDiv;
    var +='</div>'
    var +='</body>'
    var +='</html>'
    return var

geckodriver_autoinstaller.install()  # Check if the current version of geckodriver exists
                                     # and if it doesn't exist, download it automatically,
                                     # then add geckodriver to path

driver = webdriver.Firefox()
driver.get("https://www.pegacifra.com.br/cifras/violao.html")
#assert "Python" in driver.title

elems = driver.find_elements_by_xpath("//a[@href]")
arrayUrls=[]
#pega a lista de musicas do top 100
for elem in elems:
    links= elem.get_attribute("href")
    
    if re.search("cifras\/.+_(\d+).html", str(links)):
        arrayUrls.append(str(links))

##perccore e gerar o pdf das musicas
contador=0
for urlsFiltro in arrayUrls:
    print(urlsFiltro)
    driver.get(urlsFiltro)
    contador+=1
    titulo = driver.execute_script("return document.getElementsByClassName('music')[0].innerHTML")
    val = driver.execute_script("return document.getElementById('tmpac').innerHTML")
    tituloComContador= str(contador)+'.'+titulo
    conteudoHtml= gerarHtml(val,tituloComContador)
    print(conteudoHtml)
    try:
        pdfkit.from_string(conteudoHtml, './violao/'+tituloComContador+'.pdf')
    except:
        print('problema na musica',titulo)
    
        
#finaliza broser
driver.quit();    