import os
import shutil
import pdfplumber
import re

# Função para identificar o modelo do PDF
def identificar_modelo_pdf(pdf_path):
    # Função para ler o conteúdo do PDF com pdfplumber
    texto = ""
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            texto += page.extract_text()

    # Exemplo: Identificando o modelo com base em uma palavra-chave
    if re.search(r'Barueri', texto):
        return 'modelo_1'
    elif re.search(r'CURITIBA', texto):
        return 'modelo_2'
    else:
        return 'modelo_desconhecido'
0
# Função para mover o arquivo para a pasta correta
def mover_arquivo(pdf_path, destino):
    try:
        if not os.path.exists(destino):
            os.makedirs(destino)
        shutil.move(pdf_path, destino)
        print(f"Arquivo movido para: {destino}")
    except Exception as e:
        print(f"Erro ao mover o arquivo {pdf_path}: {e}")

# Função principal para processar a pasta
def processar_pasta_pdfs(pasta_origem, pasta_destino_modelo1, pasta_destino_modelo2):
    for arquivo in os.listdir(pasta_origem):
        if arquivo.endswith(".pdf"):
            caminho_pdf = os.path.join(pasta_origem, arquivo)
            modelo = identificar_modelo_pdf(caminho_pdf)

            if modelo == 'modelo_1':
                mover_arquivo(caminho_pdf, pasta_destino_modelo1)
            elif modelo == 'modelo_2':
                mover_arquivo(caminho_pdf, pasta_destino_modelo2)
            else:
                print(f"Modelo desconhecido para o arquivo: {arquivo}")

# Definir os caminhos das pastas
pasta_origem = "C:\\Users\\jhennifer.nascimento\\nfs\\pdf\\PDF"
pasta_destino_modelo1 = "Z:\\INFORMATICA\\Jhennifer\\novo\\Barueri"
pasta_destino_modelo2 = "Z:\\INFORMATICA\\Jhennifer\\novo\\Curitiba"

# Chamar a função para processar a pasta de PDFs
processar_pasta_pdfs(pasta_origem, pasta_destino_modelo1, pasta_destino_modelo2)

