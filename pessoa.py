class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, salario, estudando=False, trabalhando=False):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def apresentar(self):
        #print("\n")
        print('-','-' * 20,'-')
        print(f"Olá, sou {self.get_nome()} \n"
              f"meu aniversario é dia: {self.get_data_nascimento()} \n"
              f"n de reg istro: {self.get_codigo()}")
        print(f"Estudando: {'Sim' if self.get_estudando() else 'Não'}")
        print(f"Trabalhando: {'Sim' if self.get_estudando() else 'Não'}")
        if self.get_trabalhando():
            print(f"Salario: {self.get_salario():.2f}")
        print("+","-" * 20,"+")
        print("\n")

    def estudar(self):
        if not self.estudando:
            self.estudando = True
            print(f'{self.nome} começou a estudar')
        elif self.trabalhando and self.trabalhando:
            self.salario += 1000
            print(
                f"{self.nome} "
                f" começou a estudar e aumentou seu salario para "
                f"{self.salario:.2f}"
            )
        else:
            print(f'{self.nome} ja esta estudando')

    def trabalhar(self):
        if not self.trabalhando:
            self.trabalhando = True
            self.salario += 100
            print(f'{self.nome} começou a trabalhar !')
        else:
            print(f'{self.nome} ja está trabalhando !')


    def get_nome(self):
        return self.__nome
    def get_data_nascimento(self):
        return self.__data_nascimento
    def get_codigo(self):
        return self.__codigo
    def get_estudando(self):
        return self._estudando
    def get_trabalhando(self):
        return self._trabalhando
    def get_trabalhando(self):
        return self._salario


    def set_trabalhando(self, status):
        if self._trabalhando and status:
            print(f"Ja esta trabalhando")
        elif not self._trabalhando and not status:
            print(f"que vida boa")
        elif not self._trabalhando and status:
            self._trabalhando = status
            self._salario(100)
        else:
            self._trabalhando = status
            self.set_salario(0)
    def set_estudando(self, status):
        self._estudando = status
        if status and not self._trabalhando:
            self._salario(self._salario() + 100)
    def set_salario(self, salario):
        if salario >= 0:
            self._salario = salario
        else:
            print(f'salario invalido')

class Bebe(Pessoa):
    def __init__(self, nome, data_nascimento, registro, salario=0,
                 estudando=False, trabalhando=False):
        super().__init__(nome, data_nascimento, registro, estudando, trabalhando)
        self.fome = True
        self.chorando = True
        self.dormindo = False

    def mamar(self):
        if self.fome:
            self.fome = False
            self.chorando = False
            print(f"{self.nome} mamou e esta satisfeito.")
        else:
            print(f"{self.nome} não está com fome e não quer mamar.")

    def chorar(self):
        if self.chorando:
            print(f"{self.nome} está chorando")
        else:
            print(f"{self.nome} não está chorando")

    def dormir(self):
        if not self.dormindo:
            if self.fome:
                print(f"{self.nome} está com fome e não consegue dormir")
            else:
                self.dormindo = True
                print(f"{self.nome} foi dormir. shhh, não faça barulho")
        else:
            print(f"{self.nome} ja está dormindo.")

    def apresentar(self):
        super().apresentar()
        print(f"Fome: {'Sim' if self.fome else 'Não'}")
        print(f"Chorando: {'Sim' if self.fome else 'Não'}")
        print(f"Dormindo: {'Não' if self.fome else 'Sim'}")
        print('-' * 20)

p1 = Pessoa("Lucas", "03/03/2003", "123",100,True, True)
b1 = Bebe('Bebe','26/01/2025', '1')
p1.apresentar()
b1.apresentar()
print('-_-' * 20)
