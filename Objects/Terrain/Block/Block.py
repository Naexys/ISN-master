from Class.Terrain.Block import Block
from Assets.load_textures import *
from intValues import *

floor = 430

if MAP == 1:
    #   Parallaxe first
    Mountain = Block(2000, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
                     _is_trav_top=True, _is_trav_bottom=True, _is_no_collision=True, _texture=mountain,
                     _resize=(True, 200), _parallaxe=(True, 4))
    Mountain2 = Block(800, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
                      _is_trav_top=True, _is_trav_bottom=True, _is_no_collision=True, _texture=mountain,
                      _resize=(True, 200), _parallaxe=(True, 3))
    Mountain = Block(1200, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
                     _is_trav_top=True, _is_trav_bottom=True, _is_no_collision=True, _texture=mountain,
                     _resize=(True, 200), _parallaxe=(True, 2))

    Tree = Block(1200, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
                 _is_trav_top=True, _is_trav_bottom=True, _is_no_collision=True, _texture=tree, _resize=(True, 200),
                 _parallaxe=(True, 1.5))

    Tree2 = Block(1350, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
                  _is_trav_top=True, _is_trav_bottom=True, _is_no_collision=True, _texture=tree2, _resize=(True, 200),
                  _parallaxe=(True, 1.8))

    Tree3 = Block(2000, 235, 80, 30, _is_trav_right=True, _is_trav_left=True,
                  _is_trav_top=True, _is_trav_bottom=True, _is_no_collision=True, _texture=tree3, _resize=(True, 200),
                  _parallaxe=(True, 1.2))

    #   Then the map
    lockMap = Block(500, 0, 0, 0, _is_no_collision=True, _texture=fond)

    #   Then the object in the map
    BlockFloor = Block(500, 430, 2260, 50, _texture=nothing)
    BlockFloor2 = Block(2890, 430, 2280, 50, _texture=nothing)
    BlockFloor2 = Block(5275, 430, 2280, 50, _texture=nothing)

    # BlockFloor3 = Block(2890, 450, 2280, 50, _texture=blank, _no_texture=True)

    BlockBridge = Block(855, 360, 270, 200, _texture=nothing)

    BlockStairs = Block(1900, 360, 560, 200, _texture=nothing)
    BlockStairs2 = Block(3880, 360, 460, 150, _texture=nothing)
    BlockStairs3 = Block(4310, 290, 560, 150, _texture=nothing)

    BlockNoTop1 = Block(2015, 200, 80, 50, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop2 = Block(2095, 300, 65, 50, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop3 = Block(2160, 250, 80, 50, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop4 = Block(2240, 295, 40, 50, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop5 = Block(1705, 105, 80, 30, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop6 = Block(2600, 365, 80, 30, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop7 = Block(2680, 325, 80, 30, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
    BlockNoTop8 = Block(2540, 410, 80, 30, _is_trav_right=True, _is_trav_left=True,
                        _is_trav_top=False, _is_trav_bottom=True, _texture=nothing)
elif MAP == 2:

    #   Then the map
    lockMap = Block(500, -2500, 0, 0, _is_no_collision=True, _texture=fond2)

    #   Then the object in the map
    BlocWall = Block(450, -4500, 50, 5000, _texture=nothing)
    BlocWall2 = Block(980, -4500, 50, 5000, _texture=nothing)

    BlockFloor = Block(480, 480, 500, 50, _texture=nothing)

    BlockFloor2 = Block(620, 60, 500, 50, _texture=nothing)
    BlockFloor3 = Block(920, 5, 500, 100, _texture=nothing)

    BlockFloor4 = Block(700, -765, 500, 50, _texture=nothing)
    BlockFloor5 = Block(330, -300, 500, 50, _texture=nothing)

    BlockFloor6 = Block(620, -1400, 500, 50, _texture=nothing)
    BlockFloor7 = Block(920, -1455, 500, 100, _texture=nothing)

    BlockFloor8 = Block(450, -970, 600, 40, _texture=nothing)
    BlockFloor9 = Block(450, -2120, 600, 40, _texture=nothing)
