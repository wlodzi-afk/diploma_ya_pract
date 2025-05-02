import requests
import conf
import data


track_id = 1


def test_create_order():
    r = requests.post(conf.URL_SERVICE + conf.CREATE_ORDER_PATH, json=data.order_body, headers=data.headers)
    assert r.status_code == 201
    global track_id
    track_id = r.json()["track"]


def test_track_order():
    r = requests.get(conf.URL_SERVICE + conf.TRACK_ORDER_PATH + str(track_id), headers=data.headers)
    assert r.status_code == 200
