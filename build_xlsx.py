# TESTES PARA IMPORTAR DADOS PARA O DB AZURE
# SALVAR ESTRUTURAS EM EXCEL
# import os 
# from dotenv import load_dotenv    
import openpyxl
import jpype     
import asposecells     
jpype.startJVM() 
from asposecells.api import Workbook
workbook = Workbook("produto_plano_de_contas.txt")
book.save('produto_plano_de_contas.xlsx')
jpype.shutdownJVM()
    
#def teste ():
    #load_dotenv()
    # estrutura =  os.getenv('RESULT')

    # book.create_sheet('contas')
    # contas_page = book['contas']

    # if estrutura is not None:
    #     if len(estrutura) > 0:
    #         for intem in estrutura:
    #             contas_page.append([item.Modified Date])
    #     else:
    #         print("Nenhum dado encontrado.")
    # else:
    #     print("Nenhum dado na estrutura.")