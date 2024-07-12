import pygame
from abc import ABC, abstractmethod

class AnimationComponent(ABC):
    """ Gerencia a animação da entidade. """

    def __init__(self, entity, animation_frames, animation_speed) -> None:
        self.entity = entity
        self.animation_frames = animation_frames
        self.animation_speed = animation_speed
        self.current_frame_index = self.frame_counter = 0
        self.last_frame_index = -1  # Rastrear quando a imagem realmente muda


    def update(self, delta_time):
        """ Atualiza a animação. """
        self._increment_animation_counter(delta_time)
        self._update_current_frame()
        self._update_image_and_mask()


    def _increment_animation_counter(self, delta_time):
        self.frame_counter += self.animation_speed * delta_time
        if self.frame_counter >= len(self.animation_frames):
            self.frame_counter = 0


    def _update_current_frame(self):
        """ Atualiza a imagem e a máscara do sprite. """
        self.current_frame_index = int(self.frame_counter)


    def _update_image_and_mask(self):
        """ Atualiza a imagem e a máscara do sprite. """
        if self.current_frame_index != self.last_frame_index:
            self.entity.image = self.animation_frames[self.current_frame_index]
            if self.entity.movement_component.facing_right:
                self.entity.image = pygame.transform.flip(self.entity.image, True, False)
            self.rect = self.entity.image.get_rect(center=self.entity.rect.center)