import unittest

from pages.LojaPage import LojaPage

class LojaTest(unittest.TestCase):
    def setUp(self) -> None:
        self.texto_titulo = 'Olá, visitante.'
        self.tituloDetalhePage = 'Detalhes da loja'
        self.subTituloLocalizacaoPage = 'Localização'
        self.subTituloContatosPage = 'Contato'
        self.msg_loja_encontrada_falha = 'Ops! Nenhuma loja encontrada.'
        self.lp = LojaPage()

    def test_pesquisar_loja_sucesso(self):
        self.Title = self.lp.verificar_Home()
        assert self.Title == self.texto_titulo
        self.lp.selecionar_loja("Amazonas Play")
        self.lp.detalhar_loja()
        self.tituloDetalhe = self.lp.validar_titulo_detalhe_loja()
        assert self.tituloDetalhe == self.tituloDetalhePage
        self.subTituloLocalizacao = self.lp.validar_subTitulo_localizacao()
        assert self.subTituloLocalizacao == self.subTituloLocalizacaoPage
        self.subTituloCont = self.lp.validar_subTitulo_contato()
        assert self.subTituloCont == self.subTituloContatosPage
        self.lp.page.close()

    def test_pesquisar_loja_inexistente(self):
        self.Title = self.lp.verificar_Home()
        assert self.Title == self.texto_titulo
        self.lp.pesquisar_loja("Loja Teste")
        self.msg_falha_pesquisar_loja = self.lp.validar_msg_pesquisar_loja_falha()
        assert self.msg_falha_pesquisar_loja == self.msg_loja_encontrada_falha
        self.lp.page.close()


