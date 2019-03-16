
from django.http import HttpResponse
from google.cloud import datastore
from random import randint

client = datastore.Client()


def push(request):

    entity_imcomplete_key = client.key('generic')
    new_entity = datastore.Entity(key=entity_imcomplete_key)
    new_entity.update({
        'number': randint(100, 200)
    })
    client.put(new_entity)
    return HttpResponse("Pushed " + str(new_entity['number']))


def get(request):

    query = client.query(kind='generic')
    result = list(query.fetch())
    payload = []
    for item in result:
        payload.append(item['number'])
    return HttpResponse(str(payload))
