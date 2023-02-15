from Trengine.Game.TreeGame import TreeGame

from game.MainMenu import MainMenu
from game.PlayScene import PlayScene

def main():
    game = TreeGame()

    game.scenes = [
        MainMenu(game, "main_scene"),
        PlayScene(game, "game_scene")
        ]

    game.current_scene = game.scenes[0]

    game.run()

    pass


if __name__ == "__main__":
    main()
