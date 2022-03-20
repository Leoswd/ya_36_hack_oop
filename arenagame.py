import random


class Thing:

    def __init__(self,
                 name: str,
                 defence: float,
                 attack: float,
                 hitpoints: float
                 ) -> None:
        self.name = name
        self.defence = defence
        self.attack = attack
        self.hitpoints = hitpoints

    def __str__(self):
        return f"{self.name}: {self.defence}, {self.attack}, {self.hitpoints}"


class Person:

    DEFENCE=0.1
    ATTACK=5
    HITPOINTS=20

    def __init__(self,
                 name: str
                 ) -> None:
        self.name = name

    def __str__(self):
        return f"{type(self).__name__} {self.name}: {self.HITPOINTS}, {self.ATTACK}, {self.DEFENCE:.2f}"


    def set_things(self,things):
        for obj in things:
            self.DEFENCE+=obj.defence
            self.ATTACK+=obj.attack
            self.HITPOINTS+=obj.hitpoints
            print(f'{type(self).__name__} {self.name} надел {obj.name}')

    def attack_damage(self, attacker):
        damage = attacker.ATTACK - attacker.ATTACK * self.DEFENCE
        print(f'{attacker.name} наносит удар по {self.name} на {damage:.2f} урона')
        self.HITPOINTS -= damage


class Paladin(Person):
    DEFENCE=0.2
    HITPOINTS=40

    
class Warrior(Person):
    ATTACK=10



def main() -> None:

    #NAMES=[]
    #for i in range(20):
    #    NAMES.append('Soldier_'+str(i+1))
    NAMES=['Arny','Bruce','Jan-Clod','Jacky','Steve','Logan','Peter', 'Kate','Sam', 'Tom',
           'Fred','Mary','Jane','Richard','Arthur','Scott','Pierce','Bill', 'Molly','Dave']

    THING_NAMES = ['MagicRing', 'Sword', 'Shield']

    THINGS = []
    for i in range(40):
        THINGS.append(Thing(THING_NAMES[random.randint(0,len(THING_NAMES)-1)],0.1,1,1))

    SOLDIERS=[]
    for i in range(10):
        pal_war = random.randint(1, 2)
        if pal_war==1:
            SOLDIERS.append(Paladin(NAMES.pop(random.randint(0,len(NAMES)-1))))
        else:
            SOLDIERS.append(Warrior(NAMES.pop(random.randint(0,len(NAMES)-1))))

    print('Initial stats:')
    for s in SOLDIERS:
        print(s)

    print()

    for s in SOLDIERS:
        sol_things = []
        for i in range(random.randint(1, 4)):
            sol_things.append(THINGS.pop(random.randint(0, len(THINGS)-1)))
        s.set_things(sol_things)

    print()

    print('Stats after setting things:')
    for s in SOLDIERS:
        print(s)
    
    print()
    
    while len(SOLDIERS)>1:
        attacker, defender = random.sample(SOLDIERS, 2)
        defender.attack_damage(attacker)
        if defender.HITPOINTS<=0:
            print(f'{defender.name} погибает')
            SOLDIERS.remove(defender)

    print()

    print(f'Побеждает {SOLDIERS[0].name}!')


if __name__ == '__main__':
    main()
