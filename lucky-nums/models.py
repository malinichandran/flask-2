from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def connect_db(app):
    db.app = app
    db.init_app(app)


class GetLuckyNum(db.Model):
    """GetLuckyNum Model"""

    __tablename__ = "luckynums"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.Text, nullable=False)
    email = db.Column(db.Text, nullable=False)
    birth_year = db.Column(db.Integer, nullable=False)
    color = db.Column(db.Text,nullable=False)

    def serialize(self):
        """Returns a dict representation of luckynums which we can turn into JSON"""
        return {
            
            'name': self.name,
            'email': self.email,
            'birth_year':self.birth_year,
            'color':self.color
        }