"""
OCP - Open/Closed Principle (Princípio Aberto/Fechado)

Classes devem estar abertas para extensão, mas fechadas para modificação.
Ou seja, você pode adicionar novas funcionalidades sem alterar o código existente.
"""

from abc import ABC, abstractmethod
from typing import List


# ❌ EXEMPLO ERRADO - Violando o OCP
class DiscountCalculatorBad:
    """Classe que precisa ser modificada sempre que um novo tipo de desconto é adicionado"""
    
    def calculate_discount(self, customer_type: str, price: float) -> float:
        """Calcula desconto baseado no tipo de cliente"""
        if customer_type == "regular":
            return price * 0.0  # Sem desconto
        elif customer_type == "premium":
            return price * 0.10  # 10% desconto
        elif customer_type == "vip":
            return price * 0.20  # 20% desconto
        # ⚠️ Para adicionar novo tipo, precisa MODIFICAR esta classe!
        elif customer_type == "employee":
            return price * 0.30  # 30% desconto
        else:
            return 0.0


# ✅ EXEMPLO CORRETO - Seguindo o OCP
class Discount(ABC):
    """Classe abstrata para descontos (aberta para extensão)"""
    
    @abstractmethod
    def calculate(self, price: float) -> float:
        """Calcula o valor do desconto"""
        pass


class NoDiscount(Discount):
    """Sem desconto"""
    
    def calculate(self, price: float) -> float:
        return 0.0


class RegularDiscount(Discount):
    """Desconto para clientes regulares"""
    
    def calculate(self, price: float) -> float:
        return price * 0.05  # 5% desconto


class PremiumDiscount(Discount):
    """Desconto para clientes premium"""
    
    def calculate(self, price: float) -> float:
        return price * 0.10  # 10% desconto


class VIPDiscount(Discount):
    """Desconto para clientes VIP"""
    
    def calculate(self, price: float) -> float:
        return price * 0.20  # 20% desconto


class EmployeeDiscount(Discount):
    """Desconto para funcionários"""
    
    def calculate(self, price: float) -> float:
        return price * 0.30  # 30% desconto


# ✅ Nova classe adicionada SEM modificar código existente!
class SeasonalDiscount(Discount):
    """Desconto sazonal especial"""
    
    def calculate(self, price: float) -> float:
        return price * 0.15  # 15% desconto


class DiscountCalculator:
    """Calculadora fechada para modificação, mas aceita novos tipos de desconto"""
    
    def calculate_final_price(self, price: float, discount: Discount) -> float:
        """Calcula o preço final após aplicar o desconto"""
        discount_amount = discount.calculate(price)
        return price - discount_amount


# Exemplo avançado: Sistema de notificações
class Notifier(ABC):
    """Interface para notificações (aberta para extensão)"""
    
    @abstractmethod
    def send(self, message: str) -> None:
        """Envia uma notificação"""
        pass


class EmailNotifier(Notifier):
    """Notificação por e-mail"""
    
    def send(self, message: str) -> None:
        print(f"📧 Enviando e-mail: {message}")


class SMSNotifier(Notifier):
    """Notificação por SMS"""
    
    def send(self, message: str) -> None:
        print(f"📱 Enviando SMS: {message}")


class PushNotifier(Notifier):
    """Notificação push"""
    
    def send(self, message: str) -> None:
        print(f"🔔 Enviando notificação push: {message}")


# ✅ Nova notificação adicionada SEM modificar código existente!
class WhatsAppNotifier(Notifier):
    """Notificação por WhatsApp"""
    
    def send(self, message: str) -> None:
        print(f"💬 Enviando WhatsApp: {message}")


class NotificationService:
    """Serviço de notificações (fechado para modificação)"""
    
    def __init__(self):
        self.notifiers: List[Notifier] = []
    
    def add_notifier(self, notifier: Notifier) -> None:
        """Adiciona um novo canal de notificação"""
        self.notifiers.append(notifier)
    
    def notify_all(self, message: str) -> None:
        """Envia notificação por todos os canais configurados"""
        for notifier in self.notifiers:
            notifier.send(message)


# Demonstração de uso
if __name__ == "__main__":
    print("=" * 70)
    print("EXEMPLO ERRADO - Violando o OCP")
    print("=" * 70)
    
    bad_calculator = DiscountCalculatorBad()
    price = 100.0
    
    print(f"Preço original: R$ {price:.2f}")
    print(f"Desconto Regular: R$ {bad_calculator.calculate_discount('regular', price):.2f}")
    print(f"Desconto Premium: R$ {bad_calculator.calculate_discount('premium', price):.2f}")
    print(f"Desconto VIP: R$ {bad_calculator.calculate_discount('vip', price):.2f}")
    print("\n⚠️  Para adicionar novo tipo de desconto, precisa MODIFICAR a classe!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO CORRETO - Seguindo o OCP")
    print("=" * 70)
    
    calculator = DiscountCalculator()
    price = 100.0
    
    print(f"\nPreço original: R$ {price:.2f}")
    print("-" * 70)
    
    # Testando diferentes tipos de desconto
    discounts = [
        ("Sem Desconto", NoDiscount()),
        ("Regular", RegularDiscount()),
        ("Premium", PremiumDiscount()),
        ("VIP", VIPDiscount()),
        ("Funcionário", EmployeeDiscount()),
        ("Sazonal", SeasonalDiscount()),  # ✅ Novo tipo adicionado sem modificar código!
    ]
    
    for name, discount in discounts:
        final_price = calculator.calculate_final_price(price, discount)
        discount_amount = discount.calculate(price)
        print(f"✓ {name:15} | Desconto: R$ {discount_amount:6.2f} | Final: R$ {final_price:6.2f}")
    
    print("\n" + "=" * 70)
    print("EXEMPLO: SISTEMA DE NOTIFICAÇÕES")
    print("=" * 70)
    
    # Criando serviço de notificações
    notification_service = NotificationService()
    
    # Adicionando canais de notificação (extensível!)
    notification_service.add_notifier(EmailNotifier())
    notification_service.add_notifier(SMSNotifier())
    notification_service.add_notifier(PushNotifier())
    notification_service.add_notifier(WhatsAppNotifier())  # ✅ Novo canal!
    
    # Enviando notificação por todos os canais
    print("\nEnviando notificação:")
    notification_service.notify_all("Seu pedido foi aprovado!")
    
    print("\n" + "=" * 70)
    print("VANTAGENS DO OCP:")
    print("=" * 70)
    print("✓ Adiciona funcionalidades SEM modificar código existente")
    print("✓ Reduz risco de bugs em código que já funciona")
    print("✓ Facilita extensão do sistema")
    print("✓ Promove uso de abstrações (interfaces/classes abstratas)")
    print("✓ Código mais flexível e manutenível")
