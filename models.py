from config import app, db
from sqlalchemy.ext.automap import automap_base

with app.app_context():
    Base = automap_base()
    Base.prepare(db.engine, reflect=True)

    classes = {}

    for class_ in Base.classes:
        class_name = str(class_).split('.')[-1].replace("'>", '')
        classes[class_name] = class_
