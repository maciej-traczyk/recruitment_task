import pygame

class OctagonShape():

    def __init__(self, x: int, y: int, width: int, height: int, coner_angle: int):

        self.__coner_angle = coner_angle
        self.__width = width
        self.__height = height

        self._shape_points = self.__get_shape(x, y)
        self.rect = pygame.Rect(x, y, self.__width, self.__height)    

    def __get_shape(self, x: int, y: int) -> list[tuple[int, int]]:
        return [
            (x + self.__coner_angle, y),
            (x + self.__width - self.__coner_angle, y),
            (x + self.__width, y + self.__coner_angle),
            (x + self.__width, y + self.__height - self.__coner_angle),
            (x + self.__width - self.__coner_angle, y + self.__height),
            (x + self.__coner_angle, y + self.__height),
            (x, y + self.__height - self.__coner_angle),
            (x, y + self.__coner_angle)
        ]