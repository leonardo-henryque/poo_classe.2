class Empresa:

    def __init__(self, nome, data_entrega, codigo):

        self.nome = nome
        self.data_entrega = data_entrega
        self.codigo = codigo

    def apresentar(self):

        print(
            f"Bom dia! Sou {self.nome}, uma instituição de grande relevância no Brasil inteiro."
            f" Minha data de entrega é prevista para {self.data_entrega} e o código de registro é {self.codigo}."
        )

    def funcionarios(self):

        if self.data_entrega:
            print(f"{self.nome} já está em serviço desde {self.data_entrega}.")
        else:
            print(f"{self.nome} ainda não iniciou o funcionamento.")

    def trabalhar(self):

        if not self.data_entrega:
            print(f"{self.nome} não está em trabalho!")
        else:
            print(f"{self.nome} está totalmente operacional!")


class Fornecedor(Empresa):


    def __init__(self, nome, data_entrega, codigo, destino, horario, em_entrega=False):

        super().__init__(nome, data_entrega, codigo)
        self.horario = horario
        self.destino = destino
        self.em_entrega = em_entrega

    def apresentar(self):

        super().apresentar()
        status_entrega = "fazendo entregas" if self.em_entrega else "não está fazendo entregas"
        status_horario = "no turno da manhã" if self.horario else "no turno da noite"
        status_viagem = "está perto do destino" if self.destino else "não está perto do destino"

        print(f"O {self.nome} {status_entrega}.")
        print(f"O {self.nome} está {status_horario}.")
        print(f"O {self.nome} {status_viagem}.")

    def realizar_entrega(self):

        if self.em_entrega:
            print(f"O fornecedor {self.nome} está realizando entregas.")
        else:
            print(f"O fornecedor {self.nome} não está disponível para entregas no momento.")

    def tunro_horario(self):

        if self.horario:
            print(f"o {self.nome} estão no turno da manha")
        else:
            print(f"o {self.nome} estão no turno da  noite ")

    def prazo_destino(self):

        if self.destino:
            print(f"o {self.nome} estão perto do destino")
        else:
            print(f"o {self.nome} estao longe do destino")

p1 = Empresa("Coca-Cola", "maio", "707070")
b1 = Fornecedor("Coca-Cola Fornecimentos", "26/01/2025", "707070", "acre", "17:20" )
b1.apresentar()
print('-_-' * 20)

p1.apresentar()
p1.funcionarios()
p1.trabalhar()
