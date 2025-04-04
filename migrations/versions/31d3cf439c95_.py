"""empty message

Revision ID: 31d3cf439c95
Revises: fdb4b47e07f3
Create Date: 2019-03-29 15:34:01.490149

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '31d3cf439c95'
down_revision = 'fdb4b47e07f3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clothes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=25), nullable=True),
    sa.Column('description', sa.Text(), nullable=True),
    sa.Column('price', sa.Integer(), nullable=True),
    sa.Column('size', sa.String(length=6), nullable=True),
    sa.Column('quantity', sa.Integer(), nullable=True),
    sa.Column('timestamp', sa.DateTime(), nullable=True),
    sa.Column('image_id', sa.String(length=30), nullable=True),
    sa.Column('image_url', sa.String(length=200), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_index(op.f('ix_clothes_timestamp'), 'clothes', ['timestamp'], unique=False)
    op.create_table('cart_clothes',
    sa.Column('cloth_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['cloth_id'], ['clothes.id'], ),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.PrimaryKeyConstraint('cloth_id', 'customer_id')
    )
    op.create_table('cart_shoes',
    sa.Column('shoe_id', sa.Integer(), nullable=False),
    sa.Column('customer_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], ),
    sa.ForeignKeyConstraint(['shoe_id'], ['shoes.id'], ),
    sa.PrimaryKeyConstraint('shoe_id', 'customer_id')
    )
    op.drop_table('cart_items')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('cart_items',
    sa.Column('shoe_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('customer_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['customer_id'], ['customers.id'], name='cart_items_ibfk_1'),
    sa.ForeignKeyConstraint(['shoe_id'], ['shoes.id'], name='cart_items_ibfk_2'),
    sa.PrimaryKeyConstraint('shoe_id', 'customer_id'),
    mysql_collate='utf8mb4_0900_ai_ci',
    mysql_default_charset='utf8mb4',
    mysql_engine='InnoDB'
    )
    op.drop_table('cart_shoes')
    op.drop_table('cart_clothes')
    op.drop_index(op.f('ix_clothes_timestamp'), table_name='clothes')
    op.drop_table('clothes')
    # ### end Alembic commands ###
