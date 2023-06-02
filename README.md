[__TOC__]

# Lanchonete da Rua

# Para rodar o projeto
```
pip install flask-bcrypt

pip install flask-restplus

pip install Flask-Migrate

pip install pyjwt

pip install Flask-Script

pip install flask_testing

```

# O Problema
Há uma lanchonete de bairro que está expandindo devido seu grande sucesso. Porém, com a expansão e sem um sistema de controle de pedidos, o atendimento aos clientes pode ser caótico e confuso. Por exemplo, imagine que um cliente faça um pedido complexo, como um hambúrgues personalizado com ingredientes especificos,  acompanhado de batatas fritas e uma bebida. O atendente pode anotar o pedido em um papel e entregá-lo à cosiznha, mas não há garantia de que o pedido será preparado corretamente. Sem um sistema de controle de pedidos, pode haver confusão entre os atendentes e a cozinha, resultando em atrasos na preparação e entrega dos pedidos. Os pedidos podem ser perdidos, mal interpretados ou esquecidos, levando à insatisfação dos clientes e a perda de negócios. Em esumo, um sistema de controle de pedidos é essencial para garantir que a lanchonete possa atender os clientes de maneira eficiente, gerenciando seus  pedidos e estoques de forma adequada. Sem ele, expandir a lanchonete pode acabar não dando certo, resultando em clientes insatisfeitos e impactando os negocios de forma negativa. Para solucionar o problem, a lanchonete irá investir em um sistema de autoatendimento de fast food, que é composto por uma série de dispositivos e interfaces que permitem aos clienetes selecionar e fazer pedidos sem precisar interagir com um aendente, com as seguintes funcionalidades:

## Pedido
* Os clints são apresentados a uma interface de seleção na qual podem optar por se identificarem via CPF, se cadastrarem com nome, email ou não se identificar, podendo montar o combo na seguinte sequencia, sendo todas elas opcionais:
  * Lanche
  * Acompanhamento
  * Bebida
* Em cada etapa é exibido o nome, descrição e preço de cada produto

## Pagamento
O sistema deverá possuir uma opção de pagamento integrada para MVP. A forma de pagamento oferecida será via QRCode do Mercado Pago

## Acompanhamento
Uma vez que o pedido é confirmado e pago, ele é enviado para a cozinha para ser preparado.
Simultaneamente deve aparecer em um monitor para o cliente acompanhar o progresso do seu pedido com as seguintes etapas:

* Recibo
* Em preparação
* Pronto
* Finalizado

## Entrega
Quando o pedido estiver pronto, o sistema deverá notificar o cliente que ele está pronto para retirada. Ao ser retirado, o pedido deve ser atualizado para o status finalizado. Além das etapas do cliente, o estabelecimento precisa de uma acesso administrativo:

* Gerenciar Clientes: com a identificação dos clientes o estabelecimento pode trabalhar em campanhas promocionais
* Gerenciar produtos e categorias: Os produtos dispostos para escolha do cliente serão gerenciados pelo estabelecimento, definindo nome, categoria, preço, descrição e imagens.
Para esse sistema teremos categorias fixas:
  * Lanche
  * Acompanhamento
  * Bebida
  * Sobremesa
* Acompanhamento de pedidos: Deve ser possível acompanhar os pedidos em andamento e tempo de espera de cada pedido.

As informações dispostas no sistema de pedidos precisarão ser gerenciadas pelo estabelecimento através de um painel administrativo

# Entregas da Primeira etapa

+ Documentação do sistema (DDD) utilizando a linguagem ubíqua dos fluxos
++ Realização do pedido e pagamento
++ Preparação e entrega do pedido

+ Uma aplicação para todo sistema de backend (monolito) que deverá ser desenvolvido seguindo os padrões apresentados nas aulas:
a) Arquitetura hexagonal
b) APIs
+ Cadastro de cliente
+ Identificação do Cliente via CPF
+ Criar, editar e remover produto
+ Buscar produtos por categoria
+ Fake checkout, apenas enviar os produtos para a fila 
+ Listar pedidos

c) Aplicação deverá ser escalável para atender grandes volumes nos horários de pico
d) Banco de dados a escolha da equipe
  * Trabalhar para organizar a fila de pedidos via banco de dados

+ A aplicação deve ser entregue com um Dockerfile configurado para executá-la corretamente.

# Referencias

Build and Deploy Your Flask API With a Postgres Database

https://betterprogramming.pub/cookiecutter-template-to-build-and-deploy-your-flask-api-with-postgres-database-20ad99b8dae4

How to structure a Flask-RESTPlus web service for production builds
https://www.freecodecamp.org/news/structuring-a-flask-restplus-web-service-for-production-builds-c2ec676de563/