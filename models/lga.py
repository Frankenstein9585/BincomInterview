from config import app, db
from sqlalchemy.ext.automap import automap_base

with app.app_context():
    Base = automap_base()

    Base.prepare(db.engine, reflect=True)

    for class_ in Base.classes:
        print(str(class_).split('.'))
    #
    # PU_RESULTS = Base.classes.announced_pu_results
    #
    # pu_results = db.session.query(PU_RESULTS).filter_by(polling_unit_uniqueid=8)
    #
    # for pu_result in pu_results:
    #     print(pu_result.party_abbreviation, pu_result.party_score)
