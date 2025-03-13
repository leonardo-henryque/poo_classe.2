class Instituicao:
    def __init__(self, nome, data_entrega, codigo):
        self._nome = nome
        self._data_entrega = data_entrega
        self.__codigo = codigo

    def apresentar(self):
        print(
            f"Bom dia! Sou {self._nome}, uma instituição de grande relevância no Brasil inteiro."
            f" Minha data de entrega é prevista para {self._data_entrega} e o código de registro é {self.__codigo}."
        )

    def entrega(self):
        if not self._data_entrega:
            print(f'{self._data_entrega} começou o seu trabalho')
        else:
            print(f'{self._nome} ja esta em serviço')

    def trabalhar(self):
        if not self._data_entrega:
            self.data_entrega = False
            print(f'{self._nome} não esta em tranalho !')
        else:
            print(f'{self._nome}  !')

    def get_nome(self):
        return self._nome
    def get_data_nascimento(self):
        return self._data_entrega
    def get_codigo(self):
        return self.__codigo


    def set_nome(self, status):
        self._nome = status
        print(f"A instituição da {self._nome} é mundial mente famosa.")
    def set_entrega(self, status):
        if self._data_entrega and status:
            print(f"A {self._data_entrega}, ja está em entrega ")
        elif not self._data_entrega and not status:
            print(f"A {self._data_entrega}, não esta em entrega")
    def set___codigo(self, status):
        self.__codigo = status
        print(f"O codigo é {self.__codigo}")


class Fornecedor(Instituicao):
    def __init__(self, nome, data_entrega, codigo):
        super().__init__(nome, data_entrega, codigo)
        self.em_entrega = True
        self.turno_manha = True
        self.viajando_exterior = False

    def apresentar(self):
        super().apresentar()
        status_entrega = "está fazendo entregas" if self.em_entrega else "não está fazendo entregas"
        status_turno = "no turno da manhã" if self.turno_manha else "fora do turno da manhã"
        status_viagem = "viajando para fora" if self.viajando_exterior else "não está viajando para fora"

        print(f"O fornecedor da  {self._nome} {status_entrega}.")
        print(f"O fornecedor da {self._nome} está {status_turno}.")
        print(f"O fornecedor da {self._nome} {status_viagem}.")


p1 = Instituicao("Coca-Cola", "21/02/2025", "707070")
b1 = Fornecedor('Coca-Cola','26/01/2025', '707070')
b1.apresentar()
print('-_-' * 20)
p1.apresentar()
p1.entrega()
p1.trabalhar()