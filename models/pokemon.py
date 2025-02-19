from models.window import Window
import pygame
import json
import random

with open("models/pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)

evolutions = {
    1: {"evolves_to": 2, "level_required": 5},
    2: {"evolves_to": 3, "level_required": 10},
    4: {"evolves_to": 5, "level_required": 5},
    5: {"evolves_to": 6, "level_required": 10},
    7: {"evolves_to": 8, "level_required": 5},
    8: {"evolves_to": 9, "level_required": 10},
    10: {"evolves_to": 11, "level_required": 5},
    11: {"evolves_to": 12, "level_required": 10},
    16: {"evolves_to": 17, "level_required": 5},
    17: {"evolves_to": 18, "level_required": 10},
    23: {"evolves_to": 24, "level_required": 5},
    25: {"evolves_to": 26, "level_required": 5},
    35: {"evolves_to": 36, "level_required": 5},
    66: {"evolves_to": 67, "level_required": 5},
    67: {"evolves_to": 68, "level_required": 10},
    81: {"evolves_to": 82, "level_required": 5},
    92: {"evolves_to": 93, "level_required": 5},
    93: {"evolves_to": 94, "level_required": 10},
    104: {"evolves_to": 105, "level_required": 5},
    147: {"evolves_to": 148, "level_required": 5},
    148: {"evolves_to": 149, "level_required": 10},
    228: {"evolves_to": 229, "level_required": 5}
}


class Pokemon():
    """class to init pokemon, caract and draw"""

    def __init__(self, level = 1):
        # background image
        self.window = Window()

        self.level = level
        self.xp = 0
        self.xp_to_next_level = 15

        self.pokemon_player_id = 2
        self.load_pokemon_stats("player")

        self.pokemon_opponent_id = self.get_random_active_pokemon_id()
        self.load_pokemon_stats("opponent")

        self.pokemon_sprites_list = self.get_pokemon_sprite()

    def get_pokemon_sprite(self):
        """Get all pokemon sprites paths"""
        return [pokemon["sprites"]["front"] for pokemon in data]

    def get_random_active_pokemon_id(self):
        """Get a random active pokemon ID"""
        available_ids = [pokemon["pokedex_id"] for pokemon in data if pokemon["active"] == True]
        return random.choice(available_ids)
    
    def get_pokemon_data(self, pokemon_id):
        """Get all pokemon data from its ID"""
        for pokemon in data:
            if pokemon["pokedex_id"] == pokemon_id:
                return pokemon
        return None
    
    def load_pokemon_stats(self, target):
        """Load all pokemon stats player or opponent"""
        pokemon_id = getattr(self, f"pokemon_{target}_id")
        pokemon_data = None

        for pokemon in data:
            if pokemon["pokedex_id"] == pokemon_id:
                pokemon_data = pokemon
                break

        if not pokemon_data:
            return
        
        setattr(self, f"pokemon_{target}_name", pokemon_data["name"])
        setattr(self, f"pokemon_{target}_life", pokemon_data["stat"]["hp"])
        setattr(self, f"pokemon_{target}_atk", pokemon_data["stat"]["atk"])
        setattr(self, f"pokemon_{target}_def", pokemon_data["stat"]["def"])
        setattr(self, f"pokemon_{target}_type", pokemon_data["type"])

        print(f"Type du {target}: {pokemon_data['type']} (ID: {pokemon_id}, Nom: {pokemon_data['name']})")
        
        resistance_found = False
        for resistance in pokemon_data["resistances"]:
            if resistance["name"] == pokemon_data["type"]:
                setattr(self, f"pokemon_{target}_resistance", resistance["multiply"])
                resistance_found = True
                break
        
        if not resistance_found:
            print(f"ATTENTION: Aucune résistance trouvée pour {pokemon_data['name']} de type {pokemon_data['type']}")
            setattr(self, f"pokemon_{target}_resistance", 1.0)

        sprite_direction = "back" if target == "player" else "front"
        sprite_path = pokemon_data["sprites"][sprite_direction]
        sprite = pygame.image.load(sprite_path).convert_alpha()
        sprite = pygame.transform.scale(sprite, (sprite.get_width() * 3, sprite.get_height() * 3))
        setattr(self, f"pokemon_{target}_sprite", sprite)

    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.2)
        self.try_evolve()

    def get_pokemon_player_attack(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["atk"]

    def get_pokemon_player_name(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["name"]

    def get_pokemon_player_hp(self):

        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["hp"]

    def get_pokemon_player_defense(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["def"]
            
    def get_pokemon_player_type(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["type"]

    def get_pokemon_player_resistance(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                for resistance in pokemon["resistances"]:
                    if resistance["name"] == self.pokemon_player_type:
                        return resistance["multiply"]
            
    def get_pokemon_player_type(self):
        for pokemon in data:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["type"]
            
    def gain_xp(self, amount):
        self.xp += amount
        while self.xp >= self.xp_to_next_level:
            self.level_up()

    def level_up(self):
        self.level += 1
        self.xp -= self.xp_to_next_level
        self.xp_to_next_level = int(self.xp_to_next_level * 1.2)

        self.try_evolve()

    def try_evolve(self):
        if self.pokemon_player_id in evolutions:
            evolution = evolutions[self.pokemon_player_id]

            if self.level >= evolution["level_required"]:
                self.pokemon_player_id = evolution["evolves_to"]
                self.load_pokemon_stats("player")
    
    def win_battle(self):
        self.gain_xp(5)

    def calculate_damage(self, attacker_atk, defender_def, defender_resistance):
        if random.random() <= 0.1:
            return 0

        raw_damage = max(1, attacker_atk - defender_def)
        final_damage = raw_damage * defender_resistance
        final_damage = max(1, final_damage)

        return final_damage
    
    def player_attack(self):
        damage = self.calculate_damage(
            self.pokemon_player_atk,
            self.pokemon_opponent_def,
            self.pokemon_opponent_resistance
        )
        print(f"Joueur attaque: ATK={self.pokemon_player_atk}, DEF adversaire={self.pokemon_opponent_def}, "
        f"Résistance={self.pokemon_opponent_resistance}, Dégâts={damage}")

        self.pokemon_opponent_life -= damage
        self.draw_damage(damage, self.pokemon_opponent_name)

    def opponent_attack(self):
        damage = self.calculate_damage(
            self.pokemon_opponent_atk, 
            self.pokemon_player_def,
            self.pokemon_player_resistance
        )

        print(f"Adversaire attaque: ATK={self.pokemon_opponent_atk}, DEF joueur={self.pokemon_player_def}, "
        f"Résistance={self.pokemon_player_resistance}, Dégâts={damage}")

        self.pokemon_player_life -= damage
        self.draw_damage(damage, self.pokemon_player_name)

    def draw_damage(self, damage, target):
        if damage >= 1:
            message = f"{target}: -{damage} HP"
        else:
            message = f"ATTACK MISS | {target}: - {damage} HP"

        if target == self.pokemon_opponent_name:
            position = ((self.window.screen_width/2) - (len(message) * 4), 25)
        else:
            position = ((self.window.screen_width/2), 300)

        damage_text = self.window.text_font_battle.render(message, True, self.window.RED)
        self.window.screen.blit(damage_text, position)
        pygame.display.update()

    def draw_pokemon_opponent_hp(self):
        self.window.draw_text(
            f"{self.pokemon_opponent_name} HP: {self.pokemon_opponent_life}",
            self.window.text_font_battle,
            self.window.WHITE, 560, 25
        )

    def draw_pokemon_player_hp(self):
        self.window.draw_text(
            f"{self.pokemon_player_name} HP : {self.pokemon_player_life}",
            self.window.text_font_battle,
            self.window.WHITE, 160, 200
        )

    def draw_pokemon_xp(self):
        self.window.draw_text(
            f"{self.pokemon_player_name} XP : {self.xp}/{self.xp_to_next_level} (Niveau {self.level})",
            self.window.text_font_hp_opponent,
            self.window.WHITE, 160, 180
        )

    def draw_pokemon_player(self):
        rect = self.pokemon_player_sprite.get_rect()
        rect.center = (250, 335)
        self.window.screen.blit(self.pokemon_player_sprite, rect)

    def draw_pokemon_opponent(self):
        rect = self.pokemon_opponent_sprite.get_rect()
        rect.center = (650, 160)
        self.window.screen.blit(self.pokemon_opponent_sprite, rect)

    def debug_pokemon_data(self):
        """Affiche les informations de débogage pour les deux Pokémon"""
        print("\n=== INFORMATIONS POKÉMON JOUEUR ===")
        print(f"ID: {self.pokemon_player_id}")
        print(f"Nom: {self.pokemon_player_name}")
        print(f"Type: {self.pokemon_player_type}")
        print(f"ATK: {self.pokemon_player_atk}")
        print(f"DEF: {self.pokemon_player_def}")
        print(f"Résistance: {self.pokemon_player_resistance}")
        
        print("\n=== INFORMATIONS POKÉMON ADVERSAIRE ===")
        print(f"ID: {self.pokemon_opponent_id}")
        print(f"Nom: {self.pokemon_opponent_name}")
        print(f"Type: {self.pokemon_opponent_type}")
        print(f"ATK: {self.pokemon_opponent_atk}")
        print(f"DEF: {self.pokemon_opponent_def}")
        print(f"Résistance: {self.pokemon_opponent_resistance}")
        print("\n")