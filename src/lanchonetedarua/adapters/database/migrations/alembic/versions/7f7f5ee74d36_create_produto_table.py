"""create produto table

Revision ID: 7f7f5ee74d36
Revises: 2f79f3b3695a
Create Date: 2023-06-27 17:06:48.117623

"""
from alembic import op
import sqlalchemy as sa
import datetime

# revision identifiers, used by Alembic.
revision = '7f7f5ee74d36'
down_revision = '2f79f3b3695a'
branch_labels = None
depends_on = None


def upgrade() -> None:
    produto_table = op.create_table(
        'produto',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('nome', sa.String(50), nullable=False),
        sa.Column('descricao', sa.String(1024), nullable=False),
        sa.Column('categoria_id', sa.Integer, sa.ForeignKey("categoria.id"), nullable=False),
        sa.Column('valor', sa.Float),
        sa.Column('created_at', sa.DateTime(), default=datetime.datetime.now())
    )

    op.bulk_insert(
        produto_table,
        [
            { "id": 1, "nome": "Hamburger Brutal", "descricao": "O Queridinho Da Galera! Nosso burger mais pedido vai com 180g do nosso delicioso blend angus, pão australiano, maionese especial, bacon defumado, e queijo cheddar... (O duplo vai com o dobro de carne e queijo)", "categoria_id": 1, "valor": 35.6 },
            { "id": 2, "nome": "Hamburger Brutal", "descricao": "Seu novo burger favorito! Nosso novo burger vai com nosso blend 180g angus, pão pretzel bem macio, queijo minas que além de um sabor delicioso, traz uma textura única para seu burger. E pra finalizar: um catchup de goiabada feito na casa! Um clássico da culinária agora no seu burger!", "categoria_id": 1, "valor": 45.6 },
            { "id": 3, "nome": "Hamburger Medieval", "descricao": "Com Catupiry De Verdade! Nosso mais novo burger vai com nosso blend 180g angus, pão pretzel, bacon defumado, , queijo cheddar e o legítimo Catupiry que dá uma cremosidade inigualável! (O duplo vai com o dobro de carne e queijo)", "categoria_id": 1, "valor": 30.6 },
            { "id": 4, "nome": "Combo Brutal", "descricao": "1 burger de 180 gramas, pão australiano, maionese especial, queijo cheddar e bacon defumado + porção de batata frita + refrigerante em lata", "categoria_id": 5, "valor": 55.6 },
            { "id": 5, "nome": "Combo Bárbaro", "descricao": "1 burger de 180 gramas, pão pretzel, catchup de goiaba feito na casa e queijo minas + porção de batata frita + refrigerante em lata", "categoria_id": 5, "valor": 54.6 },
            { "id": 6, "nome": "Combo Rústico", "descricao": "1 burger de 180 gramas, pão pretzel, queijo prato, molho de tomate caseiro + porção de batata frita + refrigerante em lata", "categoria_id": 5, "valor": 60.6 },
            { "id": 7, "nome": "Batatas palito", "descricao": "batata palito", "categoria_id": 2, "valor": 10.8  },
            { "id": 8, "nome": "Batatas chips", "descricao": "batata chips", "categoria_id": 2, "valor": 10.9  },
            { "id": 9, "nome": "Coca-cola 250ml", "descricao": "coca cola", "categoria_id": 3, "valor": 7  },
            { "id": 10, "nome": "Guarana antartica 250ml", "descricao": "guarana", "categoria_id": 3, "valor": 7  },
            { "id": 11, "nome": "Brigadeiro", "descricao": "brigadeiro", "categoria_id": 4, "valor": 5.6  },
            { "id": 18, "nome": "Pudim leite", "descricao": "pudin leite", "categoria_id": 4, "valor": 8.6  },
        ],
    )



def downgrade() -> None:
    op.drop_table('produto')
