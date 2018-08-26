import argparse
import logging
import sys

import requests

logger = logging.getLogger(__name__)


def get_event_ids(event_tag):
    url = f'https://app2.sli.do/api/v0.5/events?hash={event_tag}'
    re = requests.get(url)
    d = re.json()[0]
    return d['uuid'], d['event_id']


def authenticate(event_uuid):
    url = f'https://app2.sli.do/api/v0.5/events/{event_uuid}/auth'
    re = requests.post(url, json={})
    logger.info(f'{re.status_code}, {re.text}')
    token = re.json()['access_token']
    return f'Bearer {token}'


def vote(event_id, question_id, event_uuid):
    url = f'https://app2.sli.do/api/v0.5/events/{event_id}/questions/{question_id}/like'
    auth = authenticate(event_uuid)
    re = requests.post(url, json={
        'score': 1
    }, headers={
        'Authorization': auth,
    })
    logger.info(f'{re.status_code}, {re.text}')
    return re.json()['event_question_score']


def main():
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    parser = argparse.ArgumentParser()
    parser.add_argument('event_tag', type=str)
    parser.add_argument('question_id', type=int)
    parser.add_argument('votes', type=int)
    args = parser.parse_args()
    event_uuid, event_id = get_event_ids(args.event_tag)
    for i in range(args.votes):
        logger.info(f'vote #{i}')
        vote(event_id, args.question_id, event_uuid)


if __name__ == '__main__':
    main()
