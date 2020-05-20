from django.test import TestCase
from django.urls import reverse
from django.test import Client
from app_backend import proxy_convert_functions as pc_funcs
from .pillowgraph import PillowGraph

class ProxyConvertFunkTest(TestCase):
    def test_proxy_convert(self):
        dicAdjList = {1: {2: 4, 3: 1}, 2: {1: 0, 3: 8}, 3: {}}
        strAdjList = '{1: {2: 4, 3: 1}, 2: {1: 0, 3: 8}, 3: {}}'
        self.assertEqual(dicAdjList, 
            pc_funcs.StringToAdjListDict(pc_funcs.AdjListDictToString(dicAdjList)))
        self.assertEqual(strAdjList, 
            pc_funcs.AdjListDictToString(pc_funcs.StringToAdjListDict(strAdjList)))


class PillowGraphTest(TestCase):
    def test_vertices_number(self):
    	G = PillowGraph({1: {2: 4, 3: 1}, 2: {1: 0, 3: 8}, 3: {}})
    	self.assertEqual(len(G.vertices), 3)