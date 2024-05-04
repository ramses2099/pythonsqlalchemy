from sqlalchemy import create_engine
from models import Base, User, Address
from sqlalchemy.orm import Session
from sqlalchemy import select


def main():
    # create engine
    engine = create_engine("sqlite:///database.db", echo=True)

    # create database and all table
    Base.metadata.create_all(engine)

    # insert rows
    # with Session(engine) as session:
    #     row1 = User(
    #         name="spongebob",
    #         fullname="Spongebob Squarepants",
    #         addresses=[Address(email_address="spongebob@sqlalchemy.org")],
    #     )

    #     row2 = User(
    #         name="ramses",
    #         fullname="ramses the first",
    #         addresses=[
    #             Address(email_address="ramses@sqlalchemy.org"),
    #             Address(email_address="ramses@sqlalchemy.org"),
    #         ],
    #     )

    #     row3 = User(name="antonio", fullname="antonio the second")

    #     session.add_all([row1, row2, row3])

    #     session.commit()
    with Session(engine) as session:
        stmt = select(User).where(User.name.in_(["ramses", "antonio"]))

        for user in session.scalars(stmt):
            print(user)


if __name__ == "__main__":
    main()
