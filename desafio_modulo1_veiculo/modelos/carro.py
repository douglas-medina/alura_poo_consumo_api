from modelos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas) -> None:
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self) -> str:
        status = 'ligado' if self._ligado else 'desligado'
        return f'O veículo {self.modelo}, marca {self.marca} tem {self.portas} e está {status}'