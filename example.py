from state.machine import StateMachine
from state import ExampleState1
from state import ExampleState2


class Game:
    def __init__(self):
        self.states = ("state_1", "state_2")

        self.game_state = StateMachine(
            self,
            {
                self.states[0]: ExampleState1,
                self.states[1]: ExampleState2
            }
        )

        self.game_state.change('state_1')

    @staticmethod
    def close():
        exit()

    def print_state_list(self):
        print("*" * 20)
        print("States list:")
        for s in self.states:
            print("--" + s)
        print("*" * 20)

    def run(self):
        print("Welcome!")
        self.print_state_list()
        while True:
            self.update()
            print()
            self.draw()

    def update(self):
        self.game_state.update()

    def draw(self):
        self.game_state.draw()


if __name__ == "__main__":
    g = Game()
    try:
        g.run()
    except KeyboardInterrupt:
        print("\nPress enter to exit..")
        input()
