from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from sqlalchemy_utils import database_exists, drop_database, create_database

from database_setup import Category, CategoryItem, User, Base

engine = create_engine('sqlite:///itemcatalog.db')

'''Clear existing database and tables'''
Base.metadata.drop_all(engine)

'''Creating new database and tables'''
Base.metadata.create_all(engine)

''' Bind the engine to the metadata that can be accessed through a DBSession instance'''
Base.metadata.bind = engine

DBSession = sessionmaker(bind=engine)
'''A DBSession() instance establishes all conversations with the database'''

session = DBSession()

# Create dummy user
user1 = User(name="Sundharesan R", email="sundharesanr@udacity.com",
             picture='https://www.google.co.in/images/branding/googlelogo/1x/googlelogo_color_272x92dp.png')
session.add(user1)
session.commit()

# Items for Cars
category1 = Category(name="Cars", user_id=1)

session.add(category1)
session.commit()

item1 = CategoryItem(name="Ford", user_id=1, description="The Ford Motor Company is an American multinational automaker headquartered in Dearborn, Michigan, a suburb of Detroit. It was founded by Henry Ford and incorporated on June 16, 1903.", category=category1)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Volvo", user_id=1,  description="The Volvo Group is a Swedish multinational manufacturing company headquartered in Gothenburg. While its core activity is the production, distribution and sale of trucks, buses and construction equipment.", category=category1)

session.add(item2)
session.commit()

item3 = CategoryItem(name="Hyundai", user_id=1, description="Hyundai Group is a multinational chaebol headquartered in Seoul, South Korea. It was founded by Chung Ju-yung in 1947 as a construction firm and Chung was directly in control of the company until his death in 2001.", category=category1)

session.add(item3)
session.commit()

# Items for Buildings
category2 = Category(name="Buildings", user_id=1)

session.add(category2)
session.commit()

item1 = CategoryItem(name="Apartment", user_id=1, description="An apartment, flat or unit is a self-contained housing unit that occupies only part of a building, generally on a single level.", category=category2)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Villa", user_id=1,  description="A villa was originally an ancient Roman upper-class country house. Since its origins in the Roman villa, the idea and function of a villa have evolved considerably.", category=category2)

session.add(item2)
session.commit()


# Items for Vegetables
category3 = Category(name="Vegetables", user_id=1)

session.add(category3)
session.commit()

item1 = CategoryItem(name="Eggplant", user_id=1, description="Eggplant, or aubergine, is a species of nightshade, grown for its edible fruit. Eggplant is the common name in North America, Australia and New Zealand, but British English uses the French word aubergine.", category=category3)

session.add(item1)
session.commit()

item2 = CategoryItem(name="Tomato", user_id=1, description="The tomato is the edible, often red, fruit of the plant Solanum lycopersicum, commonly known as a tomato plant. The plant belongs to the nightshade family, which is called Solanaceae. The species originated in Central and South America.", category=category3)

session.add(item2)
session.commit()


# Items for Places
category4 = Category(name="Places", user_id=1)

session.add(category4)
session.commit()


categories = session.query(Category).all()
for category in categories:
    print "Category: " + category.name
