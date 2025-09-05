from abc import ABC, abstractmethod
import copy


class Pokemon(ABC):
    """
    Classe abstraite représentant un Pokémon
    """

    # -------------------------------------------------------------------------
    # Constructeur
    # -------------------------------------------------------------------------
    def __init__(self, stat_max=None, stat_current=None, level=0, name=None, type_pk=None):
        self._stat_max: Statistic = stat_max
        self._stat_current: Statistic = stat_current
        self._level: int = level
        self._name: str = name
        self._type: str = type_pk

    # -------------------------------------------------------------------------
    # Méthodes abstraites
    # -------------------------------------------------------------------------
    @abstractmethod
    def get_pokemon_attack_coef(self) -> float:
        """
        Méthode abstraite à implémenter dans les sous-classes.
        Doit retourner un multiplicateur de dégâts en fonction du type du Pokémon.
        """
        pass

    # -------------------------------------------------------------------------
    # Méthodes concrètes communes
    # -------------------------------------------------------------------------
    def level_up(self) -> None:
        """Augmente le niveau du Pokémon"""
        self._level += 1

    def reset_actual_stat(self) -> None:
        """Réinitialise les statistiques actuelles à leur maximum"""
        self._stat_current = copy.deepcopy(self._stat_max)

    def get_hit(self, damage) -> None:
        """Réduit les PV actuels en fonction des dégâts reçus"""
        if damage > 0:
            if damage < self.hp_current:
                self.hp_current -= damage
            else:
                self.hp_current = 0

    def __str__(self):
        res = f"I am {self.name}, level : {self.level}, attack coef : {self.get_pokemon_attack_coef()}"
        return res

    # -------------------------------------------------------------------------
    # Getters et Setters avec @property
    # -------------------------------------------------------------------------
    @property
    def attack(self):
        return self._stat_max.attack

    @property
    def hp(self):
        return self._stat_max.hp

    @property
    def defense(self):
        return self._stat_max.defense

    @property
    def sp_atk(self):
        return self._stat_max.sp_atk

    @property
    def sp_def(self):
        return self._stat_max.sp_def

    @property
    def speed(self):
        return self._stat_max.speed

    @property
    def attack_current(self):
        return self._stat_current.attack

    @attack_current.setter
    def attack_current(self, value):
        self._stat_current.attack = value

    @property
    def hp_current(self):
        return self._stat_current.hp

    @hp_current.setter
    def hp_current(self, value):
        self._stat_current.hp = value

    @property
    def defense_current(self):
        return self._stat_current.defense

    @defense_current.setter
    def defense_current(self, value):
        self._stat_current.defense = value

    @property
    def sp_atk_current(self):
        return self._stat_current.sp_atk

    @sp_atk_current.setter
    def sp_atk_current(self, value):
        self._stat_current.sp_atk = value

    @property
    def sp_def_current(self):
        return self._stat_current.sp_def

    @sp_def_current.setter
    def sp_def_current(self, value):
        self._stat_current.sp_def = value

    @property
    def speed_current(self):
        return self._stat_current.speed

    @speed_current.setter
    def speed_current(self, value):
        self._stat_current.speed = value

    @property
    def level(self):
        return self._level

    @property
    def name(self):
        return self._name
