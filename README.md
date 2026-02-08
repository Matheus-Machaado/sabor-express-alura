<!DOCTYPE html>
<html lang="pt-BR">
<head>
	<meta charset="UTF-8">
</head>
<body>
	<h1>🍽️ Projeto Sabor Express</h1>
	<p>
		Este repositório foi criado com o objetivo de
		<strong>estudar e praticar Programação Orientada a Objetos (POO) em Python</strong>,
		utilizando um exemplo simples de um sistema de cadastro e controle de restaurantes.
	</p>
	<p>
		O projeto trabalha conceitos como <strong>classes</strong>, <strong>atributos</strong>,
		<strong>métodos especiais</strong> e <strong>instanciação de objetos</strong>.
	</p>
	<hr>
	<h2>🚀 Conteúdos Estudados</h2>
	<h3>🔹 Estrutura de Classe</h3>
	<ul>
		<li><strong>class Restaurante</strong> – Criação de uma classe em Python</li>
		<li><strong>self</strong> – Referência ao próprio objeto</li>
		<li><strong>atributos</strong> – Armazenamento de dados do restaurante (nome, categoria, ativo)</li>
	</ul>
	<h3>🔹 Construtor e Inicialização</h3>
	<ul>
		<li><strong>__init__</strong> – Inicializa os atributos quando o objeto é criado</li>
	</ul>
	<h3>🔹 Instanciação de Objetos</h3>
	<ul>
		<li><strong>Restaurante("Praça", "Gourmet")</strong> – Cria um objeto com nome e categoria</li>
		<li><strong>self.ativo = False</strong> – Define estado inicial do restaurante</li>
	</ul>
	<h3>🔹 Saída no Terminal (print)</h3>
	<ul>
		<li><strong>print(objeto)</strong> – Sem <strong>__str__</strong>, mostra o endereço do objeto na memória</li>
		<li><strong>__str__</strong> – Permite exibir o restaurante com informações legíveis</li>
	</ul>
	<hr>
	<h2>💡 Dicas Importantes</h2>
	<h3>🔹 Melhorando o print com __str__</h3>
	<p>
		Para evitar que o <strong>print(restaurante)</strong> mostre algo como
		<em>&lt;__main__.Restaurante object at 0x...&gt;</em>, implemente <strong>__str__</strong>.
	</p>
	<pre>
class Restaurante:
	def __init__(self, nome, categoria):
		self.nome = nome
		self.categoria = categoria
		self.ativo = False
	def __str__(self):
		status = "Ativo" if self.ativo else "Inativo"
		return f"{self.nome} | {self.categoria} | {status}"
	</pre>
	<hr>
	<h2>▶️ Como executar o projeto</h2>
	<p>Execute o arquivo principal com Python:</p>
	<pre>
python main.py
	</pre>
	<p>
		Se seu arquivo tiver outro nome (ex: <strong>app.py</strong>), troque no comando:
	</p>
	<pre>
python app.py
	</pre>
	<hr>
	<h2>📚 Objetivo do Repositório</h2>
	<ul>
		<li>Fixar os conceitos básicos e intermediários de POO em Python</li>
		<li>Praticar criação de classes e objetos com um exemplo realista</li>
		<li>Servir como material de consulta rápida durante os estudos</li>
	</ul>
	<hr>

</body>
</html>
