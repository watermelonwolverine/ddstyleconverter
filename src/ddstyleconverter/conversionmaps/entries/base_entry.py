class BaseEntry:

    def __init__(self,
                 from_texture: str,
                 to_texture: str):

        if type(from_texture) is not str:
            raise TypeError()
        if type(to_texture) is not str:
            raise TypeError()

        self.__from_texture = from_texture
        self.__to_texture = to_texture

    def get_from_texture(self):
        return self.__from_texture

    def get_to_texture(self):
        return self.__to_texture
