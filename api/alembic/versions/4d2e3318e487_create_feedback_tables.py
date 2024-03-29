"""create feedback tables

Revision ID: 4d2e3318e487
Revises: 
Create Date: 2019-11-25 04:37:47.364359

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4d2e3318e487'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('rating_code',
    sa.Column('rating_code', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('rating_code')
    )
    op.create_table('rating',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('rating_code', sa.String(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
    sa.ForeignKeyConstraint(['rating_code'], ['rating_code.rating_code'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('feedback',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('comment', sa.Integer(), nullable=False),
    sa.Column('create_time', sa.DateTime(), nullable=False, server_default=sa.text('now()')),
    sa.Column('rating_id', sa.BigInteger(), nullable=True),
    sa.ForeignKeyConstraint(['rating_id'], ['rating.id'], ),
    sa.PrimaryKeyConstraint('id')
    )

    # populate initial values
    op.execute("""
    INSERT INTO
        rating_code (rating_code, description)
    VALUES
        ('negative', 'Negative'),
        ('neutral', 'Neutral'),
        ('positive', 'Positive')
    """)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('feedback')
    op.drop_table('rating')
    op.drop_table('rating_code')
    # ### end Alembic commands ###
