from Trengine.Game.Spritesheet import SpriteSheet

class TileMap:
    # takes a file path, that loads a TileDict & a 2d array of tiles
    def __init__(self, file) -> None:
        self.file = file
        self.tile_dict = None
        self.map = None

        self.load_map()

        pass

    def load_map(self):
        with open(self.file, "r") as f:
            # the first line is the directory of the tile dict
            tile_dict_dir = f.readline().strip()
            self.tile_dict = TileDict(tile_dict_dir)

            # the next line is the map size
            map_size = f.readline().strip().split(",")
            map_width = int(map_size[0])
            map_height = int(map_size[1])

            # now we need to create the map
            self.map = [[0 for x in range(map_width)]
                        for y in range(map_height)]
            '''
                now we need to load the tiles, the format is:
                tile_name, [flags], there is no x or y because the map is a 2d array
                [
                    [tile_name, [flags], tile_name, [flags], tile_name, [flags]],
                    [tile_name, [flags], tile_name, [flags], tile_name, [flags]],
                ]
             '''

            # the first line should be a [  this is the start of the map
            # the last line should be a ]  this is the end of the map
            # if the first line is not just a [ then we have a problem
            if line[0] != "[":
                raise Exception("TileMap file is not formatted correctly")
            for line in f:
                # the line should be a list of tiles in the format:
                # [[tile_name, [flag 1, flag 2], tile_name, [flag 1, flag 2], tile_name, [flag 1, flag 2]]

                # remove the [ and ] from the line
                line = line[1:-1]
                # we can not just split by the comma because the flags are in a list
                # so we need to split by the comma but only if it's not in a list
                # by counting the number of [ and ] we can tell if we are in a list or not because the amount will be even if we are not in a list & odd if we are

                tile_name = ""
                tile_flags = []

                # we need to keep track of the number of [ and ] so we know if we are in a list or not
                list_count = 0
                for char in line:
                    if char == "[":
                        list_count += 1
                    elif char == "]":
                        list_count -= 1
                    elif char == "," and list_count % 2 == 0:
                        # we are not in a list so we can split by the comma
                        # we need to add the tile to the map
                        self.map.append(self.tile_dict.get_tile(
                            tile_name, tile_flags))
                        # now we need to reset the tile_name and tile_flags
                        tile_name = ""
                        tile_flags = []
                    else:
                        # we are in a list or not in a list
                        if list_count % 2 == 0:
                            # we are not in a list
                            tile_name += char
                        else:
                            # we are in a list
                            tile_flags += char

                pass

            pass

            print(self.map)
        pass

    pass


class TileDict:
    def __init__(self, file) -> None:
        self.file = file
        self.tiles = []

        self.load_tiles()

        pass

    def load_tiles(self):
        with open(self.file, "r") as f:
            # the first line is the directory of the sprite sheet
            # the 2nd line is the sprite sheet info
            # from than on it's the tiles
            # the format is:
            # tile_name, x, y, [flags]

            # load the sprite sheet
            sprite_sheet_dir = f.readline().strip()
            sprite_sheet_info = f.readline().strip().split(",")
            sprite_sheet = SpriteSheet(sprite_sheet_dir, int(
                sprite_sheet_info[0]), int(sprite_sheet_info[1]))

            for line in f:
                # in file example: tile_name,x,y,[flag 1,flag 2flag 3...]

                # get the stuff in the [ ] first
                tile_flags = line[line.find("[") + 1:line.find("]")]
                print(tile_flags)
                # split the flags by the comma
                tile_flags = tile_flags.split(",")
                print(tile_flags)

                # now we need to get the tile name, x, and y
                tile_info = line[:line.find("[")].strip().split(",")
                # clear any empty strings
                tile_info = list(filter(None, tile_info))

                tile_name = tile_info[0]
                tile_x = int(tile_info[1])
                tile_y = int(tile_info[2])
                tile_sprite = sprite_sheet.get_tile(tile_x, tile_y)

                # now we create the tile
                self.tiles.append(Tile(tile_name, tile_sprite, tile_flags))

            pass

            print(self.tiles)
        pass


class Tile:
    def __init__(self, name, surface, flags) -> None:
        self.name = name
        self.surface = surface
        self.flags = flags
        pass
