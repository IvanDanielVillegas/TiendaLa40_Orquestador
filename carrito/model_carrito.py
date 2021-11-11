import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Carrito(db.Model):
    __tablename__ = 'carrito'
    id  = db.Column("carrito_id", db.Integer, primary_key=True)
    status_carrito = db.Column(db.String(100))
    date_carrito = db.Column(db.DateTime, default=db.func.now())
    #customer_id_fk  = db.Column("customer_id", db.Integer, foreign_key=True)
    customer_id_fk  = db.Column("customer_id", db.Integer)
    

    def __init__(self, datos):
        self.status_carrito = datos["estado"]
        self.date_carrito = datos["fecha"]
        self.customer_id_fk = datos["customer_id"]




