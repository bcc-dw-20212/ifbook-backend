"""usuarios fazem varios cursos

Revision ID: 74d782406e61
Revises: ec764e3cdcb5
Create Date: 2022-03-16 16:42:11.982249

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '74d782406e61'
down_revision = 'ec764e3cdcb5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cursos_alunos',
    sa.Column('aluno', sa.Integer(), nullable=False),
    sa.Column('curso', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['aluno'], ['user.id'], name=op.f('fk_cursos_alunos_aluno_user')),
    sa.ForeignKeyConstraint(['curso'], ['curso.id'], name=op.f('fk_cursos_alunos_curso_curso')),
    sa.PrimaryKeyConstraint('aluno', 'curso', name=op.f('pk_cursos_alunos'))
    )
    op.drop_table('amizade')
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_constraint('fk_user_curso_id_curso', type_='foreignkey')
        batch_op.drop_column('curso_id')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('curso_id', sa.INTEGER(), nullable=False))
        batch_op.create_foreign_key('fk_user_curso_id_curso', 'curso', ['curso_id'], ['id'])

    op.create_table('amizade',
    sa.Column('user_a_id', sa.INTEGER(), nullable=False),
    sa.Column('user_b_id', sa.INTEGER(), nullable=False),
    sa.ForeignKeyConstraint(['user_a_id'], ['user.id'], name='fk_amizade_user_a_id_user'),
    sa.ForeignKeyConstraint(['user_b_id'], ['user.id'], name='fk_amizade_user_b_id_user'),
    sa.PrimaryKeyConstraint('user_a_id', 'user_b_id', name='pk_amizade')
    )
    op.drop_table('cursos_alunos')
    # ### end Alembic commands ###