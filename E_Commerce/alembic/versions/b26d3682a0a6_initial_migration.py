"""initial migration

Revision ID: b26d3682a0a6
Revises: 
Create Date: 2024-08-28 01:00:02.934390

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'b26d3682a0a6'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('users',
    sa.Column('id', sa.UUID(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('firstname', sa.String(), nullable=False),
    sa.Column('lastname', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('password_hash', sa.String(), nullable=False),
    sa.Column('phone', sa.String(), nullable=True),
    sa.Column('confirmation_token_sent_at', sa.DateTime(), nullable=True),
    sa.Column('email_confirmed_at', sa.DateTime(), nullable=True),
    sa.Column('confirmed_status', sa.Boolean(), nullable=True),
    sa.Column('last_sign_in', sa.DateTime(), nullable=True),
    sa.Column('account_created_at', sa.DateTime(), nullable=True),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.Column('created_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.Column('updated_at', sa.DateTime(timezone=True), server_default=sa.text('now()'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_email'), 'users', ['email'], unique=True)
    op.create_index(op.f('ix_users_id'), 'users', ['id'], unique=True)
    op.create_index(op.f('ix_users_phone'), 'users', ['phone'], unique=True)
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('vendors',
    sa.Column('vendor_id', sa.Integer(), nullable=False),
    sa.Column('vendor_name', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('vendor_id'),
    sa.UniqueConstraint('vendor_name')
    )
    op.create_index(op.f('ix_vendors_vendor_id'), 'vendors', ['vendor_id'], unique=False)
    op.create_table('organizations',
    sa.Column('org_id', sa.Integer(), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('org_name', sa.String(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('acc_num', sa.String(), nullable=False),
    sa.Column('acc_name', sa.String(), nullable=False),
    sa.Column('acc_bank', sa.String(), nullable=False),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ),
    sa.PrimaryKeyConstraint('org_id')
    )
    op.create_index(op.f('ix_organizations_org_id'), 'organizations', ['org_id'], unique=False)
    op.create_table('profiles',
    sa.Column('profile_id', sa.Integer(), nullable=False),
    sa.Column('profile_name', sa.String(), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('gr_num', sa.String(), nullable=False),
    sa.Column('tin_num', sa.String(), nullable=False),
    sa.Column('address', sa.String(), nullable=False),
    sa.Column('currency', sa.String(), nullable=True),
    sa.Column('vat', sa.Float(), nullable=False),
    sa.Column('account_number', sa.String(), nullable=False),
    sa.Column('account_name', sa.String(), nullable=False),
    sa.Column('account_bank', sa.String(), nullable=False),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ),
    sa.PrimaryKeyConstraint('profile_id')
    )
    op.create_index(op.f('ix_profiles_profile_id'), 'profiles', ['profile_id'], unique=False)
    op.create_table('user_vendor_tokens',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('token', sa.String(), nullable=True),
    sa.Column('expires_at', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_vendor_tokens_id'), 'user_vendor_tokens', ['id'], unique=False)
    op.create_index(op.f('ix_user_vendor_tokens_token'), 'user_vendor_tokens', ['token'], unique=True)
    op.create_table('user_vendors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.UUID(), nullable=False),
    sa.Column('vendor_id', sa.Integer(), nullable=False),
    sa.Column('is_admin', sa.Boolean(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], ondelete='CASCADE'),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ondelete='CASCADE'),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_vendors_id'), 'user_vendors', ['id'], unique=False)
    op.create_table('invoices',
    sa.Column('invoice_id', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('po_num', sa.String(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('due_date', sa.DateTime(timezone=True), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.profile_id'], ),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ),
    sa.PrimaryKeyConstraint('invoice_id')
    )
    op.create_index(op.f('ix_invoices_invoice_id'), 'invoices', ['invoice_id'], unique=False)
    op.create_table('quotes',
    sa.Column('quote_id', sa.Integer(), nullable=False),
    sa.Column('quote_name', sa.String(), nullable=False),
    sa.Column('description', sa.String(length=100), nullable=True),
    sa.Column('profile_id', sa.Integer(), nullable=True),
    sa.Column('vendor_id', sa.Integer(), nullable=True),
    sa.Column('username', sa.String(), nullable=True),
    sa.Column('date_created', sa.DateTime(), nullable=True),
    sa.Column('date_modified', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['profile_id'], ['profiles.profile_id'], ),
    sa.ForeignKeyConstraint(['username'], ['users.username'], ),
    sa.ForeignKeyConstraint(['vendor_id'], ['vendors.vendor_id'], ),
    sa.PrimaryKeyConstraint('quote_id')
    )
    op.create_index(op.f('ix_quotes_quote_id'), 'quotes', ['quote_id'], unique=False)
    op.create_table('items_invoice',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('item_price', sa.Float(), nullable=False),
    sa.Column('item_amount', sa.Integer(), nullable=False),
    sa.Column('invoice_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['invoice_id'], ['invoices.invoice_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_index(op.f('ix_items_invoice_item_id'), 'items_invoice', ['item_id'], unique=False)
    op.create_table('items_quotes',
    sa.Column('item_id', sa.Integer(), nullable=False),
    sa.Column('item_name', sa.String(), nullable=False),
    sa.Column('item_price', sa.Float(), nullable=False),
    sa.Column('item_amount', sa.Integer(), nullable=False),
    sa.Column('quote_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['quote_id'], ['quotes.quote_id'], ),
    sa.PrimaryKeyConstraint('item_id')
    )
    op.create_index(op.f('ix_items_quotes_item_id'), 'items_quotes', ['item_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_items_quotes_item_id'), table_name='items_quotes')
    op.drop_table('items_quotes')
    op.drop_index(op.f('ix_items_invoice_item_id'), table_name='items_invoice')
    op.drop_table('items_invoice')
    op.drop_index(op.f('ix_quotes_quote_id'), table_name='quotes')
    op.drop_table('quotes')
    op.drop_index(op.f('ix_invoices_invoice_id'), table_name='invoices')
    op.drop_table('invoices')
    op.drop_index(op.f('ix_user_vendors_id'), table_name='user_vendors')
    op.drop_table('user_vendors')
    op.drop_index(op.f('ix_user_vendor_tokens_token'), table_name='user_vendor_tokens')
    op.drop_index(op.f('ix_user_vendor_tokens_id'), table_name='user_vendor_tokens')
    op.drop_table('user_vendor_tokens')
    op.drop_index(op.f('ix_profiles_profile_id'), table_name='profiles')
    op.drop_table('profiles')
    op.drop_index(op.f('ix_organizations_org_id'), table_name='organizations')
    op.drop_table('organizations')
    op.drop_index(op.f('ix_vendors_vendor_id'), table_name='vendors')
    op.drop_table('vendors')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_index(op.f('ix_users_phone'), table_name='users')
    op.drop_index(op.f('ix_users_id'), table_name='users')
    op.drop_index(op.f('ix_users_email'), table_name='users')
    op.drop_table('users')
    # ### end Alembic commands ###
