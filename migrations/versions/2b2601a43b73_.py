"""empty message

Revision ID: 2b2601a43b73
Revises: 245bd85e54e3
Create Date: 2023-06-05 17:46:46.744218

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2b2601a43b73'
down_revision = '245bd85e54e3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('operacao',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('nome', sa.String(length=50), nullable=False),
    sa.Column('resumo', sa.String(length=100), nullable=False),
    sa.Column('custo', sa.Float(), nullable=False),
    sa.Column('tipo', sa.Enum('entrada', 'saida', name='tipoenum'), nullable=False),
    sa.Column('conta_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['conta_id'], ['conta.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('operacao')
    # ### end Alembic commands ###
