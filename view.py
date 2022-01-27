import jsonschema
from flask import request, jsonify
from flask.views import MethodView
from app import app

from models import Advertisement
from schema import ADVERTISEMENT_CREATE

class AdvertisementView(MethodView):

    def get(self, advertisement_id):
        advertisement = Advertisement.by_id(advertisement_id)
        return jsonify(advertisement.to_dict())

    def post(self):
        advertisement = Advertisement(**request.json)
        jsonschema.validate(advertisement, ADVERTISEMENT_CREATE)
        advertisement.add()
        return jsonify(advertisement.to_dict())

    def delete(self, advertisement_id):
        advertisement = Advertisement.by_id(advertisement_id)
        advertisement.delete()
        return jsonify(advertisement.to_dict())

@app.route('/advert/', methods=['GET','POST', ])
def advert():
    response = jsonify({'status': 'OK'})
    return response


app.add_url_rule('/advertisement/<int:advertisement_id>', view_func=AdvertisementView.as_view('advertisement_get'), methods=['GET', ])
app.add_url_rule('/advertisement/', view_func=AdvertisementView.as_view('advertisement_create'), methods=['POST', ])
app.add_url_rule('/advertisement/<int:advertisement_id>', view_func=AdvertisementView.as_view('advertisement_delete'), methods=['DELETE', ])
app.run(port=8000)