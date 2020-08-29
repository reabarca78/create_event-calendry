from datetime import datetime, timedelta

invitee_landed_at = datetime.now().strftime('%Y-%m-%dT%H:%M:%S.000Z')
email = 'reabarca78@hotmail.com'
endpoint = 'https://calendly.com/api/booking/invitees'
gym_id = 'GEBO2PJ7K6KJL2TI'
pool_id = ''
tomorrow = datetime.now() + timedelta(days=1)
after_tomorrow = datetime.now() + timedelta(days=2)
hour_week = '16:30:00-06:00'
hour_weekend = '11:00:00-06:00'


def get_schedule(event_date):
    if event_date.strftime('%A') == 'Saturday' or event_date.strftime('%A') == 'Sunday':
        return event_date.strftime('%Y-%m-%dT') + hour_weekend
    return event_date.strftime('%Y-%m-%dT') + hour_week

