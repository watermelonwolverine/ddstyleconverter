from typing import Dict

from dungeondraft.ddobject import DDObject


class Matching:

    def __init__(self,
                 object_matching: Dict[DDObject, DDObject]):
        self.object_matching = object_matching
