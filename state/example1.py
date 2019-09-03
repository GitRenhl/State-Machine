from . import BaseState


class ExampleState1(BaseState):
    def __init__(self, game):
        super().__init__(game)
        print("Example State 1 Init")
        self.value = ""

    def update(self):
        value = input(">").strip()
        if not value:
            return
        self.value = value

        if not (self.value == "state_1") and self.value in self._game.states:
            self._game.game_state.change(self.value)

    def draw(self):
        if self.value == "state_1":
            print("This is State 1 state")

        self._game.print_state_list()

    def enter(self, secret=False):
        print("state_1 Enter")

    def exit(self):
        print("state_1 Exit")
