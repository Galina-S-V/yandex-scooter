import configuration
import requests
import data


def post_new_order(body):
    return requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
        headers=data.headers,
    )


def get_order_by_track(track):
    return requests.get(
        configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK_PATH,
        # params используется для формирования параметров запроса (query string)
        # https://requests.readthedocs.io/en/latest/user/quickstart/#passing-parameters-in-urls
        params={"t": track},
        headers=data.headers,
    )
