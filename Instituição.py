class Instituicao:
    def __init__(self, nome, data_entrega, codigo):
        self.nome = nome
        self.data_entrega = data_entrega
        self.codigo = codigo

    def apresentar(self):
        print(
            f"Bom dia! Sou {self.nome}, uma instituição de grande relevância no Brasil inteiro."
            f" Minha data de entrega é prevista para {self.data_entrega} e o código de registro é {self.codigo}."
        )

    def entrega(self):
        if not self.data_entrega:
            print(f'{self.data_entrega} começou o seu trabalho')
        else:
            print(f'{self.nome} ja esta em serviço')

    def trabalhar(self):
        if not self.data_entrega:
            self.data_entrega = False
            print(f'{self.nome} não esta em tranalho !')
        else:
            print(f'{self.nome}  !')


class Fornecedor(Instituicao):
    def __init__(self, nome, data_entrega, codigo):
        super().__init__(nome, data_entrega, codigo)
        self.em_entrega = True
        self.turno_manha = True
        self.viajando_exterior = False

    def apresentar(self):
        super().apresentar()
        status_entrega = "fazendo entregas" if self.em_entrega else "não está fazendo entregas"
        status_turno = "no turno da manhã" if self.turno_manha else "fora do turno da manhã"
        status_viagem = "viajando para fora" if self.viajando_exterior else "não está viajando para fora"

        print(f"O {self.nome} {status_entrega}.")
        print(f"O {self.nome} está {status_turno}.")
        print(f"O {self.nome} {status_viagem}.")


p1 = Instituicao("Coca-Cola", "21/02/2025", "707070")
b1 = Fornecedor('Coca-Cola','26/01/2025', '707070')
b1.apresentar()
print('-_-' * 20)
p1.apresentar()
p1.entrega()
p1.trabalhar()