from abc import ABC, abstractmethod

class AttackComponent(ABC):
    """
    Classe abstrata para componentes de ataque.
    Define a interface que todos os componentes de ataque devem implementar.
    """

    STATE_ATTACKING = 'attacking'
    STATE_IDLE = 'idle'
    KNOCKBACK_DISTANCE = 90


    def __init__(self, entity, event_manager) -> None:
        self.entity = entity
        self.event_manager = event_manager
        self.state = self.STATE_IDLE


    @abstractmethod
    def attack(self):
        pass


    @abstractmethod
    def update(self, target_sprites):
        pass


    @abstractmethod
    def _perform_attack(self, target_sprites):
        pass


    @abstractmethod
    def _reset_attack(self):
        pass


    def inflict_damage(self, target, damage: int):
        """ Inflige dano ao alvo e verifica a vida restante. """
        target.receive_damage(damage)
        self._check_target_life(target)


    def knockback_target(self, target):
        """ Aplica efeito de recuo do alvo com base em sua posição. """
        target.rect.centerx += self.KNOCKBACK_DISTANCE if target.rect.centerx > self.entity.rect.centerx else -self.KNOCKBACK_DISTANCE


    def _check_target_life(self, target):
        """ Verifica se a vida do alvo chegou a zero e lida de acordo. """
        if target.life <= 0:
            target.defeat()
            target.kill()