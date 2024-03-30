class Animal:
    alive = []

    def __init__(
            self,
            name: str,
            health: int = 100,
            hidden: bool = False
    ) -> None:
        self.name = name
        self.health = health
        self.hidden = hidden
        self.alive.append(self)

    def die(self) -> None:
        Animal.alive.remove(self)

    def __repr__(self) -> str:
        result = (f"{{Name: {self.name}, "
                  f"Health: {self.health}, "
                  f"Hidden: {self.hidden}}}")
        return f"{result}"


class Herbivore(Animal):
    def hide(self) -> None:
        self.hidden = not self.hidden


class Carnivore(Animal):
    @classmethod
    def bite(cls, victim: Animal) -> None:
        if not victim.hidden and victim.__class__ == Herbivore:
            victim.health -= 50
        if victim.health <= 0:
            Animal.alive.remove(victim)
