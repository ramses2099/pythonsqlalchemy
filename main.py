from sqlalchemy import create_engine
from models import *
from sqlalchemy.orm import Session
from sqlalchemy import select
from style import Style


def main():
    # connection string for postgres db
    # url_postgress ="postgresql+psycopg2://postgres:S3cret@10.0.0.50:5432/mydatabase"
    # connection string for sqlite
    url_sqlilte = "sqlite:///database.db"
    
    # create engine
    engine = create_engine(url_sqlilte, echo=True)

    # create database and all table
    Base.metadata.create_all(engine)

    # insert rows
    # with Session(engine) as session:
    #     user1 = User(
    #         name="spongebob",
    #         fullname="Spongebob Squarepants"                       
    #     )
    #     # insert profile
    #     profile1 = Profile(name = "admin", user=user1)
    #     session.add_all([user1, profile1])
    #     session.commit()

    # select user where id == 1
    # with Session(engine) as session:
    #     stmt = select(User).where(User.id == 1)
    #     user = session.execute(statement=stmt).scalar_one()
    #     print(Style.GREEN + f"User Name:{user.name} and Profile: {user.profile.name}")
    #     print(Style.WHITE)

    #  TODO: Data Manipulation with the ORM


if __name__ == "__main__":
    main()
