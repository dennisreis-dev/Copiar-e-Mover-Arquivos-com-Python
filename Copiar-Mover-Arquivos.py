# listar arquivos
import os #Litsa, renomeia e move arquivos
import shutil #copiar arquivos

#arquivos = os.listdir()
#print(arquivos)
#
# renomear
## os.rename('Vendas - 1.xlsx', 'Vendas 1.xlsx')
#
# mover
##os.rename('Vendas - 1.xlsx', 'Vendas\Vendas - 1.xlsx')
#
# copiar arquivos
#shutil.copy2('Vendas - 1.xlsx', 'Vendas\Vendas - 1.xlsx')

lista_arquivos = os.listdir()

for arquivo in lista_arquivos:
    if 'xlsx' in arquivo:
        if "Compras" in arquivo:
            # jogar pra pasta de compras
            os.rename(arquivo, f'Compras//{arquivo}')
        elif "Vendas" in arquivo:
            # jogar pra pasta de vendas
            os.rename(arquivo, f'Vendas//{arquivo}')