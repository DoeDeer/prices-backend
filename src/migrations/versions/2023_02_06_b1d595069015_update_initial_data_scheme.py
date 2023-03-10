"""Update initial data scheme

Revision ID: b1d595069015
Revises:
Create Date: 2023-02-06 13:28:52.419801

"""

from alembic import op
import sqlalchemy as sa
from sqlalchemy.schema import Sequence, CreateSequence, DropSequence


# revision identifiers, used by Alembic.
revision = "b1d595069015"
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Update Customers table
    op.add_column(
        "customers", sa.Column("title", sa.String(length=100), nullable=True)
    )
    op.execute("UPDATE customers SET title = customer")
    op.alter_column("customers", "title", nullable=False)
    op.drop_column("customers", "customer")
    # Add integer pkey
    op.execute(CreateSequence(Sequence("customers_id_seq")))
    op.add_column("customers", sa.Column(
        "id",
        sa.Integer(),
        nullable=False,
        server_default=sa.text("nextval('customers_id_seq'::regclass)"),
    ))
    op.create_primary_key("customers_pkey", table_name="customers", columns=["id"])

    # Update Ports table
    op.alter_column(
        "ports",
        "code",
        existing_type=sa.TEXT(),
        type_=sa.String(length=5),
        existing_nullable=False,
    )
    op.alter_column(
        "ports",
        "name",
        existing_type=sa.TEXT(),
        type_=sa.String(length=100),
        existing_nullable=False,
    )

    # Update Prices table
    # Add integer pkey
    op.execute(CreateSequence(Sequence("prices_id_seq")))
    op.add_column("prices", sa.Column(
        "id",
        sa.Integer(),
        nullable=False,
        server_default=sa.text("nextval('prices_id_seq'::regclass)"),
    ))
    op.create_primary_key("prices_pkey", table_name="prices", columns=["id"])
    op.alter_column(
        "prices",
        "orig_code",
        existing_type=sa.TEXT(),
        type_=sa.String(length=5),
        existing_nullable=False,
    )
    op.alter_column(
        "prices",
        "dest_code",
        existing_type=sa.TEXT(),
        type_=sa.String(length=5),
        existing_nullable=False,
    )
    op.add_column("prices", sa.Column("customer_id", sa.Integer(), nullable=True))
    op.execute("UPDATE prices SET customer_id = (SELECT c.id FROM customers AS c WHERE c.title = customer)")
    op.drop_column("prices", "customer")
    op.alter_column(
        "prices",
        "customer_id",
        new_column_name="customer",
        nullable=False,
    )

    # Add additional indexes and fkeys
    op.create_index(op.f("ix_prices_customer"), "prices", ["customer"], unique=False)
    op.create_index(op.f("ix_prices_day"), "prices", ["day"], unique=False)
    op.create_foreign_key(op.f("prices_customer_fkey"), "prices", "customers", ["customer"], ["id"])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    # Drop additional indexes and fkeys
    op.drop_constraint(op.f("prices_customer_fkey"), "prices", type_="foreignkey")
    op.drop_index(op.f("ix_prices_day"), table_name="prices")
    op.drop_index(op.f("ix_prices_customer"), table_name="prices")

    # Drop changes at Prices table
    op.add_column("prices", sa.Column("customer_customer", sa.Text(), nullable=True))
    op.execute("UPDATE prices SET customer_customer = (SELECT c.title FROM customers AS c WHERE c.id = customer)")
    op.drop_column("prices", "customer")
    op.alter_column(
        "prices",
        "customer_customer",
        new_column_name="customer",
        nullable=False,
    )
    op.alter_column(
        "prices",
        "dest_code",
        existing_type=sa.String(length=5),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "prices",
        "orig_code",
        existing_type=sa.String(length=5),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.drop_column("prices", "id")
    op.execute(DropSequence(Sequence("prices_id_seq")))

    # Drop changes at Ports table
    op.alter_column(
        "ports",
        "name",
        existing_type=sa.String(length=100),
        type_=sa.TEXT(),
        existing_nullable=False,
    )
    op.alter_column(
        "ports",
        "code",
        existing_type=sa.String(length=5),
        type_=sa.TEXT(),
        existing_nullable=False,
    )

    # Drop changes at Customers table
    op.add_column("customers", sa.Column("customer", sa.TEXT(), nullable=True))
    op.execute("UPDATE customers SET customer = title")
    op.drop_column("customers", "id")
    op.drop_column("customers", "title")
    op.execute(DropSequence(Sequence("customers_id_seq")))
    # ### end Alembic commands ###
