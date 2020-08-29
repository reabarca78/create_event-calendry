import requests
from payload import create_payload
from configurations import *
from logs import write_log, found_in_log


def create_event(schedule, type_id):
    payload = create_payload(email, invitee_landed_at, schedule, type_id)
    r = requests.post(url=endpoint, json=payload)
    if r.status_code == 200:
        write_log(f'{type_id}/{schedule}')
    print(f'Response: {r.text}')


if not found_in_log(gym_id, get_schedule(tomorrow)):
    create_event(get_schedule(tomorrow), gym_id)
