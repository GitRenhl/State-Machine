# State-Machine
This is python state pattern implementation for games or other things
# How to use
1. Clone repository `https://github.com/GitRenhl/State-Machine.git`
1. Copy `state` folder to your project directory
1. Import and code:
1. Done
### Example:
```py
from state.machine import StateMachine
from state import ExampleState1
from state import ExampleState2


class Game:
    def __init__(self):
        self.states = ("state_1", "state_2")

        state_dict = {
            self.states[0]: ExampleState1,
            self.states[1]: ExampleState2
        }
        self.game_state = StateMachine(self, state_dict)

        self.game_state.change('state_1')

    def update(self):
        self.game_state.update()
```
