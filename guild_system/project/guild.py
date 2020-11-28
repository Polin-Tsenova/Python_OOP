# from excersises.guild_system.project.player import Player

class Guild:
    def __init__(self, name):
        self.name = name
        self.players_list = []

    def assign_player(self, player):
        if self.name == player.guild:
            return f"Player {player.name} is already in the guild."
        elif not player.guild == "Unaffiliated" and not player.guild == self.name:
            return f"Player {player.name} is in another guild."
        else:
            self.players_list.append(player)
            player.guild = self.name
            return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name):
        play_list = [p for p in self.players_list if p.name == player_name]
        if play_list:
            player = play_list[0]
            self.players_list.remove(player)
            player.guild = self.name
            return f"Player {player_name} has been removed from the guild."
        else:
            return f"Player {player_name} is not in the guild."

    def guild_info(self):
        result = f"Guild: {self.name}\n"
        for p in self.players_list:
            result += f"{p.player_info()}"
        return result


# player = Player("George", 50, 100)
# print(player.add_skill("Shield Break", 20))
# print(player.player_info())
# guild = Guild("UGT")
# print(guild.assign_player(player))
# print(guild.guild_info())

