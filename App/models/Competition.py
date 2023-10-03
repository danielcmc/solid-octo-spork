from App.database import db

class Competition(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    participants = db.relationship('Participation', back_populates='competition', lazy=True)
    creator_id = db.Column(db.Integer, nullable=False)

    def get_json(self):
        return {
            'id': self.id,
            'name': self.name
        }