"""
SRP - Single Responsibility Principle (Princípio da Responsabilidade Única)

Uma classe deve ter apenas uma razão para mudar, ou seja, 
uma única responsabilidade.
"""

# ❌ EXEMPLO ERRADO - Violando o SRP
class UserManagerBad:
    """Classe com múltiplas responsabilidades"""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def save_to_database(self):
        """Responsabilidade 1: Persistência de dados"""
        print(f"Salvando usuário {self.name} no banco de dados...")
        # Lógica de salvamento
    
    def send_welcome_email(self):
        """Responsabilidade 2: Envio de e-mail"""
        print(f"Enviando e-mail de boas-vindas para {self.email}...")
        # Lógica de envio de e-mail
    
    def generate_report(self):
        """Responsabilidade 3: Geração de relatório"""
        print(f"Gerando relatório para {self.name}...")
        # Lógica de geração de relatório


# ✅ EXEMPLO CORRETO - Seguindo o SRP
class User:
    """Classe com única responsabilidade: representar um usuário"""
    
    def __init__(self, name: str, email: str):
        self.name = name
        self.email = email
    
    def get_info(self) -> dict:
        """Retorna informações do usuário"""
        return {
            "name": self.name,
            "email": self.email
        }


class UserRepository:
    """Responsabilidade única: Persistência de dados"""
    
    def save(self, user: User) -> None:
        """Salva o usuário no banco de dados"""
        print(f"✓ Salvando usuário {user.name} no banco de dados...")
        # Lógica de salvamento no banco
    
    def find_by_email(self, email: str) -> User:
        """Busca usuário por e-mail"""
        print(f"✓ Buscando usuário com e-mail {email}...")
        # Lógica de busca
        return None


class EmailService:
    """Responsabilidade única: Envio de e-mails"""
    
    def send_welcome_email(self, user: User) -> None:
        """Envia e-mail de boas-vindas"""
        print(f"✓ Enviando e-mail de boas-vindas para {user.email}...")
        # Lógica de envio de e-mail
    
    def send_notification(self, user: User, message: str) -> None:
        """Envia notificação por e-mail"""
        print(f"✓ Enviando notificação para {user.email}: {message}")


class ReportGenerator:
    """Responsabilidade única: Geração de relatórios"""
    
    def generate_user_report(self, user: User) -> str:
        """Gera relatório do usuário"""
        print(f"✓ Gerando relatório para {user.name}...")
        report = f"""
        === RELATÓRIO DO USUÁRIO ===
        Nome: {user.name}
        E-mail: {user.email}
        ===========================
        """
        return report


# Demonstração de uso
if __name__ == "__main__":
    print("=" * 60)
    print("EXEMPLO ERRADO - Violando o SRP")
    print("=" * 60)
    
    bad_user = UserManagerBad("João Silva", "joao@email.com")
    bad_user.save_to_database()
    bad_user.send_welcome_email()
    bad_user.generate_report()
    
    print("\n" + "=" * 60)
    print("EXEMPLO CORRETO - Seguindo o SRP")
    print("=" * 60)
    
    # Criando um usuário
    user = User("Maria Santos", "maria@email.com")
    
    # Cada classe tem sua responsabilidade específica
    repository = UserRepository()
    email_service = EmailService()
    report_generator = ReportGenerator()
    
    # Utilizando cada serviço de forma independente
    repository.save(user)
    email_service.send_welcome_email(user)
    report = report_generator.generate_user_report(user)
    print(report)
    
    print("\n" + "=" * 60)
    print("VANTAGENS DO SRP:")
    print("=" * 60)
    print("✓ Cada classe tem uma única responsabilidade")
    print("✓ Facilita manutenção e testes")
    print("✓ Reduz acoplamento")
    print("✓ Aumenta coesão")
    print("✓ Facilita reutilização de código")
