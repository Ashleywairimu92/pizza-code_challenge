"""Add restaurant_id to restaurant_pizzas

Revision ID: 84886827fdc3
Revises: cf44ca90e3a4
Create Date: 2024-10-13 20:29:43.694552

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '84886827fdc3'
down_revision = 'cf44ca90e3a4'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('pizzas', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('pizzas', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.add_column('restaurant_pizzas', sa.Column('restaurant_id', sa.Integer(), nullable=True))
    op.add_column('restaurant_pizzas', sa.Column('pizza_id', sa.Integer(), nullable=True))
    op.alter_column('restaurant_pizzas', 'price',
               existing_type=sa.INTEGER(),
               type_=sa.Float(),
               nullable=True)
    op.create_foreign_key(op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurant_pizzas', 'restaurants', ['restaurant_id'], ['id'])
    op.create_foreign_key(op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'restaurant_pizzas', 'pizzas', ['pizza_id'], ['id'])
    op.alter_column('restaurants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=False)
    op.alter_column('restaurants', 'address',
               existing_type=sa.VARCHAR(),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('restaurants', 'address',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('restaurants', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.drop_constraint(op.f('fk_restaurant_pizzas_pizza_id_pizzas'), 'restaurant_pizzas', type_='foreignkey')
    op.drop_constraint(op.f('fk_restaurant_pizzas_restaurant_id_restaurants'), 'restaurant_pizzas', type_='foreignkey')
    op.alter_column('restaurant_pizzas', 'price',
               existing_type=sa.Float(),
               type_=sa.INTEGER(),
               nullable=False)
    op.drop_column('restaurant_pizzas', 'pizza_id')
    op.drop_column('restaurant_pizzas', 'restaurant_id')
    op.alter_column('pizzas', 'ingredients',
               existing_type=sa.VARCHAR(),
               nullable=True)
    op.alter_column('pizzas', 'name',
               existing_type=sa.VARCHAR(),
               nullable=True)
    # ### end Alembic commands ###
