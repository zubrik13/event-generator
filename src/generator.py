from faker import Faker
from faker_events import Event, EventGenerator
from datetime import datetime, timedelta

fake = Faker()

structure = {
    'event_time': '',
    'type': 'example',
    'event_id': '',
    'user_id': '',
    'first_name': '',
    'last_name': '',
    'spent': 0,
    'status': 'normal'
}


def open_account(event, profile: dict) -> dict:
    return {
        'event_time': event.time,
        'event_id': event.id,
        'user_id': profile.id,
        'first_name': profile.first_name,
        'last_name': profile.last_name,
    }


def make_payment(event, profile: dict):
    event.data['event_time'] = event.time
    event.data['spent'] += fake.random_number(2)


def status_update(event, profile: dict):
    if event.data['spent'] > 100 and event.data['status'] != 'big spender':
        return {
            'event_time': event.time,
            'status': 'big spender'
        }

    # No Event will be created when if condition is not True
    return 'skip'


# Random Events, 0 means infinite number of events, 60 is events per minute rate
new_account = Event(structure, open_account, 0, 60)
payment = Event(structure, make_payment, 0, 60)
new_account >> payment

EventGenerator.set_first_events(new_account)