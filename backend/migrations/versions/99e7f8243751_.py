"""empty message

Revision ID: 99e7f8243751
Revises: 66fb79f8abd3
Create Date: 2024-02-05 23:47:14.924789

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '99e7f8243751'
down_revision = '66fb79f8abd3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.add_column(sa.Column('house_rules', sa.String(length=256), nullable=True))

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('games', schema=None) as batch_op:
        batch_op.drop_column('house_rules')

    # ### end Alembic commands ###
