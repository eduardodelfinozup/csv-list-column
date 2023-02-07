import sys
sys.path.append('/formatador/')
from util.csv_util import delimitador_csv as ler_csv_virgula

def executar_formatador(name_csv, coluna, delimiter_):
    try:
        var = list()
        for customerList in ler_csv_virgula(name_csv, delimiter_):
            parametro = customerList[coluna]
            print("'" + str(parametro) + "',")
            var.append(str(parametro))
        createTxt(str(var).replace("[","").replace("]",""))
        totalVar = getTotal(var)
        print("TOTAL ENCONTRADO: ", totalVar)

    except Exception as ex:
        print('ERROR: %s' % ex)

    finally:
        print("PROCESSAMENTO REALIZADO ...")

        return ''
def createTxt(s):
    with open('novo-arquivo/parametros_formatados.txt',"w") as arquivo:
        arquivo.writelines(s)
        arquivo.close()

def getTotal(var):
    return len(var)

def main():
    try:
        #---------------------------------------------------------------------------------------------------------------
        name_csv = '{{inputs.nome_arquivo_csv}}'
        coluna = {{inputs.posicao_coluna}}
        delimitador = '{{inputs.delimitador_csv}}'

        #---------------------------------------------------------------------------------------------------------------

        if not name_csv:
            print('Voce esqueceu passar o nome do arquivo csv')
        else:
            executar_formatador(name_csv, coluna, delimitador)

    except Exception as ex:
        print('ERROR: %s' % ex)
    finally:
        print('OK')


if __name__ == '__main__':
    main()
