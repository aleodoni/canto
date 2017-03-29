from django.apps import AppConfig


class CadastroConfig(AppConfig):
    name = 'canto.cadastro'
    verbose_name = "Cadastro"

    def ready(self):
        """Override this to put in:
            Users system checks
            Users signal registration
        """
        pass
