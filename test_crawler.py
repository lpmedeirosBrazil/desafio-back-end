# coding:utf-8
import unittest
from crawler import parse_description, scrap_xml


class CrawlerTests(unittest.TestCase):
    def test_parse_description(self):
        description = """
                <div class="foto componente_materia midia-largura-620">
                 <img alt="BMW F 850 GS Adventure (Foto: divulgação)" height="413" id="281380" src="https://s2.glbimg.com/9v5p-9Cz95AS-Y1MTtVTPY2GV14=/620x413/e.glbimg.com/og/ed/f/original/2018/06/26/bmw-f850-e-f750-gs-2018.jpg" title="BMW F 850 GS Adventure (Foto: divulgação)" width="620" /><label class="foto-legenda">BMW F 850 GS Adventure (Foto: divulga&ccedil;&atilde;o)</label></div>
                 <p>
                 &nbsp;</p>
                 <p>
                 A <a href="https://revistaautoesporte.globo.com/carros/bmw/">BMW</a> come&ccedil;ou a produ&ccedil;&atilde;o da <a href="https://revistaautoesporte.globo.com/Noticias/noticia/2018/06/bmw-confirma-producao-nacional-das-novas-motos-f-750-gs-e-f-850-gs.html">F 850 GS Adventure</a> no Brasil e j&aacute; tem uma data para come&ccedil;ar a vender o modelo: primeira quinzena de mar&ccedil;o. <strong>A aventureira &eacute; a d&eacute;cima moto que passa a ser fabricado na f&aacute;brica de Manaus (AM)</strong>.<br />
                 <br />
                 A Adventure ainda n&atilde;o teve seus pre&ccedil;os divulgados, mas custar&aacute; um pouco mais do que a <strong>F 850 GS Premium</strong>, que tem painel de instrumentos convencional e custa <strong>R$ 50.950</strong>. Tamb&eacute;m ser&aacute; mais cara que a <strong>F 850 GS Premium</strong>, equipada com painel TFT, e vendida por <strong>R$ 52.950</strong>. A nova moto tamb&eacute;m traz diferen&ccedil;as no visual e no tamanho do tanque.</p>
                 <div class="saibamais componente_materia expandido">
                 <strong>saiba mais</strong>
                 <ul>
                 <li>
                 <a href="https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/bmw-ducati-e-harley-davidson-nao-estarao-no-salao-duas-rodas-2019.html">BMW, Ducati e Harley-Davidson n&atilde;o estar&atilde;o no Sal&atilde;o Duas Rodas 2019</a></li>
                 <li>
                 <a href="https://revistaautoesporte.globo.com/testes/noticia/2019/01/teste-yamaha-250-lander-2019-chega-com-freio-abs-e-novo-visual-para-encostar-na-honda-xre-300.html">Teste: Yamaha Lander chega com freio ABS e novo visual para encostar na Honda XRE 300</a></li>
                 <li>
                 <a href="https://revistaautoesporte.globo.com/testes/noticia/2019/01/teste-triumph-bonneville-t100-black-anglo-brasileira-com-sotaque-grave-que-acelera-forte-e-e-facil-de-pilotar.html">Teste: Triumph Bonneville T100 Black, uma moto que acelera forte e &eacute; f&aacute;cil de pilotar</a></li>
                 <li>
                 <a href="https://revistaautoesporte.globo.com/testes/noticia/2019/02/teste-royal-enfield-himalayan-vem-para-incomodar-honda-xre-300-e-yamaha-lander-250.html">Teste: Royal Enfield Himalayan vem para incomodar Honda XRE 300 e Yamaha Lander 250</a></li>
                 </ul>
                 </div>
                 <p>
                 &nbsp;</p>
                 <p>
                 A F 850 GS Adventure emoldura um <strong>motor bicil&iacute;ndrico de 853 cm&sup3; com inje&ccedil;&atilde;o eletr&ocirc;nica que produz 80 cv a 6.250 rpm e 9,2 kgfm a 6.250 rpm</strong>. O propulsor vai acoplado a um c&acirc;mbio de seis velocidades. E a embreagem do tipo deslizante ajuda na maciez e evita travamento da roda traseira quando se solta o manete com mais rapidez.<br />
                 <br />
                 Uma das novidades &eacute; o <strong>tanque de combust&iacute;vel que teve a</strong> <strong>capacidade aumentada de 15 para 23 litros</strong>, quando comparado ao que equipa as demais motos da gama.</p>
                 <p>
                 A fora de estrada exibe prote&ccedil;&otilde;es nas laterais do motor e na carenagem, e traz ainda <strong>cinco modos de pilotagem</strong>: rain, road, dynamic, enduro e enduro pro. Na parte eletr&ocirc;nica, h&aacute; freios ABS, controle de tra&ccedil;&atilde;o, suspens&atilde;o eletr&ocirc;nica e painel digital com <strong>tela TFT de 6,5 polegadas</strong>.</p>
                 <p>
                 Al&eacute;m da F 850 GS, <strong>outros nove modelos tamb&eacute;m s&atilde;o produzidos na f&aacute;brica:</strong> BMW F 750 GS, a BMW G 310 R, a BMW G 310 GS, a BMW R 1200 GS, a BMW R 1200 GS Adventure, a BMW S 1000 R, a BMW S 1000 RR e a BMW S 1000 XR.</p>
                 <div class="foto componente_materia midia-largura-620">
                 <img alt="Fábrica da BMW Motorrad em Manaus (AM) começa a produzir a F 850 GS Adventure (Foto: Divulgação)" height="413" id="317224" src="https://s2.glbimg.com/dhdgCSO67ibq2Uiyq-jbUtjB9Vc=/620x413/e.glbimg.com/og/ed/f/original/2019/02/27/p90337157_highres_f-850-gs-adventure-0.jpg" title="Fábrica da BMW Motorrad em Manaus (AM) começa a produzir a F 850 GS Adventure (Foto: Divulgação)" width="620" /><label class="foto-legenda">F&aacute;brica da BMW Motorrad em Manaus (AM) come&ccedil;a a produzir a F 850 GS Adventure (Foto: Divulga&ccedil;&atilde;o)</label></div>
                 <p>
                 &nbsp;</p>
        """
        expected = [{'type': 'links', 'content': ['https://revistaautoesporte.globo.com/carros/bmw/', 'https://revistaautoesporte.globo.com/Noticias/noticia/2018/06/bmw-confirma-producao-nacional-das-novas-motos-f-750-gs-e-f-850-gs.html', 'https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/bmw-ducati-e-harley-davidson-nao-estarao-no-salao-duas-rodas-2019.html', 'https://revistaautoesporte.globo.com/testes/noticia/2019/01/teste-yamaha-250-lander-2019-chega-com-freio-abs-e-novo-visual-para-encostar-na-honda-xre-300.html', 'https://revistaautoesporte.globo.com/testes/noticia/2019/01/teste-triumph-bonneville-t100-black-anglo-brasileira-com-sotaque-grave-que-acelera-forte-e-e-facil-de-pilotar.html', 'https://revistaautoesporte.globo.com/testes/noticia/2019/02/teste-royal-enfield-himalayan-vem-para-incomodar-honda-xre-300-e-yamaha-lander-250.html']}, [{'type': 'image', 'content': 'https://s2.glbimg.com/9v5p-9Cz95AS-Y1MTtVTPY2GV14=/620x413/e.glbimg.com/og/ed/f/original/2018/06/26/bmw-f850-e-f750-gs-2018.jpg'}, {'type': 'image', 'content': 'https://s2.glbimg.com/dhdgCSO67ibq2Uiyq-jbUtjB9Vc=/620x413/e.glbimg.com/og/ed/f/original/2019/02/27/p90337157_highres_f-850-gs-adventure-0.jpg'}], {'type': 'text', 'content': '                 \xa0'}, {'type': 'text', 'content': '                 A BMW começou a produção da F 850 GS Adventure no Brasil e já tem uma data para começar a vender o modelo: primeira quinzena de março. A aventureira é a décima moto que passa a ser fabricado na fábrica de Manaus (AM).                 A Adventure ainda não teve seus preços divulgados, mas custará um pouco mais do que a F 850 GS Premium, que tem painel de instrumentos convencional e custa R$ 50.950. Também será mais cara que a F 850 GS Premium, equipada com painel TFT, e vendida por R$ 52.950. A nova moto também traz diferenças no visual e no tamanho do tanque.'}, {'type': 'text', 'content': '                 \xa0'}, {'type': 'text', 'content': '                 A F 850 GS Adventure emoldura um motor bicilíndrico de 853 cm³ com injeção eletrônica que produz 80 cv a 6.250 rpm e 9,2 kgfm a 6.250 rpm. O propulsor vai acoplado a um câmbio de seis velocidades. E a embreagem do tipo deslizante ajuda na maciez e evita travamento da roda traseira quando se solta o manete com mais rapidez.                 Uma das novidades é o tanque de combustível que teve a capacidade aumentada de 15 para 23 litros, quando comparado ao que equipa as demais motos da gama.'}, {'type': 'text', 'content': '                 A fora de estrada exibe proteções nas laterais do motor e na carenagem, e traz ainda cinco modos de pilotagem: rain, road, dynamic, enduro e enduro pro. Na parte eletrônica, há freios ABS, controle de tração, suspensão eletrônica e painel digital com tela TFT de 6,5 polegadas.'}, {'type': 'text', 'content': '                 Além da F 850 GS, outros nove modelos também são produzidos na fábrica: BMW F 750 GS, a BMW G 310 R, a BMW G 310 GS, a BMW R 1200 GS, a BMW R 1200 GS Adventure, a BMW S 1000 R, a BMW S 1000 RR e a BMW S 1000 XR.'}, {'type': 'text', 'content': '                 \xa0'}]
        self.assertEqual(expected, parse_description(description))

    def test_scrap_xml(self):
        result_xml = """<?xml version="1.0" encoding="UTF-8" ?>
<rss version="2.0" xmlns:dc="http://purl.org/dc/elements/1.1/">
	<channel>
		<title>
			<![CDATA[Auto Esporte]]>
		</title>
		<link>https://revistaautoesporte.globo.com/</link>
		<description/>
		<language>pt-BR</language>
		<copyright>© Todos os direitos reservados.</copyright>
		<image>
			<url>https://e.glbimg.com/og/ed/edg2/static_files/rss/img/auto-esporte.png</url>
			<title>
				<![CDATA[Auto Esporte]]>
			</title>
			<link>https://revistaautoesporte.globo.com/</link>
		</image>
		<item>
			<title>
				<![CDATA[Confirmado: Caoa negocia compra da fábrica da Ford em SBC]]>
			</title>
			<description>
<![CDATA[<div class="foto componente_materia midia-largura-620"><img alt="Caoa - Ford (Foto: Caoa/Divulgação)" height="413" id="317229" src="https://s2.glbimg.com/jGcxaEBVUQN_FQPrNgqZre7e0AY=/620x413/e.glbimg.com/og/ed/f/original/2019/02/27/caoa_ford1.jpg" title="Caoa - Ford (Foto: Caoa/Divulgação)" width="620" /><label class="foto-legenda">Caoa &eacute; revendedora de ve&iacute;culos Ford desde a d&eacute;cada de 1970 (Foto: Caoa/Divulga&ccedil;&atilde;o)</label></div><p>
	&nbsp;</p><p>
	A f&aacute;brica da Ford em S&atilde;o Bernardo do Campo (SP) pode ter um fim diferente do completo fechamento.&nbsp;<strong>O grupo Caoa confirmou a AutoEsporte nesta quarta-feira, 27, que est&aacute; negociando a compra da f&aacute;brica, embora n&atilde;o haja nada fechado.&nbsp;</strong></p><p>
	&quot;A Caoa confirma que h&aacute; conversas com a Ford e com o Governo da Estado sobre a aquisi&ccedil;&atilde;o da planta em S&atilde;o Bernardo do Campo&quot;, disse a Caoa, em nota.&nbsp;A empresa ainda refor&ccedil;a a import&acirc;ncia da Ford no mercado nacional e lembra que h&aacute; uma &quot;forte parceria com a Ford h&aacute; mais de quatro d&eacute;cadas&quot;.</p><div class="saibamais componente_materia expandido"><strong>saiba mais</strong><ul><li><a href="https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/ford-fecha-fabrica-de-sao-bernardo-do-campo-sua-primeira-no-brasil-decisao-tira-o-new-fiesta-de-linha.html">Ford fechar&aacute; a f&aacute;brica de S&atilde;o Bernardo do Campo, sua primeira no Brasil; decis&atilde;o tira o New Fiesta de linha</a></li>
	</ul>
	]]>
			</description>
			<link>https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/oscar-2019-os-6-carros-que-aparecem-entre-os-filmes-indicados.html</link>
			<dc:creator>Da redação de Auto Esporte</dc:creator>
			<guid>3330059</guid>
		</item>
	</channel>
</rss>
"""
        expected = {'feed': [{'item': {'link': 'https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/oscar-2019-os-6-carros-que-aparecem-entre-os-filmes-indicados.html', 'title': '\n\t\t\t\tConfirmado: Caoa negocia compra da fábrica da Ford em SBC\n\t\t\t', 'description': [{'type': 'links', 'content': ['https://revistaautoesporte.globo.com/Noticias/noticia/2019/02/ford-fecha-fabrica-de-sao-bernardo-do-campo-sua-primeira-no-brasil-decisao-tira-o-new-fiesta-de-linha.html']}, [{'type': 'image', 'content': 'https://s2.glbimg.com/jGcxaEBVUQN_FQPrNgqZre7e0AY=/620x413/e.glbimg.com/og/ed/f/original/2019/02/27/caoa_ford1.jpg'}], {'type': 'text', 'content': 'A fábrica da Ford em São Bernardo do Campo (SP) pode ter um fim diferente do completo fechamento.\xa0O grupo Caoa confirmou a AutoEsporte nesta quarta-feira, 27, que está negociando a compra da fábrica, embora não haja nada fechado.\xa0'}, {'type': 'text', 'content': '"A Caoa confirma que há conversas com a Ford e com o Governo da Estado sobre a aquisição da planta em São Bernardo do Campo", disse a Caoa, em nota.\xa0A empresa ainda reforça a importância da Ford no mercado nacional e lembra que há uma "forte parceria com a Ford há mais de quatro décadas".'}]}}]}
        self.assertEqual(expected, scrap_xml(result_xml))

