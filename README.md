# State-Machine
This is python state pattern implementation for games or other things
# How to use
1. Clone repository `https://github.com/GitRenhl/State-Machine.git`
1. Copy `state` folder to your project directory
1. Import and code:
1. Done
### Example:
```py
import state as StateManagment


class Game:
    def __init__(self):
        self.states = ("state_1", "state_2")

        state_dict = {
            self.states[0]: StateManagment.ExampleState1,
            self.states[1]: StateManagment.ExampleState2
        }
        self.game_state = StateManagment.StateMachine(self, state_dict)

        self.game_state.change('state_1')

    def update(self):
        self.game_state.update()
```
