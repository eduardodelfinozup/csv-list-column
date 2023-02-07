# -*- coding: utf-8 -*-
# !/usr/bin/python3

import os, sys,csv
sys.path.append('/jobs/')
from pathlib import Path

# TODO CRIA A PASTA arquivo DENTRO arquivocsv
# Path('./arquivo').mkdir(exist_ok=True)
# with open('arquivo/' + name_arquivo_csv + '.csv', 'a', newline='') as saida:

# TODO CRIA A PASTA arquivo DENTRO Downloads
# Path('/home/eduardo/Downloads/recentes/arquivo').mkdir(exist_ok=True)
# with open('/home/eduardo/Downloads/recentes/arquivo/' + name_arquivo_csv + '.csv', 'w', newline='') as saida:
# ---------------------------------------------------------------------------------------------------------------------



# TODO: PRIMEIRO CRIAR O ARQUIVO CSV  E AS COLUNAS
def gerar_colunas(name_arquivo_csv, colunas):
    try:
        # TODO Cria a pasta arquivo caso não exista
        Path('./arquivo').mkdir(exist_ok=True)

        # TODO: aqui usamos o 'w' para abri-lo para gravação
        with open('./arquivo/' + name_arquivo_csv + '.csv', 'w', encoding='utf_8', newline='') as saida:

            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            escrever.writerow(colunas)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()


def gerar_csv(name_arquivo_csv, rows):
    try:
        # TODO: aqui usamos o 'a' para continuar a gravação
        with open('./arquivo/' + name_arquivo_csv + '.csv', 'a', encoding='utf_8', newline='') as saida:
            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            for registro in rows:
                escrever.writerow(registro)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()
        if saida.closed:
            print('Loading...')
            print('------------------------------------CARREGADO------------------------------------------------------')


def gerar_txt(name_arquivo_csv, rows):
    try:
        # TODO: aqui usamos o 'a' para continuar a gravação
        with open('./arquivo/' + name_arquivo_csv + '.txt', 'a', encoding='utf_8', newline='') as saida:
            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            for registro in rows:
                escrever.writerow(registro)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()
        if saida.closed:
            print('Loading...')
            print('------------------------------------CARREGADO------------------------------------------------------')


def gerar_registro_in_csv(name_arquivo_csv, rows):
    try:
        # TODO: aqui usamos o 'a' para continuar a gravação
        with open('./arquivo/' + name_arquivo_csv + '.csv', 'a', encoding='utf_8', newline='') as saida:
            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            escrever.writerow(rows)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()
        if saida.closed:
            print('------------------------------------CARREGADO------------------------------------------------------')


def gerarArquivoProcvCsv(name_arquivo_csv, rows):
    try:
        # TODO: aqui usamos o 'a' para continuar a gravação
        with open('./arquivo_procv/' + name_arquivo_csv + '.csv', 'a', encoding='utf_8', newline='') as saida:
            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            escrever.writerow(rows)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()
        if saida.closed:
            print('------------------------------------CARREGADO------------------------------------------------------')



def csv_separado_por_linha(name_arquivo_csv):
    nome_ficheiro = name_arquivo_csv
    THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
    my_file = os.path.join(THIS_FOLDER, 'arquivo/' + nome_ficheiro + '.csv')

    with open(my_file, encoding='utf_8') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        csv_reader.__next__()
        for row in csv_reader:
            print(row[0] + ', ' + row[1])

def delimitador_csv(name_arquivo_csv, delimitador):
    try:
        nome_ficheiro = name_arquivo_csv
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'arquivo/' + nome_ficheiro + '.csv')

        with open(my_file, encoding='utf_8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter = delimitador)
            csv_reader.__next__()

            listRow = list()
            for row in csv_reader:
                listRow.append(row)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        return listRow


def csv_separado_por_virgula(name_arquivo_csv):
    try:
        nome_ficheiro = name_arquivo_csv
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'arquivo/' + nome_ficheiro + '.csv')

        with open(my_file, encoding='utf_8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()

            listRow = list()
            for row in csv_reader:
                listRow.append(row)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        return listRow



def csv_separado_por_espacos(name_arquivo_csv):
    try:
        nome_ficheiro = name_arquivo_csv
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'arquivo/' + nome_ficheiro + '.csv')

        with open(my_file, encoding='utf_8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter='')
            csv_reader.__next__()

            listRow = list()
            for row in csv_reader:
                listRow.append(row)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        return listRow


def csv_separado_por_ponto_virgula(name_arquivo_csv):
    try:
        nome_ficheiro = name_arquivo_csv
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'arquivo/' + nome_ficheiro + '.csv')

        with open(my_file, encoding='utf_8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=';')
            csv_reader.__next__()

            listRow = list()
            for row in csv_reader:
                listRow.append(row)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        return listRow

#----------------------------------------------NOVO MODELO--------------------------------------------------------------


def ler_csv_separado_por_virgula_dir(caminho_gerado):
    try:

        with open(caminho_gerado, encoding='utf_8') as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            csv_reader.__next__()

            listRow = list()
            for row in csv_reader:
                listRow.append(row)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        return listRow


def gerar_registro_in_dir(caminho_gerado, rows):
    try:
        # TODO: aqui usamos o 'a' para continuar a gravação
        with open(caminho_gerado, 'a', encoding='utf_8', newline='') as saida:
            escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
            escrever.writerow(rows)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        saida.close()
        if saida.closed:
            print('------------------------------------CARREGADO------------------------------------------------------')


#-----------------------------------------------------------------------------------------------------------------------

# TODO: PRIMEIRO CRIAR O ARQUIVO CSV  E AS COLUNAS
def criar_colunas_dir(dir, pathComplet, colunas):
    try:
        # TODO Cria a pasta arquivo caso não exista
        Path(dir + str('/arquivo')).mkdir(exist_ok=True)

        if isFile(pathComplet) == False:
            # TODO: aqui usamos o 'w' para abri-lo para gravação
            with open(pathComplet, 'w', encoding='utf_8', newline='') as saida:
                escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
                escrever.writerow(colunas)
                saida.close()
        else:
            print('Colunas já existem...')

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        print('ok')


# TODO: PRIMEIRO CRIAR O ARQUIVO CSV  E AS COLUNAS
def criar_colunas_dir_procv(dir, pathComplet, colunas):
    try:
        # TODO Cria a pasta arquivo caso não exista
        Path(dir + str('/arquivo_procv')).mkdir(exist_ok=True)

        if isFile(pathComplet) == False:
            # TODO: aqui usamos o 'w' para abri-lo para gravação
            with open(pathComplet, 'w', encoding='utf_8', newline='') as saida:
                escrever = csv.writer(saida, delimiter=',', lineterminator='\n')
                escrever.writerow(colunas)
                saida.close()
        else:
            print('Colunas já existem...')

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        print('ok')


#-----------------------------------------------------------------------------------------------------------------------

def isFile(pathComplet):
    return os.path.isfile(pathComplet)

#----------------------------------------------NOVO MODELO--------------------------------------------------------------