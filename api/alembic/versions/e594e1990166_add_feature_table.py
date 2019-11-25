"""add feature table

Revision ID: e594e1990166
Revises: 4d2e3318e487
Create Date: 2019-11-25 05:20:51.461635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e594e1990166'
down_revision = '4d2e3318e487'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('feature',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('name', sa.String(), nullable=False, index=True, unique=True),
    sa.Column('create_time', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
    sa.PrimaryKeyConstraint('id')
    )
    op.add_column('feedback', sa.Column('feature_id', sa.BigInteger(), nullable=False))
    op.add_column('feedback', sa.Column('url', sa.String(), nullable=False))
    op.create_foreign_key(None, 'feedback', 'feature', ['feature_id'], ['id'])
    op.add_column('rating', sa.Column('feature_id', sa.BigInteger(), nullable=False))
    op.add_column('rating', sa.Column('url', sa.String(), nullable=False))
    op.create_foreign_key(None, 'rating', 'feature', ['feature_id'], ['id'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'rating', type_='foreignkey')
    op.drop_column('rating', 'url')
    op.drop_column('rating', 'feature_id')
    op.drop_constraint(None, 'feedback', type_='foreignkey')
    op.drop_column('feedback', 'url')
    op.drop_column('feedback', 'feature_id')
    op.drop_table('feature')
    # ### end Alembic commands ###
