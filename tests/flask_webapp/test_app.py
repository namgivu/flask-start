import json

from flask_webapp.app import app


class Test_apiapp_endpoint:

    def test221100(self):
        client = app.test_client()  # ref. https://flask.palletsprojects.com/en/2.2.x/testing/#sending-requests-with-the-test-client

        reqbody = {
            'chart'     : 'FMPTFVI',
            'flight_no' : 'TGW124',
        }
        resp = client.post('/some_POST_endpoint', data=json.dumps(reqbody), headers={'Content-Type': 'application/json'})
        assert resp.status_code == 200

        try:    respbody = resp.json
        except: pass
        assert isinstance(respbody, dict)
