from .builder import DATASETS
from .custom import CustomDataset


@DATASETS.register_module()
class MyDataset(CustomDataset):
    # 总的类别
    CLASSES = ('null', 'accessories', 'bag', 'belt', 'blazer', 'blouse',
               'bodysuit', 'boots', 'bra', 'bracelet', 'cape', 'cardigan', 'clogs',
               'coat', 'dress', 'earrings', 'flats', 'glasses', 'gloves', 'hair',
               'hat', 'heels', 'hoodie', 'intimate', 'jacket', 'jeans', 'jumper',
               'leggings', 'loafers', 'necklace', 'panties', 'pants', 'pumps',
               'purse', 'ring', 'romper', 'sandals', 'scarf', 'shirt', 'shoes',
               'shorts', 'skin', 'skirt', 'sneakers', 'socks', 'stockings',
               'suit', 'sunglasses', 'sweater', 'sweatshirt', 'swimwear',
               't-shirt', 'tie', 'tights', 'top', 'vest', 'wallet', 'watch',
               'wedges')

    # 所需的类
    # CLASSES = ('null', 'blazer', 'blouse',
    #        'bodysuit',   'cape', 'cardigan',
    #        'coat', 'dress', 'hoodie', 'jacket', 'jumper',
    #         'romper',  'shirt',
    #        'suit',  'sweater', 'sweatshirt', 'swimwear',
    #        't-shirt',  'top', 'vest')

    PALETTE = [[0, 0, 0], [0, 0, 63], [0, 0, 126], [0, 0, 255], [0, 63, 0],
               [0, 63, 63], [0, 63, 126], [0, 63, 255], [0, 126, 0], [0, 126, 63],
               [0, 126, 126], [0, 126, 255], [0, 255, 0], [0, 255, 63], [0, 255, 126],
               [0, 255, 255], [63, 0, 0], [63, 0, 63], [63, 0, 126], [63, 0, 255],
               [63, 63, 0], [63, 63, 63], [63, 63, 126], [63, 63, 255], [63, 126, 0],
               [63, 126, 63], [63, 126, 126], [63, 126, 255], [63, 255, 0], [63, 255, 63],
               [63, 255, 126], [63, 255, 255], [126, 0, 0], [126, 0, 63], [126, 0, 126],
               [126, 0, 255], [126, 63, 0], [126, 63, 63], [126, 63, 126], [126, 63, 255],
               [126, 126, 0], [126, 126, 63], [126, 126, 126], [126, 126, 255], [126, 255, 0],
               [126, 255, 63], [126, 255, 126], [126, 255, 255], [255, 0, 0], [255, 0, 63],
               [255, 0, 126], [255, 0, 255], [255, 63, 0], [255, 63, 63], [255, 63, 126],
               [255, 63, 255], [255, 126, 0], [255, 126, 63], [255, 126, 126]]

    def __init__(self, **kwargs):
        super(MyDataset, self).__init__(**kwargs)
