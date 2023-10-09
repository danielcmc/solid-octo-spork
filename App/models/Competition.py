from App.database import db

class Competition(db.Model):
    __tablename__='competition'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    creator_id = db.Column(db.Integer, db.ForeignKey('Admin.id'), nullable=False)
    participants = db.relationship('Student', secondary="participation", overlaps='competetions', lazy=True)


    def get_json(self):
        return {
            'id': self.id,
            'name': self.name
        }