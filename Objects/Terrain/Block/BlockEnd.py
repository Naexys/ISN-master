from Class.Terrain.BlockEnd import BlockEnd
from Assets.load_textures import *
from Functions.update_game import *

if MAP == 1:
    BlockEnd = BlockEnd(6000, 200, 100, 100, _texture=nothing, _no_texture=True)
