class FilaNormal:
    codigo:int = 0
    fila = []
    clientesatendidos = []
    senhatual:str = ""

    def gerarsenhatual(self) -> None:
        self.senhatual = f'RM{self.codigo}'

    def resetafila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self.codigo += 1

    def atualizarfila(self) -> None:
        self.resetafila()
        self.gerarsenhatual()
        self.fila.append(self.senhatual)

    def chamarcliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.clientesatendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')


