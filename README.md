<h1>Gerenciamento de Estoque de Produtos</h1>

<p>Este repositório contém um sistema simples para gerenciamento de estoque de produtos. O objetivo do projeto é fazer um sistema 
Praticando Programação Orientada a Objetos (POO) em Python. O projeto permite adicionar, remover, editar e visualizar produtos em um estoque.</p>


<h2>Estrutura do Projeto</h2>
<p>O projeto consiste em duas classes principais:</p>

<h3>Classe <code>Produtos</code></h3>
<p>Representa um produto com os seguintes atributos:</p>
<ul>
    <li><code>IDProduto</code>: Identificador único do produto.</li>
    <li><code>nome</code>: Nome do produto.</li>
    <li><code>preco</code>: Preço do produto.</li>
    <li><code>marca</code>: Marca do produto.</li>
</ul>

<h4>Método <code>__str__</code></h4>
<p>Retorna uma representação textual do produto no formato:</p>
<pre><code>(Id: &lt;IDProduto&gt; - &lt;nome&gt; - R$&lt;preco&gt; - &lt;marca&gt;)</code></pre>

<h3>Classe <code>EstoqueProduto</code></h3>
<p>Gerencia o estoque de produtos.</p>

<h4>Atributo</h4>
<ul>
    <li><code>estoque</code>: Dicionário que armazena os produtos, onde a chave é o <code>IDProduto</code> e o valor é uma instância da classe <code>Produtos</code>.</li>
</ul>

<h4>Métodos</h4>
<ul>
    <li><code>adicionar_produto(produto)</code>: Adiciona um produto ao estoque. Verifica se o <code>IDProduto</code> já existe.</li>
    <li><code>mostrar_estoque()</code>: Exibe todos os produtos no estoque.</li>
    <li><code>RemoverProduto(IDproduto)</code>: Remove um produto pelo seu <code>IDProduto</code>.</li>
    <li><code>EditarProduto(IDproduto, NovoNome=None, NovoPreco=None, NovaMarca=None)</code>: Edita os detalhes de um produto no estoque.</li>
    <li><code>LimparEstoque()</code>: Remove todos os produtos do estoque.</li>
</ul>

<h2>Uso</h2>
<p>O sistema inclui um menu interativo que permite ao usuário realizar as seguintes operações:</p>
<ol>
    <li>Adicionar Produto</li>
    <li>Remover Produto</li>
    <li>Editar Produto do Estoque</li>
    <li>Exibir Estoque</li>
    <li>Limpar Estoque</li>
    <li>Finalizar Sistema</li>
</ol>



