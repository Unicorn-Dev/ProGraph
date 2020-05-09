from .graph import Graph



def AdjListDictToString(AdjListDict):
    """Convert AdjListDict to it's string representation"""
    assert isinstance(AdjListDict, dict)
    AdjListString = str(AdjListDict)
    return AdjListString

def StringToAdjListDict(AdjListString):
    """Convert AdjListString to it's dict representation"""
    assert isinstance(AdjListString, str)
    AdjListDict = eval(AdjListString)
    return AdjListDict

def get_graph_img():
    import matplotlib.pyplot as plt
    from io import BytesIO
    from base64 import b64encode as encode
    import base64
    from PIL import Image, ImageDraw

    im = Image.new('RGB', (100, 100))

    draw = ImageDraw.Draw(im)
    draw.line((0, 0) + im.size, fill=128)
    draw.line((0, im.size[1], im.size[0], 0), fill=128)

    with BytesIO() as buffer:
        im.save(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
    
    return encode(image_png).decode('utf-8')
