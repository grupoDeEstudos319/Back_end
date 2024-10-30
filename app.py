from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato

def main():
    # Criação de um restaurante e itens do cardápio
    restaurante_praca = Restaurante('Praça', 'Gourmet')
    
    # Criação de uma bebida e um prato
    bebida_suco = Bebida('Suco de Melancia', 5.0, 'Grande')
    prato_paozinho = Prato('Pãozinho', 2.00, 'O melhor pão da cidade')
    
    # Aplicar desconto nos itens
    bebida_suco.aplicar_desconto()
    prato_paozinho.aplicar_desconto()
    
    # Adicionar itens ao cardápio
    restaurante_praca.adicionar_no_cardapio(bebida_suco)
    restaurante_praca.adicionar_no_cardapio(prato_paozinho)
    
    # Exibir o cardápio do restaurante
    restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()
