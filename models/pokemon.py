from models.window import Window
import pygame
import json
import random

with open("models/pokemon.json", "r", encoding = "utf-8") as file:
    data = json.load(file)


class Pokemon():
    """class to init pokemon, caract and draw"""

    def __init__(self):
        # background image
        self.window = Window()
        # pokemon 
        self.pokemon_player = ""
        self.pokemon_player_id = 1
        self.pokemon_player_sprite = self.get_pokemon_player_sprite()

        self.pokemon_player_life = self.get_pokemon_player_hp()
        self.pokemon_player_name = self.get_pokemon_player_name()
        self.pokemon_player_type = self.get_pokemon_player_type()
        self.pokemon_player_def = self.get_pokemon_player_defense()
        self.pokemon_player_resistance = self.get_pokemon_player_resistance()
        self.pokemon_player_atk = self.get_pokemon_player_attack()


        # pokemon opponent
        self.pokemon_opponent = ""
        self.pokemon_opponent_id = self.get_pokemon_opponent_id()
        self.pokemon_opponent_sprite = self.get_pokemon_opponent_sprite()

        self.pokemon_opponent_life = self.get_pokemon_opponent_hp()
        self.pokemon_opponent_name = self.get_pokemon_opponent_name()
        self.pokemon_opponent_type = self.get_pokemon_opponent_type()
        self.pokemon_opponent_def = self.get_pokemon_opponent_defense()
        self.pokemon_opponent_resistance = self.get_pokemon_opponent_resistance()
        self.pokemon_opponent_atk = self.get_pokemon_opponent_attack()


        self.damage = ""
        self.target = ""


        self.pokemon_availability_sprite_list = self.get_pokemon_availability_sprite_list()


    def get_pokemon_availability_sprite_list(self):
        self.pokemon_availability_sprite_list = []
        for pokemon in data["pokemon"]:
                pokemon_sprite = pokemon["sprites"]["front"]
                pokemon_sprite_img = pygame.image.load(pokemon_sprite).convert_alpha()
                if pokemon["active"] == False:
                    pokemon_sprite_img.set_alpha(128)
                    self.pokemon_availability_sprite_list.append(pokemon_sprite_img)
                else:
                    self.pokemon_availability_sprite_list.append(pokemon_sprite_img)
        return self.pokemon_availability_sprite_list





        # Mettre à jour la donnée "active" en fonction de l'attaque
        for pokemon in data:
            if pokemon["stat"]["atk"] < 53:
                pokemon["active"] = True
            else:
                pokemon["active"] = False

        # Sauvegarder les modifications dans le fichier JSON
        with open("pokemon.json", "w", encoding="utf-8") as file:
            json.dump(data, file, ensure_ascii=False, indent=4)

        print("Fichier JSON mis à jour avec succès !")





# defs get players

    def get_pokemon_player_sprite(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"]==self.pokemon_player_id:
                sprite_path = pokemon["sprites"]["back"]
                self.pokemon_player_sprite = pygame.image.load(sprite_path).convert_alpha()
                self.pokemon_player_sprite = pygame.transform.scale(self.pokemon_player_sprite, (self.pokemon_player_sprite.get_width()*3, self.pokemon_player_sprite.get_height()*3))
                return self.pokemon_player_sprite


    def get_pokemon_player_attack(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["atk"]

    def get_pokemon_player_name(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["name"]

    def get_pokemon_player_hp(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["hp"]

    def get_pokemon_player_defense(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["stat"]["def"]
            
    def get_pokemon_player_type(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                return pokemon["type"]

    def get_pokemon_player_resistance(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_player_id:
                for resistance in pokemon["resistances"]:
                    if resistance["name"] == self.pokemon_player_type:
                        return resistance["multiply"]





# defs get opponent

    def get_pokemon_opponent_id(self):

        available_ids = []
        for pokemon in data["pokemon"]:
                if pokemon["active"] == True:
                    available_ids.append(pokemon["pokedex_id"])
        return random.choice(available_ids)

    def get_pokemon_opponent_sprite(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                sprite_path_opponent = pokemon["sprites"]["front"]
                self.pokemon_opponent_sprite = pygame.image.load(sprite_path_opponent).convert_alpha()
                self.pokemon_opponent_sprite = pygame.transform.scale(self.pokemon_opponent_sprite, (self.pokemon_opponent_sprite.get_width()*3, self.pokemon_opponent_sprite.get_height()*3))
                return self.pokemon_opponent_sprite

    def get_pokemon_opponent_name(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["name"]

    def get_pokemon_opponent_hp(self):

        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["hp"]

    def get_pokemon_opponent_defense(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["def"]
            
    def get_pokemon_opponent_type(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["type"]

    def get_pokemon_opponent_resistance(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                for resistance in pokemon["resistances"]:
                    if resistance["name"] == self.pokemon_opponent_type:
                        return resistance["multiply"]



    def get_pokemon_opponent_attack(self):
        for pokemon in data["pokemon"]:
            if pokemon["pokedex_id"] == self.pokemon_opponent_id:
                return pokemon["stat"]["atk"]


# defs fight system :

    def player_attack(self):
        """the player attack the opponent"""
        if random.random() > 0.1:   
            resistance_multiplier = self.pokemon_opponent_resistance
            raw_damage = max(1,self.pokemon_player_atk - self.pokemon_opponent_def)
            damage = raw_damage * resistance_multiplier

            self.pokemon_opponent_life -= damage
            self.draw_damage(damage,self.pokemon_opponent_name)
        else:
            damage = 0
            self.draw_damage(damage,self.pokemon_opponent_name)


    def opponent_attack(self):
        """the opponent attack the player"""
        if random.random() > 0.1:   
            resistance_multiplier = self.pokemon_player_resistance
            raw_damage = max(1,self.pokemon_opponent_atk - self.pokemon_player_def)
            damage = raw_damage * resistance_multiplier
            print(resistance_multiplier)
            self.pokemon_player_life -= damage
            self.draw_damage(damage,self.pokemon_player_name)
        else:
            damage = 0
            self.draw_damage(damage,self.pokemon_player_name)


    def draw_damage(self, damage, target):
        """Display the damage dealt on the screen for a short time"""

        if damage >= 1:
            if target == self.pokemon_opponent_name:
                position = ((self.window.screen_width/2)-50, 25)
                damage_text = self.window.text_font_battle.render(
                    f"{self.pokemon_opponent_name} : - {damage} HP", 
                    True, self.window.RED)
            else:
                position = ((self.window.screen_width/2), 300)
                damage_text = self.window.text_font_battle.render(
                    f"{self.pokemon_player_name} : - {damage} HP", 
                    True, self.window.RED)
        else : 
            if target == self.pokemon_opponent_name:
                position = ((self.window.screen_width/2)-200, 25)
                damage_text = self.window.text_font_battle.render(
                    f"ATTACK MISS | {self.pokemon_opponent_name} : - {damage} HP", 
                    True, self.window.RED)
            else:
                position = ((self.window.screen_width/2), 300)
                damage_text = self.window.text_font_battle.render(
                    f"ATTACK MISS | {self.pokemon_player_name} : - {damage} HP", 
                    True, self.window.RED)

        self.window.screen.blit(damage_text, position)
        pygame.display.update()



    def draw_pokemon_opponent_hp(self):
        """draw HP to pokemon opponent"""
        self.window.draw_text(f"{self.pokemon_opponent_name} HP : {self.pokemon_opponent_life}",
                            self.window.text_font_battle,
                            self.window.WHITE,560,25)
        
    def draw_pokemon_player_hp(self):
        """draw HP to pokemon player"""
        self.window.draw_text(f"{self.pokemon_player_name} HP : {self.pokemon_player_life}",
                            self.window.text_font_battle,
                            self.window.WHITE,160,200)



    def draw_pokemon_player(self):
        """function to draw pokemon player"""

        # pokemon player
        self.rect_pokemon_player_sprite = self.pokemon_player_sprite.get_rect()
        self.rect_pokemon_player_sprite.center = (250,335)
        self.window.screen.blit(self.pokemon_player_sprite,self.rect_pokemon_player_sprite)

    def draw_pokemon_opponent(self):
        """function to draw pokemon opponent"""

        self.rect_pokemon_opponent_sprite = self.pokemon_opponent_sprite.get_rect()
        self.rect_pokemon_opponent_sprite.center = (650,160)
        self.window.screen.blit(self.pokemon_opponent_sprite,self.rect_pokemon_opponent_sprite)

    # def draw_life_pokemon(self):
