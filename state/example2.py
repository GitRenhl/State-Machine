from . import BaseState


class ExampleState2(BaseState):
    def __init__(self, game):
        super().__init__(game)
        print("Example State 2 Init")
        self.value = ""

    def update(self):
        value = input(">").strip()
        if not value:
            return
        self.value = value

        if not (self.value == "state_2") and self.value in self._game.states:
            self._game.game_state.change(self.value)

    def draw(self):
        if self.value == "state_2":
            print("This is State 2 state")

        self._game.print_state_list()

    def enter(self, secret=False):
        print("state_2 Enter")

    def exit(self):
        print("state_2 Exit")
