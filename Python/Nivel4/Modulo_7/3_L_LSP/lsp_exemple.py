"""
LSP - Liskov Substitution Principle (Princípio da Substituição de Liskov)

Objetos de uma classe derivada devem poder substituir objetos da classe base
sem quebrar a funcionalidade do programa.

Se S é um subtipo de T, então objetos do tipo T podem ser substituídos
por objetos do tipo S sem alterar as propriedades desejáveis do programa.
"""

from abc import ABC, abstractmethod
from typing import List


# ❌ EXEMPLO ERRADO - Violando o LSP
class Bird:
    """Classe base para pássaros"""
    
    def __init__(self, name: str):
        self.name = name
    
    def fly(self) -> None:
        """Todos os pássaros voam... ou não?"""
        print(f"{self.name} está voando!")


class Sparrow(Bird):
    """Pardal - voa normalmente"""
    pass


class Penguin(Bird):
    """Pinguim - NÃO voa! Viola LSP"""
    
    def fly(self) -> None:
        """Pinguins não voam, mas a classe base exige este método"""
        raise Exception(f"{self.name} não pode voar! Pinguins não voam!")
        # ⚠️ Quebra o contrato da classe base!


class Ostrich(Bird):
    """Avestruz - também NÃO voa! Viola LSP"""
    
    def fly(self) -> None:
        """Avestruzes não voam"""
        raise Exception(f"{self.name} não pode voar! Avestruzes não voam!")


# ✅ EXEMPLO CORRETO - Seguindo o LSP
class BirdCorrect:
    """Classe base para pássaros (comportamento comum)"""
    
    def __init__(self, name: str):
        self.name = name
    
    def eat(self) -> None:
        """Todos os pássaros comem"""
        print(f"{self.name} está comendo.")
    
    def make_sound(self) -> None:
        """Todos os pássaros fazem som"""
        print(f"{self.name} está fazendo som.")


class FlyingBird(BirdCorrect):
    """Pássaros que voam"""
    
    def fly(self) -> None:
        """Capacidade de voar"""
        print(f"{self.name} está voando!")


class NonFlyingBird(BirdCorrect):
    """Pássaros que não voam"""
    
    def walk(self) -> None:
        """Capacidade de andar"""
        print(f"{self.name} está andando.")


class SparrowCorrect(FlyingBird):
    """Pardal - voa"""
    pass


class EagleCorrect(FlyingBird):
    """Águia - voa"""
    pass


class PenguinCorrect(NonFlyingBird):
    """Pinguim - não voa, mas nada"""
    
    def swim(self) -> None:
        print(f"{self.name} está nadando!")


class OstrichCorrect(NonFlyingBird):
    """Avestruz - não voa, mas corre rápido"""
    
    def run_fast(self) -> None:
        print(f"{self.name} está correndo muito rápido!")


# Exemplo 2: Formas geométricas
# ❌ VIOLANDO LSP
class Rectangle:
    """Retângulo"""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    def set_width(self, width: float) -> None:
        self._width = width
    
    def set_height(self, height: float) -> None:
        self._height = height
    
    def get_area(self) -> float:
        return self._width * self._height


class Square(Rectangle):
    """Quadrado - VIOLA LSP!"""
    
    def set_width(self, width: float) -> None:
        """Quadrado tem largura = altura"""
        self._width = width
        self._height = width  # ⚠️ Altera comportamento esperado!
    
    def set_height(self, height: float) -> None:
        """Quadrado tem largura = altura"""
        self._width = height  # ⚠️ Altera comportamento esperado!
        self._height = height


# ✅ SEGUINDO LSP
class Shape(ABC):
    """Interface para formas geométricas"""
    
    @abstractmethod
    def get_area(self) -> float:
        """Calcula área da forma"""
        pass


class RectangleCorrect(Shape):
    """Retângulo correto"""
    
    def __init__(self, width: float, height: float):
        self._width = width
        self._height = height
    
    def set_width(self, width: float) -> None:
        self._width = width
    
    def set_height(self, height: float) -> None:
        self._height = height
    
    def get_area(self) -> float:
        return self._width * self._height


class SquareCorrect(Shape):
    """Quadrado correto - NÃO herda de Rectangle!"""
    
    def __init__(self, side: float):
        self._side = side
    
    def set_side(self, side: float) -> None:
        self._side = side
    
    def get_area(self) -> float:
        return self._side * self._side


# Demonstração de uso
if __name__ == "__main__":
    print("=" * 70)
    print("EXEMPLO ERRADO - Violando o LSP")
    print("=" * 70)
    
    birds = [
        Sparrow("Pardal"),
        Penguin("Pinguim"),
        Ostrich("Avestruz")
    ]
    
    print("\nTentando fazer todos os pássaros voarem:")
    for bird in birds:
        try:
            bird.fly()
        except Exception as e:
            print(f"❌ ERRO: {e}")
    
    print("\n⚠️  A substituição quebrou o programa!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO CORRETO - Seguindo o LSP")
    print("=" * 70)
    
    print("\n--- Pássaros que voam ---")
    flying_birds: List[FlyingBird] = [
        SparrowCorrect("Pardal"),
        EagleCorrect("Águia")
    ]
    
    for bird in flying_birds:
        bird.eat()
        bird.fly()  # ✅ Todos podem voar!
        print()
    
    print("--- Pássaros que não voam ---")
    non_flying_birds: List[NonFlyingBird] = [
        PenguinCorrect("Pinguim"),
        OstrichCorrect("Avestruz")
    ]
    
    for bird in non_flying_birds:
        bird.eat()
        bird.walk()  # ✅ Todos podem andar!
        if isinstance(bird, PenguinCorrect):
            bird.swim()
        if isinstance(bird, OstrichCorrect):
            bird.run_fast()
        print()
    
    print("=" * 70)
    print("EXEMPLO: FORMAS GEOMÉTRICAS - Violando LSP")
    print("=" * 70)
    
    def test_rectangle_area(rectangle: Rectangle) -> None:
        """Função que espera um retângulo"""
        rectangle.set_width(5)
        rectangle.set_height(4)
        expected_area = 5 * 4  # 20
        actual_area = rectangle.get_area()
        print(f"Largura: 5, Altura: 4")
        print(f"Área esperada: {expected_area}, Área real: {actual_area}")
        if expected_area == actual_area:
            print("✓ Teste passou!")
        else:
            print("❌ Teste FALHOU! LSP violado!")
    
    print("\nTestando com Rectangle:")
    test_rectangle_area(Rectangle(0, 0))
    
    print("\nTestando com Square (substitui Rectangle):")
    test_rectangle_area(Square(0))  # ⚠️ Quebra a expectativa!
    
    print("\n" + "=" * 70)
    print("EXEMPLO CORRETO: FORMAS GEOMÉTRICAS - Seguindo LSP")
    print("=" * 70)
    
    shapes: List[Shape] = [
        RectangleCorrect(5, 4),
        SquareCorrect(5)
    ]
    
    print("\nCalculando áreas:")
    for i, shape in enumerate(shapes, 1):
        print(f"Forma {i}: Área = {shape.get_area()}")
    
    print("\n" + "=" * 70)
    print("VANTAGENS DO LSP:")
    print("=" * 70)
    print("✓ Subtipos podem substituir tipos base sem quebrar o código")
    print("✓ Garante que hierarquias de classes sejam corretas")
    print("✓ Previne bugs em polimorfismo")
    print("✓ Aumenta confiabilidade do código")
    print("✓ Facilita reutilização e manutenção")
