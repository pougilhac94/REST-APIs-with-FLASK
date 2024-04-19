"""empty message

Revision ID: 1f6708c4ea83
Revises: 7f2dcdbef5c9
Create Date: 2024-04-11 11:38:07.930428

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1f6708c4ea83'
down_revision = '7f2dcdbef5c9'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    #op.drop_table('_alembic_tmp_user_model')
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.add_column(sa.Column('email', sa.String(), nullable=False))
        batch_op.create_unique_constraint('email_constraint', ['email'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_model', schema=None) as batch_op:
        batch_op.drop_constraint('email_constraint', type_='unique')
        batch_op.drop_column('email')

    op.create_table('_alembic_tmp_user_model',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('username', sa.VARCHAR(length=80), nullable=False),
    sa.Column('password', sa.VARCHAR(length=256), nullable=False),
    sa.Column('email', sa.VARCHAR(length=256), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email', name='name email'),
    sa.UniqueConstraint('username')
    )
    # ### end Alembic commands ###