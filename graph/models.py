from django.db import models
import base64


class Graph(models.Model):
    AdjList = models.CharField(max_length=10000)
    pub_date = models.DateTimeField('date published')

    def __str__(self):
        return self.AdjList

class Image(models.Model):
    graph = models.ForeignKey(Graph, on_delete=models.CASCADE)
    _image = models.TextField(blank=True)

    def set_data(self, image):
        self._image = base64.encodestring(image)

    def get_data(self):
        return base64.decodestring(self._image)

    image = property(get_data, set_data)
