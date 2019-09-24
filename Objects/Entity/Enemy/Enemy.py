from Class.Entity.Enemy.Enemy import *
from Assets.load_textures import *
from intValues import *

if MAP  == 1:
    EnemyThrow1 = Enemy(1200, 300, 100, 100, tikiWalkLeftThrow, tikiWalkRightThrow, (True, 400), _health=100, _gender="/Tiki/Throw")
    EnemyThrow2 = Enemy(3000, 300, 100, 100, tikiWalkLeftThrow, tikiWalkRightThrow, (True, 400), _health=100, _gender="/Tiki/Throw")
    EnemyThrow3 = Enemy(5600, 300, 100, 100, tikiWalkLeftThrow, tikiWalkRightThrow, (True, 400), _health=100, _gender="/Tiki/Throw")


    EnemyRush1 = Enemy(1900, 230, 100, 100, tikiWalkLeftRush, tikiWalkRightRush, (True, 200), _health=100, _gender="/Tiki/Rush")
    EnemyRush2 = Enemy(2900, 300, 100, 100, tikiWalkLeftRush, tikiWalkRightRush, (True, 200), _health=100, _gender="/Tiki/Rush")
