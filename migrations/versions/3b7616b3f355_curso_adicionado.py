"""curso adicionado

Revision ID: 3b7616b3f355
Revises: 5599243ba593
Create Date: 2022-03-16 15:48:49.897729

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3b7616b3f355'
down_revision = '5599243ba593'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('curso',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(length=30), nullable=False),
    sa.Column('sigla', sa.String(length=4), nullable=True),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_curso')),
    sa.UniqueConstraint('nome', name=op.f('uq_curso_nome')),
    sa.UniqueConstraint('sigla', name=op.f('uq_curso_sigla'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curso_id', sa.Integer(), nullable=False))
        batch_op.create_foreign_key(batch_op.f('fk_user_curso_id_curso'), 'curso', ['curso_id'], ['id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_curso_id_curso'), type_='foreignkey')
        batch_op.drop_column('curso_id')

    op.drop_table('curso')
    # ### end Alembic commands ###