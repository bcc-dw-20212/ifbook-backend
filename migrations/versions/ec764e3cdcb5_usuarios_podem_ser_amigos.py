"""usuarios podem ser amigos

Revision ID: ec764e3cdcb5
Revises: 3b7616b3f355
Create Date: 2022-03-16 16:30:13.655761

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ec764e3cdcb5'
down_revision = '3b7616b3f355'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('amizade',
    sa.Column('user_a_id', sa.Integer(), nullable=False),
    sa.Column('user_b_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['user_a_id'], ['user.id'], name=op.f('fk_amizade_user_a_id_user')),
    sa.ForeignKeyConstraint(['user_b_id'], ['user.id'], name=op.f('fk_amizade_user_b_id_user')),
    sa.PrimaryKeyConstraint('user_a_id', 'user_b_id', name=op.f('pk_amizade'))
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('amizade')
    # ### end Alembic commands ###
