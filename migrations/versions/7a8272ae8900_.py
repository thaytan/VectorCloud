"""empty message

Revision ID: 7a8272ae8900
Revises: 7228c2d45567
Create Date: 2018-12-29 21:59:47.031214

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '7a8272ae8900'
down_revision = '7228c2d45567'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('settings_cache')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('settings_cache',
    sa.Column('id', sa.INTEGER(), nullable=False),
    sa.Column('variable', sa.TEXT(), nullable=True),
    sa.Column('value', sa.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###