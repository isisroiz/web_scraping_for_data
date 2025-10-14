import sys
import os
import datetime
import importlib
sys.path.append(r'C:\Users\Isis\Documents\webscrapping_bacen') 
import requests as r  
import pandas as pd
import new_lib as nl
import zipfile as z  # Apelido 'z' para zipfile
import io

print(dir(nl)) 
print(nl.soma(2, 2))
print(nl)
print(pd)


DESTINO_BASE = r'C:\Users\Isis\Documents\webscrapping_bacen\dados'
nl.criar_pasta(DESTINO_BASE) 
DESTINO_ZIP_FILES = os.path.join(DESTINO_BASE, 'zipfiles')
nl.criar_pasta(DESTINO_ZIP_FILES) 
 

ANO_INICIAL = 2015
ANO_FINAL = datetime.date.today().year
print('\n--- INICIANDO FASE DE DOWNLOAD DAS BASES NO BACEN ---')

for ano in range(ANO_INICIAL, ANO_FINAL + 1):
    mes_limite = datetime.date.today().month if ano == ANO_FINAL else 12
    
    for mes in range(1, mes_limite + 1):
        info = nl.gerar_info_data(ano, mes)
        if info is None: continue
        
        url_download = info['url']
        
        if nl.baixar_e_extrair_zip(url_download, DESTINO_ZIP_FILES):
            print(f'Download e extração de {ano}-{mes} concluídos.')
        else:
            print(f'Arquivo não encontrado para {ano}-{mes}. Continuando processo de download.')
            
    
print('---Fim da aquisição. Unificando todas as bases.')
df_consolidado = nl.unificar_bases(DESTINO_ZIP_FILES)

# BLOCO DE EXECUÇÃO MANUAL PARA 2014 (URL QUE NÃO SEGUE PADRÃO): 

URLS_MANUAIS_2014 = [ 
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201412-IF-201412.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201410-AT_2014-10.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201409-IF-201409.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201408-IF-201408.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201407-IF-201407.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201406-IF-201406.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201405-IF-201405.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201404-IF-201404.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201403-IF-201403.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201402-IF-201402.zip',
   r'https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/ESTATCAMBIF201401-IF_201401.zip',
        ]
    
print("--- INICIANDO DOWNLOAD MANUAL PARA 2014 ---")

for url_fixa in URLS_MANUAIS_2014:
    nl.baixar_e_extrair_zip(url_fixa, DESTINO_ZIP_FILES)
    if nl.baixar_e_extrair_zip(url_download, DESTINO_ZIP_FILES):
        print(f'Download e extração de {ano}-{mes} concluídos.')
    else:
        print(f'Arquivo não encontrado para {ano}-{mes}. Continuando processo de download.')
    
print("--- Download de 2014 concluído. ---")

        
