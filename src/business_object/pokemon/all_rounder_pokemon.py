from business_object.pokemon.abstract_pokemon import Pokemon


class AllRounderPokemon(Pokemon):
    def get_pokemon_attack_coef(self) -> float:
        """Coefficient pour un All-Rounder: basé sur sp_atk + sp_def"""
        return 1 + (self.sp_atk_current + self.sp_def_current) / 200
