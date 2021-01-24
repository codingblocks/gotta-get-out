import pygame
from pytmx import load_pygame

from src.config import TITLE_SCREEN_TMX_PATH
from src.scenes.scene import Scene
from pygame import Surface
import typing
import src.scenes.globals as g


class TitleScene(Scene):
    def __init__(self, title: str = "Scene", state: dict = typing.Dict):
        self.resources = g.resources
        self.messaging = g.messaging
        self.tmx_data = load_pygame(TITLE_SCREEN_TMX_PATH)
        super().__init__(title, state)

    def update(self, dt):
        g.messaging.info("Oh no, your ship is damaged. Pirates will be here soon!", 1)
        g.messaging.update(dt)
        if pygame.mouse.get_pressed()[0]:
            self.change_scene("ship")

    def render(self, surface: Surface):
        self.render_tmx(self.tmx_data, surface)
        g.messaging.render(surface)

    def _start_over(self):
        self.change_scene("ship")
