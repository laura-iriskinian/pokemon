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

    def __init__(self, pokemon_id,level = 1):
        # background image
        self.window = Window()
        # pokemon 
        self.pokemon_player = ""
        self.pokemon_id = pokemon_id
        self.pokemon_sprite = self.get_pokemon_sprite()

        self.pokemon_life = self.get_pokemon_hp()
        self.pokemon_name = self.get_pokemon_name()
        self.pokemon_type = self.get_pokemon_type()
        self.pokemon_def = self.get_pokemon_defense()
        # self.pokemon_resistance = self.get_pokemon_resistance()
        self.pokemon_atk = self.get_pokemon_attack()
        self.level = level
        self.xp = 0
        self.xp_to_next_level = 15

        self.damage = ""
        self.target = ""

        self.position_pokemon = ""



# defs get players

    def get_pokemon_sprite(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"]==self.pokemon_id:
                sprite_path = pokemon["sprites"]["back"]
                self.pokemon_sprite = pygame.image.load(sprite_path).convert_alpha()
                self.pokemon_sprite = pygame.transform.scale(self.pokemon_sprite, (self.pokemon_sprite.get_width()*3, self.pokemon_sprite.get_height()*3))
                return self.pokemon_sprite

    def get_pokemon_attack(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
                return pokemon["stat"]["atk"]

    def get_pokemon_name(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
                return pokemon["name"]

    def get_pokemon_hp(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
                return pokemon["stat"]["hp"]

    def get_pokemon_defense(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
                return pokemon["stat"]["def"]
            
    def get_pokemon_type(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
                return pokemon["type"]

    def get_pokemon_resistance(self,attacker_type):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
                for resistance in pokemon["resistances"]:
                    if resistance["name"] == attacker_type:
                        return resistance["multiply"]
            
    def get_pokemon_type(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_id:
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
        if self.pokemon_id in evolutions:
            evolution = evolutions[self.pokemon_id]

            if self.level >= evolution["level_required"]:
                new_pokemon_id = evolution["evolves_to"]
                self.pokemon_id = new_pokemon_id

                for pokemon in data["pokemon"]:
                    if pokemon["pokedex_id"] == new_pokemon_id:
                        self.pokemon_name = pokemon["name"]
                        self.pokemon_atk = pokemon["stat"]["atk"]
                        self.pokemon_life = pokemon["stat"]["hp"]
                        self.pokemon_def = pokemon["stat"]["def"]
                        self.pokemon_type = pokemon["type"]
                        self.pokemon_sprite = pygame.image.load(pokemon["sprites"]["back"]).convert_alpha()
                        self.pokemon_sprite = pygame.transform.scale(self.pokemon_sprite, (self.pokemon_sprite.get_width() * 3, self.pokemon_sprite.get_height() * 3))
                        break
    
    def win_battle(self):
        self.gain_xp(5)




# # defs get opponent

#     def get_pokemon_opponent_id(self):

#         available_ids = []
#         for pokemon in data["pokemon"]:
#                 if pokemon["active"] == True:
#                     available_ids.append(pokemon["pokedex_id"])
#         return random.choice(available_ids)

#     def get_pokemon_opponent_sprite(self):

#         for pokemon in data["pokemon"]:
#             if pokemon["pokedex_id"] == self.pokemon_opponent_id:
#                 sprite_path_opponent = pokemon["sprites"]["front"]
#                 self.pokemon_opponent_sprite = pygame.image.load(sprite_path_opponent).convert_alpha()
#                 self.pokemon_opponent_sprite = pygame.transform.scale(self.pokemon_opponent_sprite, (self.pokemon_opponent_sprite.get_width()*3, self.pokemon_opponent_sprite.get_height()*3))
#                 return self.pokemon_opponent_sprite


# defs fight system :

    def attack(self,target, attacker):
        """the player attack the opponent"""
        if random.random() > 0.1:   
            
            resistance_multiplier = target.get_pokemon_resistance(self.pokemon_type)

            raw_damage = max(1,self.pokemon_atk - target.pokemon_def)
            damage = raw_damage * resistance_multiplier

            target.pokemon_life -= damage
            self.draw_damage(damage,target,attacker)
        else:
            damage = 0
            self.draw_damage(damage,target,attacker)


    def draw_damage(self, damage,target, attacker):
        """Display the damage dealt on the screen for a short time"""

        if damage >= 1:
            if attacker == "player" :
                position = ((self.window.screen_width/2)-50, 25)
                damage_text = self.window.text_font_battle.render(
                    f"{target.pokemon_name} : - {damage} HP", 
                    True, self.window.RED)
            else:
                position = ((self.window.screen_width/2), 300)
                damage_text = self.window.text_font_battle.render(
                    f"{target.pokemon_name} : - {damage} HP", 
                    True, self.window.RED)
        else : 
            if attacker == "player":
                position = ((self.window.screen_width/2)-200, 25)
                damage_text = self.window.text_font_battle.render(
                    f"ATTACK MISS | {target.pokemon_name} : - {damage} HP", 
                    True, self.window.RED)
            else:
                position = ((self.window.screen_width/2), 300)
                damage_text = self.window.text_font_battle.render(
                    f"ATTACK MISS | {target.pokemon_name} : - {damage} HP", 
                    True, self.window.RED)

        self.window.screen.blit(damage_text, position)
        pygame.display.update()



    def draw_pokemon_opponent_hp(self,opponent):
        """draw HP to pokemon opponent"""
        self.window.draw_text(f"{opponent.pokemon_name} HP : {opponent.pokemon_life}",
                            self.window.text_font_battle,
                            self.window.WHITE,560,25)
        
    def draw_pokemon_player_hp(self,player):
        """draw HP to pokemon player"""
        self.window.draw_text(f"{player.pokemon_name} HP : {player.pokemon_life}",
                            self.window.text_font_battle,
                            self.window.WHITE,160,200)
        
    def draw_pokemon_xp(self,player):
        """Draw XP pokemon player"""
        self.window.draw_text(f"{player.pokemon_name} XP : {player.pokemon_xp}",
                            self.window.text_font_hp_opponent,
                            self.window.WHITE, 160, 180)



    def draw_pokemon_player(self,player):
        """function to draw pokemon player"""

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"]==player.pokemon_id:
                sprite_path = pokemon["sprites"]["back"]
                self.pokemon_sprite = pygame.image.load(sprite_path).convert_alpha()
                self.pokemon_sprite = pygame.transform.scale(self.pokemon_sprite, (self.pokemon_sprite.get_width()*3, self.pokemon_sprite.get_height()*3))

        # pokemon player
        self.rect_pokemon_sprite = self.pokemon_sprite.get_rect()
        self.rect_pokemon_sprite.center = (250,335)
        self.window.screen.blit(self.pokemon_sprite,self.rect_pokemon_sprite)

    def draw_pokemon_opponent(self,opponent):
        """function to draw pokemon opponent"""

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"]==opponent.pokemon_id:
                sprite_path = pokemon["sprites"]["front"]
                self.pokemon_sprite = pygame.image.load(sprite_path).convert_alpha()
                self.pokemon_sprite = pygame.transform.scale(self.pokemon_sprite, (self.pokemon_sprite.get_width()*3, self.pokemon_sprite.get_height()*3))

        self.rect_pokemon_opponent_sprite = self.pokemon_sprite.get_rect()
        self.rect_pokemon_opponent_sprite.center = (650,160)
        self.window.screen.blit(self.pokemon_sprite,self.rect_pokemon_opponent_sprite)
