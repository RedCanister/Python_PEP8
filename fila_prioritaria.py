class FilaPrioritaria:
    codigo: int = 0
    fila: list[str] = []
    cliente_atendidos: list[str] = []
    senha_atual: str = ""

    def gera_senha_atual(self) -> None:
        self.senha_atual = f'PR{str(self.codigo)}'

    def reseta_fila(self) -> None:
        if self.codigo >= 100:
            self.codigo = 0
        else:
            self. codigo += 1

    def atualiza_fila(self) -> None:
        self.reseta_fila()
        self.gera_senha_atual()
        self.fila.append(self.senha_atual)

    def chama_cliente(self, caixa:int) -> str:
        cliente_atual = self.fila.pop(0)
        self.cliente_atendidos.append(cliente_atual)
        return (f'Cliente atual: {cliente_atual}, dirija-se ao caixa: {caixa}')

    def estatisticas(self, dia: str, agencia: str, flag: str) -> dict:
        if flag != 'detail':
            estatistica = {f'{agencia}-{dia}': len(self.cliente_atendidos)}
        else:
            estatistica = {}
            estatistica['dia'] = dia
            estatistica['agencia'] = agencia
            estatistica['clientes_atendidos'] = self.cliente_atendidos
            estatistica['quantidade_clientes_atendidos'] = len(self.cliente_atendidos)

        return estatistica




