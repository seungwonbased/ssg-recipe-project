from app import db


post_liker = db.Table(
    'post_liker',
    db.Column('user_id', db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('post_id', db.Integer, db.ForeignKey(
        'post.id', ondelete='CASCADE'), primary_key=True)
)


comment_liker = db.Table(
    'comment_liker',
    db.Column('user_id', db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), primary_key=True),
    db.Column('comment_id', db.Integer, db.ForeignKey(
        'comment.id', ondelete='CASCADE'), primary_key=True)
)


class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(200), nullable=False)
    content = db.Column(db.Text(), nullable=False)
    price = db.Column(db.Integer, nullable=True)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('post_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    liker = db.relationship('User', secondary=post_liker,
                            backref=db.backref('post_liker_set'))
    food_id = db.Column(db.Integer, db.ForeignKey(
        'food.id', ondelete='CASCADE'), nullable=True)
    food = db.relationship('Food', backref=db.backref('post_set'))


class Comment(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    post_id = db.Column(db.Integer, db.ForeignKey(
        'post.id', ondelete='CASCADE'))
    post = db.relationship('Post', backref=db.backref('comment_set'))
    content = db.Column(db.Text(), nullable=False)
    create_date = db.Column(db.DateTime(), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey(
        'user.id', ondelete='CASCADE'), nullable=False)
    user = db.relationship('User', backref=db.backref('comment_set'))
    modify_date = db.Column(db.DateTime(), nullable=True)
    liker = db.relationship('User', secondary=comment_liker,
                            backref=db.backref('comment_liker_set'))


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)


class Food(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    foodname = db.Column(db.String(150), unique=True, nullable=True)
    food_price = db.Column(db.Integer, unique=False, nullable=True)
    food_unit = price = db.Column(db.Integer, unique=False, nullable=True)
    food_category = db.Column(
        db.String(150), unique=False, nullable=True)
