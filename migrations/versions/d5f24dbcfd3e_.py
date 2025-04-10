"""empty message

Revision ID: d5f24dbcfd3e
Revises: c72b6f2c8302
Create Date: 2019-03-13 15:53:57.330229

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'd5f24dbcfd3e'
down_revision = 'c72b6f2c8302'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shoes', sa.Column('brand_id', sa.Integer(), nullable=True))
    op.drop_constraint('shoes_ibfk_1', 'shoes', type_='foreignkey')
    op.create_foreign_key(None, 'shoes', 'brands', ['brand_id'], ['id'])
    op.drop_column('shoes', 'brand')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('shoes', sa.Column('brand', mysql.INTEGER(display_width=11), autoincrement=False, nullable=True))
    op.drop_constraint(None, 'shoes', type_='foreignkey')
    op.create_foreign_key('shoes_ibfk_1', 'shoes', 'brands', ['brand'], ['id'])
    op.drop_column('shoes', 'brand_id')
    # ### end Alembic commands ###
