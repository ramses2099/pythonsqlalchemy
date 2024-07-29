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

    # insert user and rol
    # with Session(engine) as session:
    #     user1 = User(
    #         name="spongebob",
    #         fullname="Spongebob Squarepants"                       
    #     )
    #     # insert profile
    #     profile1 = Profile(name = "admin", user=user1)
    #     session.add_all([user1, profile1])
    #     session.commit()
    
    # insert other user and rol
    # with Session(engine) as session:
    #     user2 = User(
    #         name="ramses",
    #         fullname="ramses perez"                       
    #     )
    #     # insert profile
    #     profile2 = Profile(name = "Normal", user=user2)
    #     session.add_all([user2, profile2])
    #     session.commit()
    
    # select user where id == 1
    # with Session(engine) as session:
    #     stmt = select(User).where(User.id == 1)
    #     user = session.execute(statement=stmt).scalar_one()
    #     print(Style.GREEN + f"User Name:{user.name} and Profile: {user.profile.name}")
    #     print(Style.WHITE)
    
    # update user where id ==2
    # with Session(engine) as session:
    #     stmt = select(User).where(User.id == 2)
    #     user = session.execute(statement=stmt).scalar_one()
    #     print(Style.GREEN + f"Full Name:{user.fullname}")
    #     user.fullname = "juan lopez"
    #     print(Style.GREEN + f"Update Full Name:{user.fullname}")
    #     print(Style.WHITE)
    #     session.commit()
    
    # delete profile
    # with Session(engine) as session:
    #     profile2 = session.get(Profile, 2)
    #     session.delete(profile2)
    #     session.commit()
    
    # select all users
    with Session(engine) as session:
        stmt = select(User)        
        users = session.execute(statement=stmt)
                
        for i, user in enumerate(users):
            print(f"index : {i} name :{user[0].name} fullname : {user[0].fullname}")
           
        # print(Style.WHITE)
    

   
if __name__ == "__main__":
    main()
