from model_carrito import db

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
def delete_instance(model, id):
    model.query.filter_by(id=id).delete()
    commit_changes()

# PATCH
def edit_instance(model, id, datos):
    instance = model.query.filter_by(id=id).all()[0]
    instance.status_carrito = datos["estado"]
    instance.date_carrito = datos["fecha"]
    instance.customer_id_fk = datos["customer_id"]
    commit_changes()
    

# GET
def get_by_id(model, id):
    instance = model.query.filter_by(id=id).first()
    return instance

# COMMIT
def commit_changes():
    db.session.commit()
