import requests
import zipfile
import io
import os 
import datetime
import pandas as pd


def soma(a, b):
    """Retorna a soma de dois números."""
    return a + b

def criar_pasta(caminho):
    """Cria uma pasta se ela ainda não existir."""
    os.makedirs(caminho, exist_ok=True)
    print(f"Pasta criada/verificada: {caminho}")

def baixar_e_extrair_zip(url, destino_pasta):
    """Baixa o arquivo ZIP da URL e extrai o conteúdo para a pasta de destino."""
    print(f"Baixando ZIP de: {url}")
    resposta = requests.get(url)
    
    if resposta.status_code == 200:
        with zipfile.ZipFile(io.BytesIO(resposta.content)) as z:
            z.extractall(destino_pasta)
        print(f"Arquivos extraídos com sucesso em: {destino_pasta}")
        return True
    else:
        print(f"Erro ao baixar: Status Code {resposta.status_code}")
        return False
    

def gerar_info_data(ano, mes):
    try:
        data = datetime.date(ano, mes, 1)
    except ValueError:
        return None # Data inválida

    mes_num_2d = data.strftime("%m") # Ex: '01', '09'
    ano_str = str(ano)
    
    # Padrão identificado: Letra fixa (f) + ANO + MÊS 
    prefixo = f'ESTATCAMBIF{ano_str}{mes_num_2d}'
    
    #1. PADRÃO 1 (2025): SEM O -IF-
    if ano == 2025:
        sufixo = f'-{ano_str}{mes_num_2d}.zip'
        
    #2. PADRÃO 2 (2015-2024): COM O -IF-
    elif ano >= 2015 and ano <= 2024:
        sufixo = f'-IF-{ano_str}{mes_num_2d}.zip'
        
    #3. EXCEÇÃO: Anos fora do padrão (2014)
    else: 
        #Não há lógica aplicada aqui.
        return None
    
    url_padrao = prefixo + sufixo 
    
    return{
        'url': f"https://www.bcb.gov.br/content/estatisticas/rankingcambioinstituicoes/{url_padrao}",
        'filename_csv': f"Ranking Instituição {ano_str} {mes_num_2d}.csv"
        }
    

def unificar_bases(pasta_csv):
    lista_dfs = []
    arquivos = os.listdir(pasta_csv)
    
    print(f'Iniciando unificação de {len(arquivos)} arquivos na pasta...')
    
    for nome_arquivo in arquivos: 
        if nome_arquivo.endswith('.csv') and not nome_arquivo.startswith('~'):
            caminho_completo = os.path.join(pasta_csv, nome_arquivo)
            
            try:
                df = pd.read_csv(
                    caminho_completo,
                    sep = ';',
                    encoding = 'latin1', 
                    header = 5,
                    thousands = '.'
                )
                
                partes_nome = nome_arquivo.split(' ')
                if len(partes_nome) >= 4:
                    ano = partes_nome[2]
                    mes = partes_nome[3].split('.')[0]
                    df['Data_Ref'] = f'{ano}-{mes}'
                    
                lista_dfs.append(df)
                print(f'-> {nome_arquivo} carregado ({len(df)} linhas).')
                
            except Exception as e: 
                print(f'ERRO ao ler o CSV {nome_arquivo}: {e}.')
                continue
        if not lista_dfs: 
            print(f'Nenhum DataFrame CSV válido encontrado para unificar.')
            return None
        
        df_consolidado = pd.concat(lista_dfs, ignore_index = True)
        print(f'Bases unificadas com sucesso! Total de linhas: {len(df_consolidado)}.')
        
        return df_consolidado