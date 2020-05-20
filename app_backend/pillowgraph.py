import math
from io import BytesIO
from base64 import b64encode as encode
from PIL import Image, ImageDraw, ImageFont
import platform

from .exceptions import *


class PillowGraph:
    def __init__(self, _AdjList=dict(), directed=False,
                 _imgXsize=2000, _imgYsize=2000):
        """
        self.vertices is dict where
            keys is vertex
            vals is coords
            Example: {'1': [0, 0.4], '2': [2.32, 1.223]}
        self.AdjList is dict of dicts
            AdjList[_from] is dict where
                keys is _to vertex 
                and vals is list of edges weight
            Example: {'1': {}, '2': {'1': [0]}}
        """
        assert isinstance(_AdjList, dict)
        _vertices = list(_AdjList.keys())
        self.imgXsize = _imgXsize
        self.imgYsize = _imgYsize
        self.vertices = dict()
        for ver in _vertices:
            self.vertices[ver] = [0, 0]
        self.set_vertex_coords()
        self.AdjList = _AdjList

    def set_vertex_coords(self) -> None:
        N = len(self.vertices)
        for ind, xy in enumerate(self.vertices.values()):
            xy[0] = (1 + math.cos(ind * 2 * math.pi / N) / 1.3) \
                    * self.imgXsize / 2
            xy[1] = (1 + math.sin(ind * 2 * math.pi / N) / 1.3) \
                    * self.imgYsize / 2

    def draw(self):
        im = Image.new('RGBA', (self.imgXsize, self.imgYsize))

        draw = ImageDraw.Draw(im)
        self._draw_edges(draw)
        self._draw_vertices(draw)

        with BytesIO() as buffer:
            im.save(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()

        return encode(image_png).decode('utf-8')

    def algodraw(self, AlgoSequense, algo_iteration):
        im = Image.new('RGBA', (self.imgXsize, self.imgYsize))

        draw = ImageDraw.Draw(im)
        self._draw_edges(draw, AlgoSequense[:algo_iteration])
        self._draw_vertices(draw)

        with BytesIO() as buffer:
            im.save(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()

        return encode(image_png).decode('utf-8')

    def _draw_vertices(self, draw):
        r = int((self.imgXsize + self.imgYsize) / 40)
        for name, xy in self.vertices.items():
            draw.ellipse(
                [xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r],
                fill=(100, 0, 0, 230),
                outline=(100, 100, 100, 200),
                width=int(r / 10)
            )
            font = ImageFont.truetype('static/fonts/CGR.ttf', int(r * 1.5))
            textX, textY = draw.textsize(str(name), font=font)
            draw.text([xy[0] - textX / 2, xy[1] - textY / 2],
                      str(name), font=font, fill=(256, 256, 256, 150))

    def _draw_edges(self, draw, special_edges=None):
        for _from, val in self.AdjList.items():
            for _to, weights in val.items():
                xy = (self.vertices[_from][0], self.vertices[_from][1],
                      self.vertices[_to][0], self.vertices[_to][1])
                draw.line(xy, fill=(50, 50, 50, 250),
                          width=int((self.imgXsize + self.imgYsize) / 200))
                centerXY = [(xy[0] + xy[2]) / 2, (xy[1] + xy[3]) / 2]
                alpha = math.pi / 11
                dx1 = ((xy[2] - xy[0]) * math.cos(alpha) + (
                            xy[3] - xy[1]) * math.sin(alpha)) / 8
                dy1 = ((xy[3] - xy[1]) * math.cos(alpha) - (
                            xy[2] - xy[0]) * math.sin(alpha)) / 8
                dx2 = ((xy[2] - xy[0]) * math.cos(alpha) - (
                            xy[3] - xy[1]) * math.sin(alpha)) / 8
                dy2 = ((xy[3] - xy[1]) * math.cos(alpha) + (
                            xy[2] - xy[0]) * math.sin(alpha)) / 8
                xy_up_arrow_line = [centerXY[0] - dx1, centerXY[1] - dy1,
                                    centerXY[0], centerXY[1]]
                xy_down_arrow_line = [centerXY[0] - dx2, centerXY[1] - dy2,
                                      centerXY[0], centerXY[1]]
                draw.line(xy_up_arrow_line, fill=(50, 50, 50, 250),
                          width=int((self.imgXsize + self.imgYsize) / 300))
                draw.line(xy_down_arrow_line, fill=(50, 50, 50, 250),
                          width=int((self.imgXsize + self.imgYsize) / 300))
        if special_edges:
            for edge in special_edges:
                _from, _to = edge
                color = (255, 164, 4, 250)
                xy = (self.vertices[_from][0], self.vertices[_from][1],
                      self.vertices[_to][0], self.vertices[_to][1])
                draw.line(xy, fill=color,
                          width=int((self.imgXsize + self.imgYsize) / 200))
                centerXY = [(xy[0] + xy[2]) / 2, (xy[1] + xy[3]) / 2]
                alpha = math.pi / 11
                dx1 = ((xy[2] - xy[0]) * math.cos(alpha) + (
                            xy[3] - xy[1]) * math.sin(alpha)) / 8
                dy1 = ((xy[3] - xy[1]) * math.cos(alpha) - (
                            xy[2] - xy[0]) * math.sin(alpha)) / 8
                dx2 = ((xy[2] - xy[0]) * math.cos(alpha) - (
                            xy[3] - xy[1]) * math.sin(alpha)) / 8
                dy2 = ((xy[3] - xy[1]) * math.cos(alpha) + (
                            xy[2] - xy[0]) * math.sin(alpha)) / 8
                xy_up_arrow_line = [centerXY[0] - dx1, centerXY[1] - dy1,
                                    centerXY[0], centerXY[1]]
                xy_down_arrow_line = [centerXY[0] - dx2, centerXY[1] - dy2,
                                      centerXY[0], centerXY[1]]
                draw.line(xy_up_arrow_line, fill=color,
                          width=int((self.imgXsize + self.imgYsize) / 300))
                draw.line(xy_down_arrow_line, fill=color,
                          width=int((self.imgXsize + self.imgYsize) / 300))

    def add_vertex(self, vertex):
        """
        Raise Exception if something goes wrong
        and vertex is not added
        """
        assert isinstance(vertex, str)
        if len(vertex) > 15:
            raise ToLongName(vertex)
        try:
            self.AdjList[vertex]
        except KeyError:
            pass
        else:
            raise VretexAlreadyExist(vertex)
        self.AdjList[vertex] = {}

    def add_edge(self, edge):
        """
        Raise Exception if sometsing gone wrong
        and edge is not added
        """
        assert isinstance(edge, str)
        _to, _from, _weight = None, None, None
        try:
            _to, _from, _weight = edge.split()
        except:
            try:
                _to, _from = edge.split()
            except:
                raise VretexNumberError(edge)
        else:
            try:
                _weight = int(_weight)
            except:
                raise IncorrectWeightError(edge)
        if _from not in self.AdjList or _to not in self.AdjList:
            raise VretexDoesNotExist(edge)
        try:
            self.AdjList[_to][_from]
        except:
            self.AdjList[_to][_from] = []
        self.AdjList[_to][_from].append(_weight)

    def delete_vertex(self, vertex):
        """
        Raise Exception if sometsing gone wrong
        and vertex is not deleted
        """
        assert isinstance(vertex, str)
        try:
            self.AdjList[vertex]
        except KeyError:
            raise VretexDoesNotExist(vertex)
        del self.AdjList[vertex]
        for edge_dic in self.AdjList.values():
            try:
                del edge_dic[vertex]
            except:
                pass

    def delete_edge(self, edge):
        """
        Raise Exception if sometsing gone wrong
        and edge is not deleted.
        """
        assert isinstance(edge, str)
        _to, _from, _weight = None, None, None
        try:
            _to, _from, _weight = edge.split()
        except:
            try:
                _to, _from = edge.split()
            except:
                raise VretexNumberError(edge)
        else:
            try:
                _weight = int(_weight)
            except:
                raise IncorrectWeightError(edge)
        try:
            self.AdjList[_to]
            self.AdjList[_from]
        except KeyError:
            raise VretexDoesNotExist(edge)
        try:
            self.AdjList[_to][_from]
            if _weight is None:
                self.AdjList[_to][_from].pop()
            else:
                self.AdjList[_to][_from].remove(_weight)
            if len(self.AdjList[_to][_from]) == 0:
                del self.AdjList[_to][_from]
        except:
            raise EdgeDoesNotExist(edge)

    def dfs(self, vertex, colors, queue, parent=None):
        if colors[vertex] == 'W':
            colors[vertex] = 'G'
            if parent:
                edge = parent, vertex
                queue.append(edge)
            for to in self.AdjList[vertex]:
                self.dfs(to, colors, queue, vertex)
            colors[vertex] = 'B'

    def bfs(self, queue, walked, sequence):
        while not queue.empty():
            vertex = queue.get()
            for to in self.AdjList[vertex]:
                if not walked[to]:
                    queue.put(to)
                    walked[to] = True
                    edge = vertex, to
                    sequence.append(edge)
