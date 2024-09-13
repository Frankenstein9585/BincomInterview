from collections import defaultdict
from datetime import datetime

from flask import jsonify, render_template, request

from config import app, db
from models import classes


@app.route('/')
def index():
    return 'Hello World'


@app.route('/polling_unit_result')
def polling_unit_result():
    unique_id = 9
    announced_pu_results = classes['announced_pu_results']
    polling_unit = classes['polling_unit']
    polling_unit_info = db.session.query(polling_unit).filter_by(uniqueid=unique_id).first()
    pu_results = db.session.query(announced_pu_results).filter_by(polling_unit_uniqueid=unique_id)
    return render_template('polling_unit_result.html', pu_results=pu_results, polling_unit_info=polling_unit_info)


@app.route('/lga-result')
def lga_result():
    lga = classes['lga']
    lgas = db.session.query(lga).all()
    return render_template('lga_result.html', lgas=lgas)


@app.route('/compute-result')
def compute_result():
    lga_id = request.args.get('lga_id')
    print(lga_id)
    party_scores = defaultdict(int)
    polling_unit = classes['polling_unit']
    announced_pu_results = classes['announced_pu_results']
    polling_units = db.session.query(polling_unit).filter_by(lga_id=lga_id).all()
    for polling_unit in polling_units:
        print(polling_unit.uniqueid)
        pu_results = db.session.query(announced_pu_results).filter_by(polling_unit_uniqueid=polling_unit.uniqueid)
        for pu_result in pu_results:
            party_scores[pu_result.party_abbreviation] += pu_result.party_score
    print(party_scores)
    return jsonify(party_scores)


@app.route('/new-result')
def new_result():
    polling_unit = classes['polling_unit']
    polling_unit_numbers = db.session.query(polling_unit.polling_unit_number).distinct().all()
    party_list = ['ACN', 'ANPP', 'CDC', 'CPP', 'CPP', 'DPP', 'JP', 'LABO', 'PDP', 'PPA']  # had to hardcode this
    return render_template('store_result.html', party_list=party_list, polling_unit_numbers=polling_unit_numbers)


@app.route('/submit-results', methods=['GET', 'POST'])
def submit_results():
    polling_units = classes['polling_unit']
    announced_pu_results = classes['announced_pu_results']
    if request.method == 'POST':
        votes_dict = request.form.to_dict()
        polling_unit_number = votes_dict.pop('polling_unit_number')
        polling_unit = db.session.query(polling_units).filter_by(polling_unit_number=polling_unit_number).first()
        for party, votes in votes_dict.items():
            if votes == '':
                continue
            # used dummy data here
            result = announced_pu_results(
                polling_unit_uniqueid=polling_unit.uniqueid,
                party_abbreviation=party,
                party_score=votes,
                entered_by_user='Admin',
                date_entered=datetime.utcnow(),
                user_ip_address='182.762.18.29')
            db.session.add(result)
        db.session.commit()
    return 'Success'
