import requests
import conf
import data


def create_order():
    return requests.post(conf.URL_SERVICE + conf.CREATE_ORDER_PATH, json=data.order_body, headers=data.headers)


def track_order(track_id):
    return requests.get(conf.URL_SERVICE + conf.TRACK_ORDER_PATH + str(track_id), headers=data.headers)
