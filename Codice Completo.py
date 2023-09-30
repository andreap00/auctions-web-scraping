## THE CODE IS ALMOST DONE BUT STILL NOT COMPLETE

"#### Relevant libraries"
    
from urllib.request import Request, urlopen
from bs4 import BeautifulSoup
from unidecode import unidecode
from datetime import datetime
import pandas as pd
import locale
import time
import http.client
from datetime import datetime
import re

  
"#### Auxiliary lists"
  
artists = ['Pedro Portugal', 'Pedro Proença', 'Sofia Areal', 'Cabrita Reis',
            'Calapez', 'Graça Morais', 'Julião Sarmento', 'Palolo',
            'Raul Perez', 'Batarda', 'Noronha da Costa', 'Sena', 'Parente',
            'Jorge Martins', 'Álvaro Lapa', 'José de Guimarães', 'Escada',
            'Angelo de Souza', 'Manuel Baptista', 'Paula Rego', 'René Bertholo',
            'Areal', 'João Vieira', 'Nikias', 'Lourdes de Castro',
            'Ana Hatherly', 'Calvet', 'Cargaleiro', 'Bual', 'Figueiredo Sobral',
            'Pomar', 'Amado', 'Cesariny', 'Pedro Leitão', 'Neves e Sousa',
            'Sá Nogueira', 'Nadir Afonso', 'Júlio Resende', 'Hogan',
            'Ceslestino Alves', 'Joaquim Rodrigo', 'Silva Lino',
            'Candido da Costa Pinto', 'Murteira', 'Vieira da Silva',
            'Dominguez Alvarez', 'Vidigal', 'Botelho', 'João Reis', 'Victorino',
            'António Soares', 'Dórdio Gomes', 'Abel Salazar', 'Abel Manta',
            'Eduardo Viana', 'Francis Smith', 'Falcão Trigoso', 'Simão da Veiga',
            'Acácio Lino', 'Abel Cardoso', 'António Saúde', 'António Carneiro',
            'Aurélia de Sousa', 'Veloso Salgado', 'João Vaz', 'Columbano',
            'Sousa Pinto', 'José Malhoa', 'Artur Loureiro', 'Cruzeiro Seixas',
            'Marques de Oliveira', 'Alfredo Keil', 'Almada Negreiros',
            'Celestino Alves', 'Angelo de Sousa']
    
artists_full = ['Pedro Portugal', 'Pedro Proença', 'Sofia Areal',
                'Pedro Cabrita Reis', 'Pedro Calapez', 'Graça Morais',
                'Juliao Sarmento', 'Joao Antonio da Silva Palolo', 'Raul Perez',
                'Eduardo Batarda', 'Luis Noronha da Costa', 'Antonio Sena',
                'Guilherme Parente', 'Jorge Martins', 'Alvaro Lapa',
                'Jose de Guimaraes', 'Jose Escada', 'Angelo de Souza',
                'Manuel Baptista', 'Paula Rego', 'Rene Bertholo',
                'Antonio Santiago Areal', 'Joao Vieira', 'Nikias Spakinakis',
                'Lourdes Castro', 'Ana Hatherly', 'Carlos Calvet',
                'Manuel Cargaleiro', 'Artut Bual', 'Figueiredo Sobral',
                'Julio Pomar', 'Maria Fernanda Amado', 'Mario Cesariny',
                'Pedro Leitao', 'Albano Sousa', 'Rolando Sa Nogueira',
                'Nadir Afonso', 'Julio Resende', 'Joao Hogan',
                'Ceslestino Alves', 'Joaquim Rodrigo', 'Antonio Silva Lino',
                'Candido da Costa Pinto', 'Jaime Murteira',
                'Maria Helena Vieira da Silva', 'Dominguez Alvarez',
                'Ana Vidigal', 'Carlos Botelho', 'Joao Reis', 'Tulio Victorino',
                'Antonio Soares', 'Dordio Gomes', 'Abel Salazar', 'Abel Manta',
                'Eduardo Viana', 'Francis Smith', 'Falcao Trigoso',
                'Simao da Veiga', 'Acacio Lino', 'Abel Cardoso', 'Manuel Saude',
                'Antonio Carneiro', 'Aurelia de Sousa', 'Veloso Salgado',
                'Joao Vaz', 'Columbano Bordalo Pinheiro',
                'Jose Julio de Souza Pinto', 'Jose Malhoa', 'Artur Loureiro',
                'Artur Manuel Cruzeiro Seixas', 'Joao Marques de Oliveira',
                'Alfredo Keil', 'Almada Negreiros', 'Celestino Alves',
                'Angelo de Sousa']
    
medias = [['oleo', 'oil'],
          ['guache', 'gouache'],
          ['pastel'],
          ['acrilico', 'acrilic', 'acrylic'],
          ['serigrafia', 'serigraphy'],
          ['litografia', 'lithograph'],
          ['tempera', 'temper'],
          ['tinta-da-china', 'tinta da china', 'chinese ink'],
          ['aguatinta', 'aquatint'],
          ['tinta', 'ink'],
          ['carvao', 'charcoal'],
          ['grafite', 'graphite'],
          ['lapis de cor', 'colored pencils'],
          ['lapis de cera', 'ceras', 'crayon'],
          ['lapis', 'pencil'],
          ['caneta', 'pen'],
          ['gravura', 'engraving'],
          ['aguarela', 'watercolor'],
          ['sanguinea', 'blood'],
          ['agua-forte', 'etching'],
          ['mista', 'mixed']]
    
supports = [['platex'],
            ['papel', 'paper'],
            ['tela', 'canvas'],
            ['madeira', 'wood'],
            ['aglomerado', 'chipboard'],
            ['contraplacado', 'plywood'],
            ['cartao', 'cardboard'],
            ['cartolina'],
            ['placas para xilogravura', 'xylography plates'],
            ['pano', 'cloth'],
            ['azulejo', 'tile'],
            ['mdf', 'hardboard']]
    
signed_yes = ['assinado', 'assinada', 'signed']
signed_no = ['nao assinado', 'nao assinada', 'unigned']
    
dated = ['datado no verso de', 'datado de', 'datada no verso de', 'datada de',
         'datados de', 'datadas de', 'datado de ', 'datada de ', 'datado',
         'datada', 'dated ', 'dated']
 
   
"#### Palácio do Correio Velho"
   
pcv_data = []
start = time.time()

print("Starting.. ", datetime.fromtimestamp(start))
    
for artist in artists:   
  print("ts=%s artist=%s" % (datetime.fromtimestamp(time.time()), artist) )
  for i in range(1, 25):
    print("ts=%s artist=%s page=%s" % (datetime.fromtimestamp(time.time()), artist, i) )
    artist_url = f'https://www.pcv.pt/search-results?query={unidecode(artist.lower()).replace(" ", "%2B")}&past=1&pageNum={i}'
    artist_req = Request(artist_url , headers={'User-Agent': 'Mozilla/5.0'})
    try:
      print("Open ", artist_url)
      artist_page = urlopen(artist_req).read()
    except http.client.IncompleteRead:
      try:
        print("try ", artwork_req)
        artwork_page = urlopen(artwork_req).read()
      except http.client.IncompleteRead as e:
        artwork_page = e.partial
    artist_soup = BeautifulSoup(artist_page, "html.parser")
    artworks = artist_soup.find_all(
      class_ = 'col-6 col-md-4 col-lg-3 mt-3 mb-5 lotListItem')        
    if artworks == []:
      break
    for artwork in artworks[:]:
      title = artwork.find(class_ ="search-lot-title").contents
      state = artwork.find(class_ ="realized mb-2").contents[0].strip()
      print("ts=%s artist=%s page=%s artwork=%s" % (datetime.fromtimestamp(time.time()), artist, i, title) )
      if state == 'Passed':
        artworks.remove(artwork)
      else:
        count = 0
        for element in unidecode(artist).lower().split():
          if element in unidecode(str(title)).lower():
            count += 1
        if count == 0:
          artworks.remove(artwork)                     
        else: 
          artwork_data = {}
          artwork_data["Artist"] = artists_full[artists.index(artist)]
          artwork_data["Auction house"] = 'Palácio do Correio Velho'                  
          href = artwork.find('a')['href']
          artwork_url= f'https://www.pcv.pt{href}'
          artwork_data["Source"] = artwork_url
          artwork_req = Request(
            artwork_url , headers={'User-Agent': 'Mozilla/5.0'}
          )
          try:
            print("Open ", artwork_url)
            artwork_page = urlopen(artwork_req).read()
          except http.client.IncompleteRead:
            try:
              print("Try ", artwork_url)
              artwork_page = urlopen(artwork_req).read()
            except http.client.IncompleteRead as e:
              artwork_page = e.partial
          artwork_soup = BeautifulSoup(artwork_page, "html.parser")
          description = unidecode(str(artwork_soup.find(id ="itemOverviewTranslatable").find('p')).lower()).replace('<p class="mb-2">', "").replace('\n', "").replace('<br/>', "").replace('dim. aprox.', "").replace('Dim. aprox.', "").replace('dim. approx.', "").replace('Dim. aprox.', "").replace('</p>', "").replace(' cm', " ").strip()
          if unidecode(artist).lower() not in description:
            artworks.remove(artwork)
          else:
            description= description.replace(
              unidecode(artist).lower(), "")
            artwork_data["Price (€)"] = float(artwork_soup.find(class_ ="lotRealizedPrice mb-1").contents[2].strip().replace('€',"").replace(',', "")[:-3])
            date = artwork_soup.find(
              class_ = "dateTime").contents[0].split()
            artwork_data["Auction date"] = datetime.strptime(f"{date[1].replace(',', '')} {date[0]} {date[2]}", "%d %B %Y").strftime("%A, %d %B %Y")
            n = 1
            for elements in medias:
              for element in elements:
                if element in description:
                  artwork_data[f"Media {n}"] = elements[-1]
                  description = description.replace(
                    element,"")
                  n += 1
                  break
              if n == 4:
                break
            for elements in supports:
              for element in elements:
                if element in description:
                  artwork_data["Support"] = elements[-1]
                  description = description.replace(
                    element, "")
                  break
            if '"' in description:
              title_aux = description.split('"', 2)
              try:
                artwork_data["Title"] = title_aux[1]
                description = description.replace(
                    '"' + title_aux[1] + '"', "")
              except:
                pass
            if ' x ' in description:
              dim_aux = description.split(' x ', 1)
              left = dim_aux[0].rsplit(' ', 1)
              right = dim_aux[1].split(' ', 1)
              try:
                artwork_data["Hight (cm)"] = float(
                  left[1].replace(",", "."))
                artwork_data["Width (cm)"] = float(
                  right[0].replace(",", "."))
                if len(right) == 1:
                  description = left[0]
                else:
                  description = left[0] + right[1]
                description = description.replace(f"{left[1]} x {right[0]}", "")
              except:
                pass
            run = 0
            for element in signed_no:
              if element in description:
                artwork_data["Signed (Yes/No)"] = 'No'
                description = description.replace(
                  element, "")
                run = 1
                break
            if run == 0:
              for element in signed_yes:
                if element in description:
                  artwork_data["Signed (Yes/No)"] = 'Yes'
                  description = description.replace(
                    element, "")
                  break
            for element in dated:
              if element in description:
                artwork_data["Creation"] = description.split(element, 1)[1].split(' ', 1)[0].replace('approximate', "").replace(':', "").replace(',', "").replace(';', "").strip()
                description = description.replace(element, "").replace(artwork_data["Creation"], "")
                break
            artwork_data["Description"] = description
            pcv_data.append(artwork_data)
    
pcv_output = pd.DataFrame(
  pcv_data, columns = [
    "Artist", "Auction date", "Title", "Creation", "Hight (cm)",
    "Width (cm)", "Media 1", "Media 2", "Media 3", "Support",
    "Signed (Yes/No)", "Auction house", "Price (€)", "Source", 
    "Description"])

out_path = "/home/users/marco/Downloads/andrea/pcv_output_lourdes_v01.xlsx"
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
pcv_output.to_excel(writer, sheet_name = 'Data', index = False)
writer.close()

end = time.time()
print("end first action house!", datetime.fromtimestamp(end))
print("tot: ", round(end-start,2), "sec")





"#### Cabral Moncada Leilões"

  
cml_data = []
\
for artist in artists:
    print("ts=%s artist=%s" % (datetime.fromtimestamp(time.time()), artist) )
    cml_all_artworks = []   
    for i in range(0, 320, 32):  
        print("ts=%s artist=%s page=%s" % (datetime.fromtimestamp(time.time()), artist, i) )           
        artist_url = f'https://www.cml.pt/cml.nsf/Pesquisa.xsp!start={i}&query={unidecode(artist.lower()).replace(" ", "%20")}'
        artist_req = Request(artist_url , headers={'User-Agent': 'Mozilla/5.0'})
        try:  
          print("Open ", artist_url)
          artist_page = urlopen(artist_req).read()
        except http.client.IncompleteRead:
          try:
            time.sleep(10)
            artwork_page = urlopen(artwork_req).read()
          except http.client.IncompleteRead as e:
            artwork_page = e.partial
        except:
          continue
        artist_soup = BeautifulSoup(artist_page, "html.parser")
        artworks = artist_soup.find_all(
          class_ = 'mdl-cell mdl-card mdl-shadow--4dp portfolio-card loteCard')
        if artworks == []:
          break
        for artwork in artworks[:]:     
          print("ts=%s artist=%s page=%s artwork=%s" % (datetime.fromtimestamp(time.time()), artist, i, title) )       
          state = str(artwork.find_all(class_ ="mdl-tooltip"))
          if 'Retirado' in state:
            continue
          author = artwork.find(class_ ="dsp_autor")
          if author == None:
            continue
          author = author.contents
          if unidecode(artist).lower() not in unidecode(str(author)).lower():
            continue                
          artwork_data = {}                
          try:
            artwork_data["Price (€)"] = float(unidecode(str(artwork.find(class_ = "statusDiv"))).split('EUR ', 1)[1].split('</span>', 1)[0].replace(',', ""))
          except:
            continue                    
          artwork_data["Artist"] = artists_full[artists.index(artist)]
          artwork_data["Auction house"] = 'Cabral Moncada Leilões'            
          artwork_url = artwork.find('a')['href']
          artwork_data["Source"] = artwork_url
          artwork_req = Request(
            artwork_url , headers={'User-Agent': 'Mozilla/5.0'})
          try:
            artwork_page = urlopen(artwork_req).read()
          except http.client.IncompleteRead:
            try:
              artwork_page = urlopen(artwork_req).read()
            except http.client.IncompleteRead as e:
              artwork_page = e.partial
          artwork_soup = BeautifulSoup(artwork_page, "html.parser")
          try:
            date = str(artwork_soup.find(
              class_ = "tituloSessao").contents[2]).split(" ")
            month = date[0].replace('<span>\xa0|\xa0', '')
            artwork_data["Auction date"] = datetime.strptime(f"{date[1].replace(',', '')} {month} {date[2].replace('</span>', '')}", "%d %B %Y").strftime("%A, %d %B %Y")
          except:
            try:
              date = artwork_soup.find(class_ = "mdl-cell mdl-cell--8-col").contents[3].split('a partir')[0].replace('\nEncerra', "").split('de')
              locale.setlocale(locale.LC_ALL, 'pt_pt.UTF-8')
              date_pt = datetime.strptime(f"{date[0].replace(' ', '')} {date[1].replace(' ', '')} {date[2].replace(' ', '')}", "%d %B %Y")
              locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')
              artwork_data["Auction date"] = date_pt.strftime("%A, %d %B %Y")
            except:
              pass                
          artwork_data["Title"] = str(artwork_data["Source"]).rsplit("/", 1)[1].replace("-", " ").replace("   ", " - ").replace("  ", ", ").replace("%28", "(").replace("%29", ")")            
          description = unidecode(str(artwork.find(class_ = "mdl-card__supporting-text")).lower()).split(':detalheslote', 1)[1].replace('pt">', "").replace('</div>', "").replace('<br/>', "").replace('</a>', "")
          if 'dimensoes (altura x comprimento x largura) -' in description:
            find_dim = description.split(
              'dimensoes (altura x comprimento x largura) - ', 1)
            dim = description.split(
              'dimensoes (altura x comprimento x largura) - ', 1)[1]
            if ' x ' in dim:
              dim_aux = dim.split(' x ', 1)
              try:
                left = dim_aux[0].rsplit(' ', 1)[1]
              except:
                left = dim_aux[0]
              right = dim_aux[1].split(' ', 1)[0].replace('\n', "")
              if right[-1] == ",":
                right = right[:-1]
              if right[-2:] == "cm":
                right = right[:-2]
              try:
                artwork_data["Hight (cm)"] = float(left.replace(",", "."))
                artwork_data["Width (cm)"] = float(right.replace(",", "."))
                description = find_dim[0]
              except:
                pass
            else:
              artwork_data["Hight (cm)"] = float(dim.split(' ', 1)[0].replace(",", "."))
          elif ' x ' in description:
            dim_aux = description.split(' x ', 1)
            left = dim_aux[0].rsplit(' ', 1)[1]
            right = dim_aux[1].split(' ', 1)[0].replace('\n', "")
            if right[-1] == ",":
              right = right[:-1]
            if right[-2:] == "cm":
              right = right[:-2]
            try:
              artwork_data["Hight (cm)"] = float(left.replace(",", "."))
              artwork_data["Width (cm)"] = float(right.replace(",", "."))
              description = description.replace(f"{left} x {right}", "")
            except:
              pass
          for element in dated:
            if element in description:
              artwork_data["Creation"] = description.split(element, 1)[1].split(' ', 2)[1].replace('</span>\n', "").replace(':', "").replace(',', "").replace(';', "").strip()
              description = description.replace(element, "").replace(artwork_data["Creation"], "")
              break      
          n = 1
          for elements in medias:
            for element in elements:
              if element in description:
                artwork_data[f"Media {n}"] = elements[-1]
                description = description.replace(element,"")
                n += 1
                break
            if n == 4:
              break
          for elements in supports:
            for element in elements:
              if element in description:
                artwork_data["Support"] = elements[-1]
                description = description.replace(element, "")
                break           
          run = 0
          for element in signed_no:
            if element in description:
              artwork_data["Signed (Yes/No)"] = 'No'
              description = description.replace(element, "")
              run = 1
              break
          if run == 0:
            for element in signed_yes:
              if element in description:
                artwork_data["Signed (Yes/No)"] = 'Yes'
                description = description.replace(element, "")
                break                    
          artwork_data["Description"] = description           
          cml_data.append(artwork_data)
            
cml_output = pd.DataFrame(
    cml_data, columns = [
        "Artist", "Auction date", "Title", "Creation", "Hight (cm)",
        "Width (cm)", "Media 1", "Media 2", "Media 3", "Support",
        "Signed (Yes/No)", "Auction house", "Price (€)", "Source",
        "Description"])


out_path = "/home/users/marco/Downloads/andrea/pcv_output_lourdes_v02.xlsx"
writer = pd.ExcelWriter(out_path , engine='xlsxwriter')
cml_output.to_excel(writer, sheet_name = 'Data', index = False)
writer.close()

end = time.time()
print("end second action house!", datetime.fromtimestamp(end))
print("tot: ", round(end-start,2), "sec")





"#### Veritas Art Auctioneers"
   
ver_data = []
start = time.time()

print("Starting.. ", datetime.fromtimestamp(start))
    
 
for artist in artists:  
  print("ts=%s artist=%s" % (datetime.fromtimestamp(time.time()), artist) )
  for i in range(1, 25):
    print("ts=%s artist=%s page=%s" % (datetime.fromtimestamp(time.time()), artist, i) )
    artist_url = f'https://veritas.art/en/search/previous/{i}/?q={unidecode(artist.lower()).replace(" ", "+")}'
    artist_req = Request(artist_url , headers={'User-Agent': 'Mozilla/5.0'})
    try:
      print("Open ", artist_url)
      artist_page = urlopen(artist_req).read()
    except http.client.IncompleteRead:
      try:
        print("try ", artwork_req)
        artwork_page = urlopen(artwork_req).read()
      except http.client.IncompleteRead as e:
        artwork_page = e.partial
    artist_soup = BeautifulSoup(artist_page, "html.parser")
    artworks = artist_soup.find_all(
      class_ = 'card-lot')        
    if artworks == []:
      break
    a=0
    for artwork in artworks[:]:
      a+=1
      title_element = artwork.find(class_="card-lot__name")
      name = artwork.find(class_="card-lot__author")
      if name == None:
        artworks.remove(artwork)
      else:
        name = name.contents    
        if title_element:
            title = title_element.contents
        else:
            title = "Untitled"
        print("ts=%s artist=%s page=%s artwork=%s" % (datetime.fromtimestamp(time.time()), artist, i, title) )
        count = 0
        doublecount = 0
        for element in unidecode(artist).lower().split():
          if element in unidecode(str(name)).lower():
            count += 1
          doublecount += 1
        if count != doublecount:
          artworks.remove(artwork)                     
        else: 
          artwork_data = {}
          artwork_data["Artist"] = artists_full[artists.index(artist)]
          artwork_data["Auction house"] = 'VERITAS Art Auctioneers'                  
          href = artwork.find('a')['href']
          artwork_url= f'{href}'
          artwork_data["Source"] = artwork_url
          cookie = {'wordpress_logged_in_106bbd91953433fe84c3a6ff0a062309': 'pernigo.andrea@gmail.com|1697038775|sNCUjzIVmJUYwswG6dCJCB9AXz9wy73EocWl2vlUFTl|47fc39c8210a87de6203339adeb969786408ed1df6ffaf1e13d53dec46f5de13'}
          cookie_string = '; '.join([f'{key}={value}' for key, value in cookie.items()])
          artwork_req = Request(
            artwork_url , headers={'User-Agent': 'Mozilla/5.0', 'Cookie': cookie_string,}
          ) 
          try:
            print("Open ", artwork_url)
            artwork_page = urlopen(artwork_req).read()
          except http.client.IncompleteRead:
            try:
              print("Try ", artwork_url)
              artwork_page = urlopen(artwork_req).read()
            except http.client.IncompleteRead as e:
              artwork_page = e.partial
          artwork_soup = BeautifulSoup(artwork_page, "html.parser")
          prices = artwork_soup.find_all(class_ = 'price')
          if not prices:
            artworks.remove(artwork)  
          else:
            price = prices[1].text.strip()
            if price == '0':
              artworks.remove(artwork)
            else:
              sections = (artwork_soup.find_all('div', class_ ="lot-info__section"))
              fourth_section = sections[3]
              description_elements = fourth_section.find_all('p')
              description = (unidecode(str(description_elements[0]).lower()).replace('<br/>', " ").replace('\n', "").replace('<p>',"").replace('</p>',"")).replace('\r',"").strip()
              final_description = description
              if ' cm' in description:
                words = description.split()
                measures = words[words.index('cm')-1]        
              elif 'cm' in description:
                words = description.split()
                for item in words:
                  if 'cm' in item:
                    measures = item.replace('cm', "").strip()
              else:
                if len(description_elements) > 1:
                  measures = description_elements[1].get_text(strip=True)
                  measures = measures.split('cm', 1)
                  measures = measures[0].replace('(mancha/image)', "").replace('(papel/sheet)', "").strip()
                else:
                  measures = None
              artwork_data["Price (€)"] = float(price.replace('.',""))
              date = sections[1].find('p').get_text(strip=True)
              artwork_data["Auction date"] = datetime.strptime(date, '%d %B %Y').strftime('%Y-%m-%d')
              n = 1
              for elements in medias:
                for element in elements:
                  if element in description:
                    artwork_data[f"Media {n}"] = elements[-1]
                    description = description.replace(
                      element,"")
                    n += 1
                    break
                if n == 4:
                  break
              for elements in supports:
                for element in elements:
                  if element in description:
                    artwork_data["Support"] = elements[-1]
                    description = description.replace(
                      element, "")
                    break
              artwork_data["Title"] = artwork_soup.find(class_ ="title name").get_text(strip=True).replace('"',"")
              if measures == None:
                artwork_data["Hight (cm)"] = None
                artwork_data["Width (cm)"] = None
              else:  
                if 'xx' in measures:
                  measures = measures.replace('xx', 'x')
                if 'x' in measures:
                  dim_aux = measures.split('x')
                  left = dim_aux[0].replace(",", ".")
                  right = dim_aux[1].replace(",", ".")
                  artwork_data["Hight (cm)"] = float(left)
                  artwork_data["Width (cm)"] = float(right)
              run = 0
              for element in signed_no:
                if element in description:
                  artwork_data["Signed (Yes/No)"] = 'No'
                  description = description.replace(
                    element, "")
                  run = 1
                  break
              if run == 0:
                for element in signed_yes:
                  if element in description:
                    artwork_data["Signed (Yes/No)"] = 'Yes'
                    description = description.replace(
                      element, "")
                    break
              for element in dated:
                if element in description:
                  artwork_data["Creation"] = description.split(element, 1)[1].split(' ', 1)[0].replace('approximate', "").replace(':', "").replace(',', "").replace(';', "").strip()
                  description = description.replace(element, "").replace(artwork_data["Creation"], "")
                  break
              artwork_data["Description"] = final_description
              ver_data.append(artwork_data)
    
ver_output = pd.DataFrame(
  ver_data, columns = [
    "Artist", "Auction date", "Title", "Creation", "Hight (cm)",
    "Width (cm)", "Media 1", "Media 2", "Media 3", "Support",
    "Signed (Yes/No)", "Auction house", "Price (€)", "Source", 
    "Description"])

out_path = "/Users/OSPITE/OneDrive/Desktop/Tesi Nova/Phyton/ver_output_v03.xlsx"
writer =  pd.ExcelWriter(out_path , engine='xlsxwriter')
ver_output.to_excel(writer, sheet_name = 'Data', index = False)
writer.close()

end = time.time()
print("end third action house!", datetime.fromtimestamp(end))
print("tot: ", round(end-start,2), "sec")

