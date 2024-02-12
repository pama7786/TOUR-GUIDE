from myapp.models import User, TouristAttractionSite, Review, user_site_table
from myapp import db, app
from faker import Faker
import random


fake = Faker()


with app.app_context():
    User.query.delete()
    TouristAttractionSite.query.delete()
    Review.query.delete()

    users = []
    for i in range(20):
        print('**all good**')
        people = User(username=fake.name())
        users.append(people)
    db.session.add_all(users)
    db.session.commit()

    popularSites = [
    "Maasai Mara National Reserve",
    "Amboseli National Park",
    "Nairobi National Park",
    "Samburu National Reserve",
    "Tsavo National Park",
    "Lake Nakuru National Park",
    "Lamu Island",
    "Diani Beach",
    "Hell's Gate National Park",
    "Mount Kenya",
    "Lake Turkana",
    "Great Rift Valley",
    "Mount Longonot National Park",
    "Malindi",
    "Karura Forest",
    "Sheldrick Elephant Orphanage",
    "Giraffe Centre",
    "Bomas of Kenya",
    "Kisumu Impala Sanctuary",
    "Kakamega Forest Reserve"
]

    SiteLocation = [
        "Southwestern Kenya, adjacent to Tanzania",
        "Southern Kenya, near the Tanzanian border",
        "Just 7 kilometers from Nairobi city center",
        "Northern Kenya, along the Ewaso Nyiro River",
        "Southeastern Kenya",
        "Rift Valley, central Kenya",
        "Off the northeastern coast of Kenya",
        "South of Mombasa, on the Indian Ocean",
        "Rift Valley, near Lake Naivasha",
        "Central Kenya",
        "Northwestern Kenya", 
        "Runs through Kenya from north to south",
        "Rift Valley, near Naivasha",
        "Along the Kenyan coast",
        "Nairobi",
        "Nairobi",
        "Nairobi",
        "Kisumu, western Kenya",
        "Western Kenya",
        "Eastern Kenya"
    ]

    SiteDescription = [
        "Known for the Great Migration of wildebeest and zebras, Maasai Mara offers stunning wildlife and scenic landscapes.",
        "Home to iconic views of Mount Kilimanjaro and abundant wildlife, including elephants and lions.",
        "A unique wildlife park located just outside Kenya's capital, Nairobi, offering the chance to see animals against a city backdrop.",
        "Known for its rare northern species of wildlife, including Grevy's zebras and reticulated giraffes.",
        "One of the largest national parks in the world, split into Tsavo East and Tsavo West, with diverse landscapes and wildlife.",
        "Famous for its flamingo populations and rhino sanctuary, offering great bird-watching and wildlife experiences.",
        "A picturesque and tranquil island with well-preserved Swahili architecture and rich cultural heritage.",
        "A stunning coastal destination with white sandy beaches, coral reefs, and water sports opportunities.",
        "Known for its geothermal activity, unique landscapes, and rock climbing opportunities.",
        "Africa's second-highest mountain, a UNESCO World Heritage site, and a popular trekking destination.",
        "The world's largest desert lake, known for its striking colors, unique geological formations, and diverse tribes.",
        "A geological wonder with dramatic landscapes, hot springs, and numerous lakes.",
        "Home to Mount Longonot, a dormant volcano, and a great spot for hiking and panoramic views.",
        "A coastal town with beautiful beaches, historical sites, and a vibrant Swahili culture.",
        "An urban forest in Nairobi with walking and biking trails, waterfalls, and birdwatching opportunities.",
        "A rescue center for orphaned elephants and rhinos, offering a chance to see these magnificent creatures up close.",
        "A conservation center where you can feed and interact with endangered Rothschild's giraffes.",
        "Showcasing traditional Kenyan culture through music, dance, and artifacts.",
        "A wildlife sanctuary on the shores of Lake Victoria, home to impalas and other animals.",
        "A tropical rainforest with diverse flora and fauna, including rare birds and primates."
    ]





    sites = []
    for i in range(20):
        available_sites = TouristAttractionSite(
            touristSite=popularSites[i],            
            description=SiteDescription[i],
            location=SiteLocation[i],
            rating=random.randint(1, 5))
        print('***Good****') 
        sites.append(available_sites)
    db.session.add_all(sites)
    db.session.commit()

    reviews = []
    for i in range(20):
        r = Review(rating=random.choice(['satisfied', 'slightly satisfied', 'unsatisfied', 'very unsatisfied']), user_id=random.randint(1, 20), tourist_attraction_site_id=random.randint(1, 20))
        reviews.append(r)
    db.session.add_all(reviews)
    db.session.commit()

    # join = []
    # for i in db.session.query(Review).all():
    #     j = user_site_table.insert().values(user_id=i.user_id, sites_id =i. tourist_attraction_site_id)
    #     join.append(j)
    # db.session.add_all(join)
    # db.session.commit()
 

    join = []

    for review in db.session.query(Review).all():
        user_id = review.user_id
        site_id = review.tourist_attraction_site_id

        join_data = {'user_id': user_id, 'site_id': site_id}

        join.append(join_data)

    db.session.execute(user_site_table.insert().values(join))
    db.session.commit()


#     add_category = categories.insert()…values(
#     task_id=new…id, cat_id=category_exist.id, time=datetime…now()
# )
# db.session…execute(add_category)






