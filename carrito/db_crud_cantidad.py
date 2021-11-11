from model_cantidad import db

# GET
def get_all(model):
    data = model.query.all()
    return data

# POST
def add_instance(model, datos):
    instance = model(datos)
    db.session.add(instance)
    commit_changes()

# DELETE
def delete_instance(model, product_id,carrito_id):
    model.query.filter_by(product_id_fk=product_id,carrito_id_fk=carrito_id).delete()
    commit_changes()

# PATCH
def edit_instance(model, product_id,carrito_id, datos):
    #FILTER WITH TWO IDS
    instance = model.query.filter_by(product_id_fk=product_id,carrito_id_fk=carrito_id).all()[0]
    instance.quantity = datos["cantidad_total"]
    instance.product_id_fk = datos["product_id"]
    instance.carrito_id_fk = datos["carrito_id"]
    commit_changes()
    

# GET
def get_by_id(model, product_id,carrito_id):
    instance = model.query.filter_by(product_id_fk=product_id,carrito_id_fk=carrito_id).first()
    return instance

# COMMIT
def commit_changes():
    db.session.commit()
