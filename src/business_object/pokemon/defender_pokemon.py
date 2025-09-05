from business_object.pokemon.abstract_pokemon import Pokemon


class DefenderPokemon(Pokemon):
    def get_pokemon_attack_coef(self) -> float:
        """Coefficient pour un Defender: basé sur attack + defense"""
        return 1 + (self.attack_current + self.defense_current) / 200
