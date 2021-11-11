import flask_sqlalchemy

db = flask_sqlalchemy.SQLAlchemy()

class Cantidad(db.Model):
    __tablename__ = 'cantidad'
    #id  = db.Column("cantidad_id", db.Integer, primary_key=True)
    quantity = db.Column("cantidad_total",db.Integer)
    product_id_fk  = db.Column("product_id", db.Integer,primary_key=True)
    carrito_id_fk  = db.Column("carrito_id", db.Integer,primary_key=True)
    #product_id_fk  = db.Column("product_id", db.Integer, foreign_key=True)
    #carrito_id_fk  = db.Column("carrito_id", db.Integer, foreign_key=True)

    def __init__(self, datos):
        self.quantity = datos["cantidad_total"]
        self.product_id_fk = datos["product_id"]
        self.carrito_id_fk = datos["carrito_id"]
