import os

# Criando um nome para seu arquivo
nome_arquivo = input('Digite um nome para o arquivo(sem extensão): ')

# Mapeando as extensões
formato_extensao = {
    'txt': 'TEXTO',
    'csv': 'CSV',
    'xml': 'XML'

}

# Interando entre as extensões disponíveis
print('Formato de extensões disponíveis: ')
for ext, descricao in formato_extensao.items():
    print(f'{ext} -> {descricao}')

# Escolha de extensão pelo usuário
escolha_usuario = input('Digite o formato que deseja seu arquivo: ')
if escolha_usuario in formato_extensao:
    arquivo_completo = f'{nome_arquivo}.{escolha_usuario}'
else:
    print('Formato de extensão inválida!')

# Criando o arquivo
try:
    caminho_completo = input('Digite o caminho onde deseja salvar seu arquivo: ')
    caminho_completo = os.path.join(caminho_completo, arquivo_completo)

    with open(caminho_completo, 'w', encoding='UTF-8') as arquivo:
        conteudo = input('Digite o conteúdo do arquivo(sem as aspas): ')
        arquivo.write(conteudo)
    print(f'Arquivo {arquivo_completo} foi criado com sucesso em {caminho_completo}')
except Exception as e:
    print('Ocorreu um erro', e)

# Lendo o arquivo
lendo_arquivo = input('Deseja ver o conteúdo do arquivo? S/N ')
if lendo_arquivo.upper() == 'S':
    try:
        with open(caminho_completo, 'r', encoding='UTF-8') as arquivo:
            lendo = arquivo.read()
        print(f'{arquivo_completo}: {lendo}')
    except FileNotFoundError as e:
        print('Arquivo não encontrado', e)
    except Exception as e:
        print('Ocorreu um erro', e)
else:
    print('Encerrando o programa!')
