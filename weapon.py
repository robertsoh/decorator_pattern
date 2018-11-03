from abc import ABC, abstractmethod


class Weapon(ABC):

    @abstractmethod
    def aim_and_fire(self):
        pass


class BaseWeapon(Weapon):

    def aim_and_fire(self):
        print("Apuntar y disparar")


class WeaponDecorator(Weapon):

    def __init__(self, weapon):
        self._weapon = weapon

    @abstractmethod
    def aim_and_fire(self):
        pass


class WeaponAccesoryMuffler(WeaponDecorator):

    def add_muffler(self):
        print("Agrega silenciador al arma")

    def aim_and_fire(self):
        self.add_muffler()
        self._weapon.aim_and_fire()


class WeaponAccesoryLigths(WeaponDecorator):

    def add_ligths(self):
        print("Agrega linterna al arma")

    def aim_and_fire(self):
        self.add_ligths()
        self._weapon.aim_and_fire()


def main():
    base_weapon = BaseWeapon()
    weapon_accesory_muffler = WeaponAccesoryMuffler(base_weapon)
    weapon_accesory_ligths = WeaponAccesoryLigths(weapon_accesory_muffler)
    weapon_accesory_ligths.aim_and_fire()


if __name__ == "__main__":
    main()
