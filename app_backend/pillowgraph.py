import math
from io import BytesIO
from base64 import b64encode as encode
from PIL import Image, ImageDraw


class PillowGraph:
    def __init__(self, _AdjList=dict(), directed=False, _imgXsize=600, _imgYsize=600):
        assert isinstance(_AdjList, dict)
        _vertices = list(_AdjList.keys())
        self.imgXsize = _imgXsize
        self.imgYsize = _imgYsize
        self.vertices = dict()
        for ver in _vertices:
            self.vertices[ver] = [0, 0]
        self.add_vertex()
        self.AdjList = _AdjList

    def add_vertex(self, _vertex=None) -> None:
        if _vertex is not None:
            self.vertices[_vertex] = [0, 0]
            self.AdjList[_vertex] = dict()
        N = len(self.vertices)
        for ind, xy in enumerate(self.vertices.values()):
            xy[0] = (1 + math.cos(ind * 2 * math.pi / N) / 1.3) * self.imgXsize / 2
            xy[1] = (1 + math.sin(ind * 2 * math.pi / N) / 1.3) * self.imgYsize / 2
        

    def add_edge(self, _from, _to, _weight=None) -> bool:
        assert isinstance(_weight, None) or isinstance(_weight, int)
        try:
            self.AdjList[_from]
            self.AdjList[_to]
        except:
            return False
        self.AdjList[_from][_to] = _weight
        return True

    def draw(self, color='y'):

        im = Image.new('RGBA', (self.imgXsize, self.imgYsize))
        
        draw = ImageDraw.Draw(im)
        self._draw_vertexes(draw)
        self._draw_edges(draw)
                
        with BytesIO() as buffer:
            im.save(buffer, format='png')
            buffer.seek(0)
            image_png = buffer.getvalue()

        return encode(image_png).decode('utf-8')

    def _draw_vertexes(self, draw):
        r = int((self.imgXsize + self.imgYsize) / 40)   
        for xy in self.vertices.values():
            draw.ellipse(
                [xy[0] - r, xy[1] - r, xy[0] + r, xy[1] + r],
                fill=(100, 0, 0, 230), 
                outline=(100, 100, 100, 200), 
                width=int(r / 10))
    
    def _draw_edges(self, draw):
        for _from, val in self.AdjList.items():
            for _to, weight in val.items():
                xy = (self.vertices[_from][0], self.vertices[_from][1], 
                    self.vertices[_to][0], self.vertices[_to][1])
                draw.line(xy, fill=(50, 50, 50, 250), 
                    width=int((self.imgXsize + self.imgYsize) / 200))
