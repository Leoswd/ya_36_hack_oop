import random
from colorama import init
init()
from colorama import Fore


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
        return (f'{self.name}({self.defence:.3f}, '
                f'{self.attack}, {self.hitpoints})')


class Person:

    DEFENCE = 0.1
    ATTACK = 5
    HITPOINTS = 20

    def __init__(self,
                 name: str
                 ) -> None:
        self.name = name

    def __str__(self):
        return (f'{type(self).__name__} {self.name}: '
                f'{self.HITPOINTS}, {self.ATTACK}, {self.DEFENCE:.3f}')

    def set_things(self, things):
        self.things = things
        print(f'{type(self).__name__} {self.name} надевает:')
        for obj in things:
            print(obj)
            self.DEFENCE += obj.defence
            self.ATTACK += obj.attack
            self.HITPOINTS += obj.hitpoints
        print()

    def attack_damage(self, attacker):
        damage = attacker.ATTACK - attacker.ATTACK * self.DEFENCE
        print(Fore.YELLOW + f'{attacker.name} наносит удар по {self.name} '
              f'на {damage:.3f} урона')
        self.HITPOINTS -= damage


class Paladin(Person):
    DEFENCE = 2 * Person.DEFENCE
    HITPOINTS = 2 * Person.HITPOINTS


class Warrior(Person):
    ATTACK = 2 * Person.ATTACK


class Elf(Person):
    DEFENCE = 2 * Person.DEFENCE
    ATTACK = 2 * Person.ATTACK


def main() -> None:

    SOLDIER_TYPES = [Paladin, Warrior, Elf]

    NAMES = ['Arny', 'Bruce', 'JanClod', 'Jackie', 'Steve', 'Logan',
             'Peter', 'Kate', 'Sam', 'Tom', 'Fred', 'Mary', 'Jane',
             'Richard', 'Arthur', 'Scott', 'Pierce', 'Bill', 'Molly', 'Dave']

    THING_TYPES = ['MagicRing', 'MagicStaff', 'Sword', 'Shield',
                   'Jacket', 'Boots', 'Helmet', 'Bow']

    THINGS = []
    for i in range(random.randint(40, 100)):
        THINGS.append(Thing(THING_TYPES[random.randint(0, len(THING_TYPES)-1)],
                      random.randint(0, 100)/1000, random.randint(0, 5),
                      random.randint(0, 20)))
    # THINGS.sort()

    SOLDIERS = []
    for i in range(10):
        SOLDIERS.append(random.choice(SOLDIER_TYPES)(NAMES.pop(
                             random.randint(0, len(NAMES)-1))))

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

    print(Fore.RED + 'БОЙ НАЧИНАЕТСЯ!')
    while len(SOLDIERS) > 1:
        attacker, defender = random.sample(SOLDIERS, 2)
        defender.attack_damage(attacker)
        if defender.HITPOINTS <= 0:
            print(Fore.RED + f'{defender.name} погибает')
            SOLDIERS.remove(defender)

    print()

    print(Fore.GREEN + f'Побеждает {SOLDIERS[0].name}!'.upper())


if __name__ == '__main__':
    main()
