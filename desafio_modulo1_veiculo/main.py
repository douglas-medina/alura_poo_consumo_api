from modelos.carro import Carro
from modelos.moto import Moto

carro_passeio = Carro(
    marca='BMW',
    modelo='320i',
    portas=4
)

carro_transporte = Carro(
    marca='Peugeot',
    modelo='Boxer Minibus',
    portas=5
)

moto_esportiva = Moto(
    marca='BMW',
    modelo='GS1200',
    tipo='Esportiva'
)

moto_viagem = Moto(
    marca='Harley-Davidson',
    modelo='Fat Boy 114',
    tipo='Viagem'
)

def main():
    print(carro_passeio)
    print(carro_transporte)

    print(moto_esportiva)
    print(moto_viagem)




if __name__ == '__main__':
    main()