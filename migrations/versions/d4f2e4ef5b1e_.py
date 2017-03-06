"""empty message

Revision ID: d4f2e4ef5b1e
Revises: 4c6632617022
Create Date: 2017-02-15 22:30:54.050254

"""

# revision identifiers, used by Alembic.
revision = 'd4f2e4ef5b1e'
down_revision = '4c6632617022'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('production_needs', 'product',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('production_needs', 'product_in',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.alter_column('production_needs', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=False)
    op.create_primary_key(None, 'production_needs', ['id_'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('production_needs', 'quantity',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('production_needs', 'product_in',
               existing_type=sa.INTEGER(),
               nullable=True)
    op.alter_column('production_needs', 'product',
               existing_type=sa.INTEGER(),
               nullable=True)
    # ### end Alembic commands ###