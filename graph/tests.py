from django.test import TestCase
from django.urls import reverse
from django.test import Client
from django.utils import timezone
import datetime
import string

from .models import Graph


def create_graph(AdjList, days):
    """
    Create a graph with the given `AdjList` and published the
    given number of `days` offset to now (negative for graph published
    in the past, positive for graphs that have yet to be published).
    """
    time = timezone.now() + datetime.timedelta(days=days)
    return Graph.objects.create(AdjList=AdjList, pub_date=time)


class URLsTest(TestCase):
    def test_graph_main_url(self):
        """
        Test that graph main page url works.
        """
        client = Client()
        response = client.get('/graph/')
        self.assertEqual(response.status_code, 200)

    def test_concrete_graph_url(self):
        """
        Test that concreate graph page url works.
        And that not-existing graph url isn't work.
        """
        graph = create_graph('{1: {2: 4, 3: 1}, 2: {1: 0, 3: 8}, 3: {}}', 0)
        client = Client()
        response = client.get('/graph/{}/'.format(graph.id))
        self.assertEqual(response.status_code, 200)
        response = client.get('/graph/{}/'.format(graph.id + 1))
        self.assertEqual(response.status_code, 404)
        
