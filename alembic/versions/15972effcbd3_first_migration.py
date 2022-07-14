"""First migration

Revision ID: 15972effcbd3
Revises: 
Create Date: 2022-07-13 16:24:21.774872

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '15972effcbd3'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('book',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_book_id'), 'book', ['id'], unique=False)
    op.create_table('bookmark',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('page', sa.Integer(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_bookmark_id'), 'bookmark', ['id'], unique=False)
    op.create_table('booknote',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('page', sa.Integer(), nullable=False),
    sa.Column('line', sa.Integer(), nullable=False),
    sa.Column('note', sa.String(), nullable=False),
    sa.Column('book_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['book_id'], ['book.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_booknote_id'), 'booknote', ['id'], unique=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_booknote_id'), table_name='booknote')
    op.drop_table('booknote')
    op.drop_index(op.f('ix_bookmark_id'), table_name='bookmark')
    op.drop_table('bookmark')
    op.drop_index(op.f('ix_book_id'), table_name='book')
    op.drop_table('book')
    # ### end Alembic commands ###