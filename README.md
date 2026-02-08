<!DOCTYPE html>
<html lang="pt-BR">
<head>
	<meta charset="UTF-8">
	<title>📘 Projeto Sabor Express</title>
</head>
<body>

	<h1>🍽️ Projeto Sabor Express</h1>

	<p>
		Este repositório foi criado com o objetivo de
		<strong>praticar Programação Orientada a Objetos (POO) em Python</strong>,
		utilizando um exemplo simples e realista de um sistema de cadastro de restaurantes.
	</p>

	<p>
		O projeto trabalha conceitos fundamentais como <strong>classes</strong>,
		<strong>atributos</strong>, <strong>métodos especiais</strong> e
		<strong>instanciação de objetos</strong>.
	</p>

	<hr>

	<h2>🚀 Conceitos Abordados</h2>

	<h3>🔹 Estrutura de Classes</h3>
	<ul>
		<li>Criação de classes em Python</li>
		<li>Uso do método construtor <strong>__init__</strong></li>
		<li>Definição de atributos de instância</li>
	</ul>

	<h3>🔹 Programação Orientada a Objetos</h3>
	<ul>
		<li>Instanciação de objetos</li>
		<li>Encapsulamento de dados</li>
		<li>Estados do objeto (ativo / inativo)</li>
	</ul>

	<h3>🔹 Métodos Especiais</h3>
	<ul>
		<li><strong>__init__</strong> – Inicializa os atributos da classe</li>
		<li><strong>__str__</strong> (opcional) – Permite exibir informações do objeto de forma amigável</li>
	</ul>

	<hr>

	<h2>📂 Estrutura Básica do Projeto</h2>

	<pre>
sabor-express/
│
├── restaurante.py
├── main.py
└── README.html
	</pre>

	<p>
		O arquivo principal contém a definição da classe <strong>Restaurante</strong>,
		onde são definidos os atributos e o comportamento do objeto.
	</p>

	<hr>

	<h2>🧪 Exemplo de Código</h2>

	<pre>
class Restaurante:
	def __init__(self, nome, categoria):
		self.nome = nome
		self.categoria = categoria
		self.ativo = False

restaurante_praca = Restaurante("Praça", "Gourmet")
restaurante_pizza = Restaurante("Pizza Express", "Italiano")
	</pre>

	<hr>

	<h2>💡 Aprendizados Importantes</h2>

	<ul>
		<li>O método construtor deve se chamar <strong>__init__</strong>, não <strong>__int__</strong></li>
		<li>Cada objeto criado possui seus próprios valores de atributos</li>
		<li>O <strong>print(objeto)</strong> pode ser personalizado com <strong>__str__</strong></li>
	</ul>

	<hr>

	<h2>📚 Objetivo do Repositório</h2>

	<ul>
		<li>Fixar conceitos básicos de POO em Python</li>
		<li>Servir como material de estudo e consulta</li>
		<li>Preparar base para projetos maiores</li>
	</ul>

	<p>
		Este projeto faz parte do processo de aprendizado em Python
		e pode ser evoluído futuramente com listas, menus interativos,
		persistência de dados e muito mais.
	</p>

</body>
</html>
