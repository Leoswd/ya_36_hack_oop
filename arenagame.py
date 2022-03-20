import random
from colorama import Fore
from typing import List, Type


class Thing:
    """Базовый класс экипировки."""

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

    def __str__(self) -> str:
        return (f'{self.name}({self.defence:.3f}, '
                f'{self.attack}, {self.hitpoints})')


class Person:
    """Базовый класс персонажа."""

    DEFENCE: float = 0.1
    ATTACK: float = 5
    HITPOINTS: float = 20

    def __init__(self,
                 name: str
                 ) -> None:
        self.name = name

    def __str__(self) -> str:
        return (f'{type(self).__name__} {self.name}: '
                f'{self.HITPOINTS}, {self.ATTACK}, {self.DEFENCE:.3f}')

    def set_things(self, things) -> None:
        """Надеть предметы экипировки."""
        self.things: List[Type[Thing]] = things
        print(f'{type(self).__name__} {self.name} надевает:')
        for obj in things:
            print(obj)
            self.DEFENCE += obj.defence
            self.ATTACK += obj.attack
            self.HITPOINTS += obj.hitpoints
        print()

    def attack_person(self, attacker) -> None:
        """Атака противника."""
        damage: float = attacker.ATTACK - attacker.ATTACK * self.DEFENCE
        print(Fore.YELLOW + f'{attacker.name} наносит удар по {self.name} '
              f'на {damage:.3f} урона')
        self.HITPOINTS -= damage


class Paladin(Person):
    """Персонаж: паладин."""

    DEFENCE = 2 * Person.DEFENCE
    HITPOINTS = 2 * Person.HITPOINTS


class Warrior(Person):
    """Персонаж: воин."""

    ATTACK = 2 * Person.ATTACK


class Elf(Person):
    """Персонаж: эльф."""

    DEFENCE = 2 * Person.DEFENCE
    ATTACK = 2 * Person.ATTACK


def main() -> None:
    """Главная функция."""
    NUM_FIGHTERS: int = 10

    FIGHTER_TYPES: List[Type[Person]] = [Paladin, Warrior, Elf]

    NAMES: List[str] = ['Arny', 'Bruce', 'JanClod', 'Jackie', 'Steve',
                        'Logan', 'Peter', 'Karl', 'Sam', 'Tom',
                        'Fred', 'Matt', 'John', 'Richard', 'Arthur',
                        'Scott', 'Pierce', 'Bill', 'Mike', 'Dave']

    THING_TYPES: List[str] = ['MagicRing', 'MagicStaff', 'Sword', 'Shield',
                              'Jacket', 'Boots', 'Helmet', 'Bow']

    THINGS = []
    for i in range(random.randint(NUM_FIGHTERS * 4, NUM_FIGHTERS * 10)):
        THINGS.append(Thing(THING_TYPES[random.randint(0, len(THING_TYPES)-1)],
                      random.randint(0, 100)/1000, random.randint(0, 5),
                      random.randint(0, 20)))
    THINGS.sort(key=lambda x: x.defence)

    FIGHTERS = []
    for i in range(NUM_FIGHTERS):
        FIGHTERS.append(random.choice(FIGHTER_TYPES)(NAMES.pop(
                             random.randint(0, len(NAMES)-1))))

    print('Initial stats:')
    for fighter in FIGHTERS:
        print(fighter)

    print()

    # 'Setting things'
    for fighter in FIGHTERS:
        fighter_things = []
        for i in range(random.randint(1, 4)):
            fighter_things.append(THINGS.pop(random.randint(0, len(THINGS)-1)))
        fighter.set_things(fighter_things)

    print()
    print('Stats after setting things:')
    for fighter in FIGHTERS:
        print(fighter)

    print()
    print(Fore.RED + 'БОЙ НАЧИНАЕТСЯ!')
    while len(FIGHTERS) > 1:
        attacker, defender = random.sample(FIGHTERS, 2)
        defender.attack_person(attacker)
        if defender.HITPOINTS <= 0:
            print(Fore.RED + f'{defender.name} погибает')
            FIGHTERS.remove(defender)

    print()
    print(Fore.GREEN + f'Побеждает {FIGHTERS[0].name}!'.upper() + Fore.RESET)


if __name__ == '__main__':
    main()
