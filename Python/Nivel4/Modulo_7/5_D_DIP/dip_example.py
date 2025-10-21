"""
DIP - Dependency Inversion Principle (Princípio da Inversão de Dependência)

1. Módulos de alto nível não devem depender de módulos de baixo nível.
   Ambos devem depender de abstrações.

2. Abstrações não devem depender de detalhes.
   Detalhes devem depender de abstrações.
"""

from abc import ABC, abstractmethod
from typing import List


# ❌ EXEMPLO ERRADO - Violando o DIP
class MySQLDatabase:
    """Implementação concreta de banco de dados MySQL"""
    
    def connect(self) -> None:
        print("🔌 Conectando ao MySQL...")
    
    def save_data(self, data: str) -> None:
        print(f"💾 Salvando no MySQL: {data}")


class UserServiceBad:
    """Classe de alto nível DEPENDE de implementação concreta (baixo nível)"""
    
    def __init__(self):
        # ⚠️ Dependência direta de classe concreta!
        self.database = MySQLDatabase()
    
    def save_user(self, user: str) -> None:
        self.database.connect()
        self.database.save_data(user)
        # Se mudar para PostgreSQL, precisa MODIFICAR esta classe!


# ✅ EXEMPLO CORRETO - Seguindo o DIP
class Database(ABC):
    """Abstração (interface) para banco de dados"""
    
    @abstractmethod
    def connect(self) -> None:
        pass
    
    @abstractmethod
    def save_data(self, data: str) -> None:
        pass
    
    @abstractmethod
    def get_data(self, id: str) -> str:
        pass


class MySQLDatabaseCorrect(Database):
    """Implementação concreta - MySQL"""
    
    def connect(self) -> None:
        print("🔌 Conectando ao MySQL...")
    
    def save_data(self, data: str) -> None:
        print(f"💾 Salvando no MySQL: {data}")
    
    def get_data(self, id: str) -> str:
        print(f"📖 Buscando no MySQL: ID {id}")
        return f"Dados do MySQL (ID: {id})"


class PostgreSQLDatabase(Database):
    """Implementação concreta - PostgreSQL"""
    
    def connect(self) -> None:
        print("🔌 Conectando ao PostgreSQL...")
    
    def save_data(self, data: str) -> None:
        print(f"💾 Salvando no PostgreSQL: {data}")
    
    def get_data(self, id: str) -> str:
        print(f"📖 Buscando no PostgreSQL: ID {id}")
        return f"Dados do PostgreSQL (ID: {id})"


class MongoDBDatabase(Database):
    """Implementação concreta - MongoDB"""
    
    def connect(self) -> None:
        print("🔌 Conectando ao MongoDB...")
    
    def save_data(self, data: str) -> None:
        print(f"💾 Salvando no MongoDB: {data}")
    
    def get_data(self, id: str) -> str:
        print(f"📖 Buscando no MongoDB: ID {id}")
        return f"Dados do MongoDB (ID: {id})"


class UserService:
    """Classe de alto nível DEPENDE de abstração (não de implementação)"""
    
    def __init__(self, database: Database):
        # ✅ Recebe abstração via injeção de dependência
        self.database = database
    
    def save_user(self, user: str) -> None:
        self.database.connect()
        self.database.save_data(user)
    
    def get_user(self, id: str) -> str:
        return self.database.get_data(id)


# Exemplo 2: Sistema de notificações
# ❌ VIOLANDO DIP
class EmailSenderBad:
    """Implementação concreta de envio de e-mail"""
    
    def send_email(self, message: str) -> None:
        print(f"📧 Enviando e-mail: {message}")


class NotificationServiceBad:
    """Depende diretamente de implementação concreta"""
    
    def __init__(self):
        # ⚠️ Acoplamento forte!
        self.email_sender = EmailSenderBad()
    
    def notify(self, message: str) -> None:
        self.email_sender.send_email(message)
        # Para adicionar SMS, precisa modificar esta classe!


# ✅ SEGUINDO DIP
class MessageSender(ABC):
    """Abstração para envio de mensagens"""
    
    @abstractmethod
    def send(self, message: str) -> None:
        pass


class EmailSender(MessageSender):
    """Implementação concreta - E-mail"""
    
    def send(self, message: str) -> None:
        print(f"📧 Enviando e-mail: {message}")


class SMSSender(MessageSender):
    """Implementação concreta - SMS"""
    
    def send(self, message: str) -> None:
        print(f"📱 Enviando SMS: {message}")


class PushNotificationSender(MessageSender):
    """Implementação concreta - Push Notification"""
    
    def send(self, message: str) -> None:
        print(f"🔔 Enviando notificação push: {message}")


class NotificationService:
    """Depende de abstração, não de implementação concreta"""
    
    def __init__(self, senders: List[MessageSender]):
        # ✅ Recebe lista de abstrações
        self.senders = senders
    
    def notify(self, message: str) -> None:
        """Envia notificação por todos os canais configurados"""
        for sender in self.senders:
            sender.send(message)


# Exemplo 3: Sistema de pagamento
class PaymentProcessor(ABC):
    """Abstração para processamento de pagamentos"""
    
    @abstractmethod
    def process_payment(self, amount: float) -> bool:
        pass


class CreditCardProcessor(PaymentProcessor):
    """Processador de cartão de crédito"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"💳 Processando pagamento de R$ {amount:.2f} via Cartão de Crédito")
        return True


class PayPalProcessor(PaymentProcessor):
    """Processador PayPal"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"💰 Processando pagamento de R$ {amount:.2f} via PayPal")
        return True


class PixProcessor(PaymentProcessor):
    """Processador PIX"""
    
    def process_payment(self, amount: float) -> bool:
        print(f"⚡ Processando pagamento de R$ {amount:.2f} via PIX")
        return True


class OrderService:
    """Serviço de pedidos - depende de abstração"""
    
    def __init__(self, payment_processor: PaymentProcessor):
        # ✅ Injeção de dependência via abstração
        self.payment_processor = payment_processor
    
    def create_order(self, amount: float) -> None:
        print(f"\n🛒 Criando pedido de R$ {amount:.2f}...")
        success = self.payment_processor.process_payment(amount)
        if success:
            print("✓ Pedido criado com sucesso!")
        else:
            print("❌ Falha ao processar pagamento!")


# Demonstração de uso
if __name__ == "__main__":
    print("=" * 70)
    print("EXEMPLO ERRADO - Violando o DIP")
    print("=" * 70)
    
    print("\n--- Serviço de Usuário (acoplado ao MySQL) ---")
    user_service_bad = UserServiceBad()
    user_service_bad.save_user("João Silva")
    print("\n⚠️  Para trocar o banco, precisa MODIFICAR a classe UserServiceBad!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO CORRETO - Seguindo o DIP")
    print("=" * 70)
    
    print("\n--- Usando MySQL ---")
    mysql_db = MySQLDatabaseCorrect()
    user_service_mysql = UserService(mysql_db)
    user_service_mysql.save_user("Maria Santos")
    user_service_mysql.get_user("123")
    
    print("\n--- Usando PostgreSQL ---")
    postgres_db = PostgreSQLDatabase()
    user_service_postgres = UserService(postgres_db)
    user_service_postgres.save_user("Pedro Oliveira")
    user_service_postgres.get_user("456")
    
    print("\n--- Usando MongoDB ---")
    mongo_db = MongoDBDatabase()
    user_service_mongo = UserService(mongo_db)
    user_service_mongo.save_user("Ana Costa")
    user_service_mongo.get_user("789")
    
    print("\n✓ Trocamos o banco SEM modificar a classe UserService!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO: NOTIFICAÇÕES - Seguindo DIP")
    print("=" * 70)
    
    # Configurando diferentes canais de notificação
    email = EmailSender()
    sms = SMSSender()
    push = PushNotificationSender()
    
    print("\n--- Notificação apenas por E-mail ---")
    notification_service1 = NotificationService([email])
    notification_service1.notify("Seu pedido foi aprovado!")
    
    print("\n--- Notificação por E-mail e SMS ---")
    notification_service2 = NotificationService([email, sms])
    notification_service2.notify("Seu código de verificação: 123456")
    
    print("\n--- Notificação por todos os canais ---")
    notification_service3 = NotificationService([email, sms, push])
    notification_service3.notify("Promoção especial: 50% de desconto!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO: PAGAMENTOS - Seguindo DIP")
    print("=" * 70)
    
    # Testando diferentes formas de pagamento
    print("--- Pagamento com Cartão de Crédito ---")
    credit_card = CreditCardProcessor()
    order_service1 = OrderService(credit_card)
    order_service1.create_order(150.00)
    
    print("\n--- Pagamento com PayPal ---")
    paypal = PayPalProcessor()
    order_service2 = OrderService(paypal)
    order_service2.create_order(250.00)
    
    print("\n--- Pagamento com PIX ---")
    pix = PixProcessor()
    order_service3 = OrderService(pix)
    order_service3.create_order(99.90)
    
    print("\n" + "=" * 70)
    print("VANTAGENS DO DIP:")
    print("=" * 70)
    print("✓ Reduz acoplamento entre módulos")
    print("✓ Facilita troca de implementações")
    print("✓ Facilita testes (mock de dependências)")
    print("✓ Código mais flexível e extensível")
    print("✓ Inversão de controle (IoC)")
    print("✓ Promove uso de injeção de dependência")
