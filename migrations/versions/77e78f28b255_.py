"""empty message

Revision ID: 77e78f28b255
Revises: 03bec8f1f378
Create Date: 2022-11-09 14:40:11.972241

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77e78f28b255'
down_revision = '03bec8f1f378'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('goal', sa.Column('lazy', sa.String(), nullable=True))
    op.add_column('task', sa.Column('goal_id', sa.Integer(), nullable=True))
    op.create_foreign_key(None, 'task', 'goal', ['goal_id'], ['goal_id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'task', type_='foreignkey')
    op.drop_column('task', 'goal_id')
    op.drop_column('goal', 'lazy')
    # ### end Alembic commands ###
