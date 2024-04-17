#from fila_normal import filanormal
from fila_prioritaria import FilaPrioritaria

# fila_teste = filanormal()
# fila_teste.atualizarfila()
# fila_teste.atualizarfila()
# fila_teste.atualizarfila()
#
# print(fila_teste.chamarcliente(5))
# print(fila_teste.chamarcliente(10))

fila_teste_2 = FilaPrioritaria()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
fila_teste_2.atualiza_fila()
print(fila_teste_2.chama_cliente(10))
print(fila_teste_2.chama_cliente(1))
print(fila_teste_2.estatisticas("10/01/1993", 198, "detail"))