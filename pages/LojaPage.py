from appium.webdriver.common.appiumby import AppiumBy

from pages.PageObject import PageObject


class LojaPage:

    btn_pular_splashScreen = "br.com.brmalls.customer.amazonasshopping:id/btSkip"
    titulo_home = "//android.widget.TextView[@text=\"Olá, visitante.\"]"
    btn_alerta = "//android.widget.TextView[@text=\"Aceitar e continuar\"]"
    btn_verMais = "//android.widget.TextView[@text=\"ver mais\"]"
    btn_lupa = "//androidx.compose.ui.platform.ComposeView/android.view.View/android.view.View/android.view.View[1]/android.view.View[3]/android.view.View/android.view.View[2]"
    input_search_loja = "android.widget.EditText"
    btn_saibaMais = "//android.widget.TextView[@text=\"saiba mais\"]"
    titulo_detalhe_loja =  "//android.widget.TextView[@text=\"Detalhes da loja\"]"
    subTitulo_localizacao = "//android.widget.TextView[@text=\"Localização\"]"
    subTitulo_contato = "//android.widget.TextView[@text=\"Contato\"]"

    msg_pesq_loja_falha = "//android.widget.TextView[@text=\"Ops! Nenhuma loja encontrada.\"]"

    def __init__(self):
        self.page = PageObject()
        self.driver = self.page.driver
        super(LojaPage, self).__init__()

    def verificar_Home(self):
        self.page.myFindElement(AppiumBy.ID, self.btn_pular_splashScreen).click()
        self.tituloHome = self.page.myFindElement(AppiumBy.XPATH, self.titulo_home).text
        self.page.myFindElement(AppiumBy.XPATH, self.btn_alerta).click()
        self.page.myFindElement(AppiumBy.XPATH, self.btn_verMais).click()
        return self.tituloHome

    def pesquisar_loja(self, lojas):
        self.page.myFindElement(AppiumBy.XPATH, self.btn_lupa).click()
        self.page.myFindElement(AppiumBy.CLASS_NAME, self.input_search_loja).send_keys(lojas)

    def selecionar_loja(self, loja):
        lojaPesquisada = loja
        selecao_loja = f"//android.widget.TextView[@text='{lojaPesquisada}']"

        self.pesquisar_loja(loja)
        self.page.myFindElement(AppiumBy.XPATH, selecao_loja).click()




    def detalhar_loja(self):
        self.page.myFindElement(AppiumBy.XPATH, self.btn_saibaMais).click()

    def validar_titulo_detalhe_loja(self):
        self.titulo_detalhe = self.page.myFindElement(AppiumBy.XPATH, self.titulo_detalhe_loja).text
        return self.titulo_detalhe

    def validar_subTitulo_localizacao(self):
        self.subTitulo_local = self.page.myFindElement(AppiumBy.XPATH, self.subTitulo_localizacao).text
        return self.subTitulo_local

    def validar_subTitulo_contato(self):
        self.subTitulo_contatos = self.page.myFindElement(AppiumBy.XPATH, self.subTitulo_contato).text
        return self.subTitulo_contatos

    def validar_msg_pesquisar_loja_falha(self):
        self.msg_falha = self.page.myFindElement(AppiumBy.XPATH, self.msg_pesq_loja_falha).text
        return self.msg_falha










