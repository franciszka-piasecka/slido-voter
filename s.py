import argparse
import random

import requests

headers = {
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-GB,en;q=0.9,en-US;q=0.8,pl;q=0.7',
    'content-type': 'application/json;charset=UTF-8',
    'accept': 'application/json, text/plain',
    'cache-control': 'no-cache, no-store',
    'authority': 'app2.sli.do'
}


def get_event_uuid(event_tag):
    url = f'https://app2.sli.do/api/v0.5/events?hash={event_tag}'
    re = requests.get(url, headers=headers)
    d = re.json()[0]
    return d['uuid'], d['event_id']


def authenticate(event_uuid):
    url = f'https://app2.sli.do/api/v0.5/events/{event_uuid}/auth'
    re = requests.post(url, json={}, headers=headers)
    print(re, re.text)
    token = re.json()['access_token']
    return f'Bearer {token}'


def vote(event_id, question_id, event_uuid):
    url = f'https://app2.sli.do/api/v0.5/events/{event_id}/questions/{question_id}/like'
    print('authenticate')
    auth = authenticate(event_uuid)
    print('vote')
    re = requests.post(url, json={
        'score': 1
    }, headers={
        'Authorization': auth,
        **headers
    })
    print(re, re.text)
    return re.json()['event_question_score']


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('event_tag', type=str)
    parser.add_argument('question_id', type=int)
    parser.add_argument('votes', type=int)
    args = parser.parse_args()
    print('get_uuid')
    event_uuid, event_id = get_event_uuid(args.event_tag)
    print(event_uuid)
    random.seed()
    for i in range(args.votes):
        print(f'vote #{i}')
        vote(event_id, args.question_id, event_uuid)
