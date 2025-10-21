"""
ISP - Interface Segregation Principle (Princípio da Segregação de Interface)

Os clientes não devem ser forçados a depender de interfaces que não utilizam.
É melhor ter várias interfaces específicas do que uma interface geral.
"""

from abc import ABC, abstractmethod


# ❌ EXEMPLO ERRADO - Violando o ISP
class Worker(ABC):
    """Interface grande que força implementação de métodos não utilizados"""
    
    @abstractmethod
    def work(self) -> None:
        """Trabalhar"""
        pass
    
    @abstractmethod
    def eat(self) -> None:
        """Comer"""
        pass
    
    @abstractmethod
    def sleep(self) -> None:
        """Dormir"""
        pass


class HumanWorker(Worker):
    """Trabalhador humano - usa todos os métodos"""
    
    def work(self) -> None:
        print("👷 Humano trabalhando...")
    
    def eat(self) -> None:
        print("🍽️  Humano comendo...")
    
    def sleep(self) -> None:
        print("😴 Humano dormindo...")


class RobotWorker(Worker):
    """Robô - NÃO come nem dorme, mas é FORÇADO a implementar!"""
    
    def work(self) -> None:
        print("🤖 Robô trabalhando...")
    
    def eat(self) -> None:
        """Robô não come, mas precisa implementar"""
        raise NotImplementedError("Robôs não comem!")  # ⚠️ Problema!
    
    def sleep(self) -> None:
        """Robô não dorme, mas precisa implementar"""
        raise NotImplementedError("Robôs não dormem!")  # ⚠️ Problema!


# ✅ EXEMPLO CORRETO - Seguindo o ISP
class Workable(ABC):
    """Interface específica para trabalho"""
    
    @abstractmethod
    def work(self) -> None:
        pass


class Eatable(ABC):
    """Interface específica para alimentação"""
    
    @abstractmethod
    def eat(self) -> None:
        pass


class Sleepable(ABC):
    """Interface específica para sono"""
    
    @abstractmethod
    def sleep(self) -> None:
        pass


class HumanWorkerCorrect(Workable, Eatable, Sleepable):
    """Humano implementa todas as interfaces que precisa"""
    
    def work(self) -> None:
        print("👷 Humano trabalhando...")
    
    def eat(self) -> None:
        print("🍽️  Humano comendo...")
    
    def sleep(self) -> None:
        print("😴 Humano dormindo...")


class RobotWorkerCorrect(Workable):
    """Robô implementa APENAS a interface que precisa"""
    
    def work(self) -> None:
        print("🤖 Robô trabalhando 24/7...")


# Exemplo 2: Sistema de impressão
# ❌ VIOLANDO ISP
class MultiFunctionPrinter(ABC):
    """Interface grande que nem todas as impressoras suportam"""
    
    @abstractmethod
    def print_document(self, document: str) -> None:
        pass
    
    @abstractmethod
    def scan_document(self) -> str:
        pass
    
    @abstractmethod
    def fax_document(self, document: str) -> None:
        pass
    
    @abstractmethod
    def photocopy_document(self, document: str) -> None:
        pass


class ModernPrinter(MultiFunctionPrinter):
    """Impressora moderna - tem todas as funções"""
    
    def print_document(self, document: str) -> None:
        print(f"🖨️  Imprimindo: {document}")
    
    def scan_document(self) -> str:
        print("📷 Escaneando documento...")
        return "documento_escaneado.pdf"
    
    def fax_document(self, document: str) -> None:
        print(f"📠 Enviando fax: {document}")
    
    def photocopy_document(self, document: str) -> None:
        print(f"📋 Fazendo fotocópia: {document}")


class SimplePrinter(MultiFunctionPrinter):
    """Impressora simples - só imprime, mas é FORÇADA a implementar tudo"""
    
    def print_document(self, document: str) -> None:
        print(f"🖨️  Imprimindo: {document}")
    
    def scan_document(self) -> str:
        raise NotImplementedError("Esta impressora não escaneia!")  # ⚠️
    
    def fax_document(self, document: str) -> None:
        raise NotImplementedError("Esta impressora não envia fax!")  # ⚠️
    
    def photocopy_document(self, document: str) -> None:
        raise NotImplementedError("Esta impressora não faz fotocópias!")  # ⚠️


# ✅ SEGUINDO ISP
class Printer(ABC):
    """Interface específica para impressão"""
    
    @abstractmethod
    def print_document(self, document: str) -> None:
        pass


class Scanner(ABC):
    """Interface específica para escaneamento"""
    
    @abstractmethod
    def scan_document(self) -> str:
        pass


class Fax(ABC):
    """Interface específica para fax"""
    
    @abstractmethod
    def fax_document(self, document: str) -> None:
        pass


class Photocopier(ABC):
    """Interface específica para fotocópia"""
    
    @abstractmethod
    def photocopy_document(self, document: str) -> None:
        pass


class SimplePrinterCorrect(Printer):
    """Impressora simples - implementa APENAS o que precisa"""
    
    def print_document(self, document: str) -> None:
        print(f"🖨️  Imprimindo: {document}")


class ModernPrinterCorrect(Printer, Scanner, Fax, Photocopier):
    """Impressora moderna - implementa todas as interfaces necessárias"""
    
    def print_document(self, document: str) -> None:
        print(f"🖨️  Imprimindo: {document}")
    
    def scan_document(self) -> str:
        print("📷 Escaneando documento...")
        return "documento_escaneado.pdf"
    
    def fax_document(self, document: str) -> None:
        print(f"📠 Enviando fax: {document}")
    
    def photocopy_document(self, document: str) -> None:
        print(f"📋 Fazendo fotocópia: {document}")


class ScannerPrinter(Printer, Scanner):
    """Impressora com scanner - implementa apenas 2 interfaces"""
    
    def print_document(self, document: str) -> None:
        print(f"🖨️  Imprimindo: {document}")
    
    def scan_document(self) -> str:
        print("📷 Escaneando documento...")
        return "documento_escaneado.pdf"


# Demonstração de uso
if __name__ == "__main__":
    print("=" * 70)
    print("EXEMPLO ERRADO - Violando o ISP")
    print("=" * 70)
    
    print("\n--- Trabalhadores ---")
    human = HumanWorker()
    robot = RobotWorker()
    
    # Humano funciona perfeitamente
    print("\nHumano:")
    human.work()
    human.eat()
    human.sleep()
    
    # Robô tem problemas
    print("\nRobô:")
    robot.work()
    try:
        robot.eat()  # ❌ Erro!
    except NotImplementedError as e:
        print(f"❌ ERRO: {e}")
    
    try:
        robot.sleep()  # ❌ Erro!
    except NotImplementedError as e:
        print(f"❌ ERRO: {e}")
    
    print("\n⚠️  Interface muito grande força implementações desnecessárias!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO CORRETO - Seguindo o ISP")
    print("=" * 70)
    
    print("\n--- Trabalhadores ---")
    human_correct = HumanWorkerCorrect()
    robot_correct = RobotWorkerCorrect()
    
    print("\nHumano:")
    human_correct.work()
    human_correct.eat()
    human_correct.sleep()
    
    print("\nRobô:")
    robot_correct.work()
    print("✓ Robô não precisa implementar eat() e sleep()!")
    
    print("\n" + "=" * 70)
    print("EXEMPLO: IMPRESSORAS - Violando ISP")
    print("=" * 70)
    
    simple = SimplePrinter()
    print("\nImpressora Simples:")
    simple.print_document("relatorio.pdf")
    
    try:
        simple.scan_document()  # ❌ Erro!
    except NotImplementedError as e:
        print(f"❌ ERRO: {e}")
    
    print("\n" + "=" * 70)
    print("EXEMPLO CORRETO: IMPRESSORAS - Seguindo ISP")
    print("=" * 70)
    
    print("\n--- Impressora Simples ---")
    simple_correct = SimplePrinterCorrect()
    simple_correct.print_document("relatorio.pdf")
    print("✓ Não precisa implementar scan, fax, photocopy!")
    
    print("\n--- Impressora Moderna (Multifuncional) ---")
    modern = ModernPrinterCorrect()
    modern.print_document("contrato.pdf")
    modern.scan_document()
    modern.fax_document("documento.pdf")
    modern.photocopy_document("carteira.pdf")
    
    print("\n--- Impressora com Scanner ---")
    scanner_printer = ScannerPrinter()
    scanner_printer.print_document("foto.jpg")
    scanner_printer.scan_document()
    print("✓ Implementa apenas print e scan!")
    
    print("\n" + "=" * 70)
    print("VANTAGENS DO ISP:")
    print("=" * 70)
    print("✓ Classes não são forçadas a implementar métodos que não usam")
    print("✓ Interfaces menores e mais específicas")
    print("✓ Maior flexibilidade e facilidade de manutenção")
    print("✓ Reduz acoplamento entre classes")
    print("✓ Código mais limpo e compreensível")
