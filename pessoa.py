class Pessoa:
    def __init__(self, nome, data_nascimento, codigo, salario, estudando=False, trabalhando=False):
        self.__nome = nome
        self.__data_nascimento = data_nascimento
        self.__codigo = codigo
        self._estudando = estudando
        self._trabalhando = trabalhando
        self._salario = salario

    def apresentar(self):
        print(f'Olá sou {self.nome}, minha data de nascimento é {self.data_nascimento}'
              f', meu codigo é {self.codigo}')

        if self.estudando:
            print(f'Estou Estudando')
        else:
            print(f'Não estou estudando')

        if self.trabalhando:
            print(f'Estou trabalhando')
        else:
            print(f'Não estou trabalhando')

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
    def get_salario(self):
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
            self.set_salario()
    def set_estudando(self, status):
        self._estudando = status
        if status:
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

    def apresentar(self):
        print(f'Olá sou {self.nome}, minha data de nascimento é {self.data_nascimento}'
              f', meu codigo é {self.codigo}')

        if self.fome:
            print(f'O {self.nome} está com fome')
        else:
            print(f'O {self.nome} não ta com fome')

        if self.chorando:
            print(f'O {self.nome} ta chorando')
        else:
            print(f'O {self.nome} nao esta chorando')

        if self.dormindo:
            print(f'O {self.nome} esta dormindo')
        else:
            print(f'O {self.nome} nao esta dormindo')

    def mamar(self):
        if not self.fome:
            print('bebe não está com fome')
        else:
            self.fome = False
            self.chorando = False
            print(f'{self.nome} mamou legal ')
            print('bebe não esta mais com fome')

    def dormir(self):
        if not self.fome:
            self.dormindo = True
            print('bebe foi dormir')
        else:
            print('bebe está com fome não pode dormir')




p1 = Pessoa("Lucas", "03/03/2003", "123",1200,True, True)
b1 = Bebe('Bebe','26/01/2025', '1')
b1.apresentar()
print('-_-' * 20)
