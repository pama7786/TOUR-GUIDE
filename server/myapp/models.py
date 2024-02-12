from myapp import db
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

user_site_table = db.Table('user_site_association',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id'), primary_key=True),
    db.Column('site_id', db.Integer, db.ForeignKey('sites.id'), primary_key=True)
)
class User(db.Model, SerializerMixin):
    __tablename__ = "users"
    serialize_rules = ('-sites','-reviews.user',)
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)

    reviews = db.relationship('Review', backref='user')

    # sites = db.relationship('TouristAttractionSite', secondary=user_site_table, back_populates='users')

class TouristAttractionSite(db.Model, SerializerMixin):
    __tablename__ = 'sites'

    serialize_rules = ('-user.sites',)

    id = db.Column(db.Integer, primary_key=True)
    touristSite = db.Column(db.String)
    location = db.Column(db.String)
    description = db.Column(db.String)
    rating = db.Column(db.Integer)

    reviews = db.relationship('Review', backref='site')
    
    # users = db.relationship('User', secondary=user_site_table, back_populates='sites')

class Review(db.Model, SerializerMixin):
    __tablename__ = "reviews"


    serialize_rules = ('-user.reviews','-site.reviews','-user.sites.reviews',)
    # serialize_rules = ('-users',)

    id = db.Column(db.Integer, primary_key=True)
    rating = db.Column(db.String)

    @validates('rating')
    def validate_rating(self, key, rating):
        if len(rating) < 8:
            raise ValueError("rating not enough")
        return rating

    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    tourist_attraction_site_id = db.Column(db.Integer, db.ForeignKey('sites.id'))

    # def to_dict(self):
    #     return {
    #         'id': self.id,
    #         'rating': self.rating

    #     }

    # User.sites = db.relationship('TouristAttractionSite', secondary=user_site_table, backref=db.backref('users'))

