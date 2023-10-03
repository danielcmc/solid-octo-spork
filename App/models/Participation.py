from App.database import db

class Participation(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competition.id'), nullable=False)
    rank = db.Column(db.Integer, nullable=False)
    points_earned = db.Column(db.Integer, nullable=False)

    user = db.relationship('User', back_populates='participations')
    competition = db.relationship('Competition', back_populates='participants')

    def calculate_points(self):
        if self.rank == 1:
            return 10
        elif self.rank == 2:
            return 7
        elif self.rank == 3:
            return 4
        else:
            return 1

    def get_json(self):
        return {
            'id': self.id,
            'user_id': self.user_id,
            'competition_id': self.competition_id,
            'rank': self.rank,
            'points_earned': self.calculate_points()
        }