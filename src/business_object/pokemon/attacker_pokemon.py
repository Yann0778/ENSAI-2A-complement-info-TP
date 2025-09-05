from business_object.pokemon.abstract_pokemon import Pokemon


class AttackerPokemon(Pokemon):
    def get_pokemon_attack_coef(self) -> float:
        """Coefficient pour un Attacker: basé sur speed + attack"""
        return 1 + (self.speed_current + self.attack_current) / 200
