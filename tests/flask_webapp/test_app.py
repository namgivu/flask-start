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

    def test221101_dictkeyorder(self):
        client = app.test_client()  # ref. https://flask.palletsprojects.com/en/2.2.x/testing/#sending-requests-with-the-test-client

        reqbody = {
            'chart'     : 'FMPTFVS',
            'flight_no' : '607',
        }
        resp = client.post('/some_POST_endpoint', data=json.dumps(reqbody), headers={'Content-Type': 'application/json'})
        assert resp.status_code == 200

        #region assert key listing order ref. Adil https://accumulus-sg.slack.com/archives/D02JERVUUDT/p1666182355582629
        reqbody = resp.json

        d                = reqbody['test_key_order']
        ACT_dictkeyorder = list(d.keys())

        EXP_dictkeyorder = ['Dec 2022', 'Jan 2023', 'Nov 2022']
        assert ACT_dictkeyorder == EXP_dictkeyorder
        #endregion assert key listing order ref. Adil https://accumulus-sg.slack.com/archives/D02JERVUUDT/p1666182355582629
