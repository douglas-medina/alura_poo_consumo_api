from modelos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo) -> None:
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self) -> str:
        status = 'ligado' if self._ligado else 'desligado'
        return f'A motocicleta {self.modelo}, marca {self.marca}, tipo {self.tipo} está {status}'