from app.models.db import db

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True) # INT
    text = db.Column(db.String(200)) # VARCHAR(200)
    createdAt = db.Column(db.DateTime(timezone=False))
    doneAt = db.Column(db.DateTime(timezone=False))
    deletedAt = db.Column(db.DateTime(timezone=False))

    def toJson(self):
        return {
            'id': self.id,
            'text': self.text,
            'createdAt': self.createdAt,
            'doneAt': self.doneAt,
            'deletedAt': self.deletedAt,
        }