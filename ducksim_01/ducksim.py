from typing import Callable
from duck import *


class DuckSimulatorController:
    _duck: Duck
    _actions: dict[str, Callable]

    def __init__(self):
        choose_duck: str = self._ask_user_which_duck_create()
        self._create_duck(choose_duck)
        self._actions = self._init_actions()

    def execute_command(self, action_name: str) -> bool:
        action_name = action_name.lstrip().rstrip()
        if not action_name:
            return False

        if not self._is_action_exist(action_name):
            print(f'Invalid action {action_name}. Enter Possible action')
            return True

        action = self._actions[action_name]
        print(action())
        return True

    def _ask_user_which_duck_create(self) -> str:
        text = f""" 
        In that program you can choose one of the types of ducks:
        {self._ducks_to_str()}
        """
        print(text)
        while True:
            user_input = input('What kind of duck will we be today?').lstrip().rstrip()
            if not self._is_duck_exist(user_input):
                print(f'Invalid duck {user_input}. Try correct duck type.')
                print(f'Enter one of the duck type: {self._ducks_to_str()}')
            else:
                break
        return user_input

    def _create_duck(self, duck_name: str) -> None:
        if not self._is_duck_exist(duck_name):
            print(f'Duck "{duck_name}" not found. Enter valid type of duck')
            return

        self._duck = self._get_duck_types()[duck_name]()
        print(f'Duck {duck_name} successfully created')

    def _is_duck_exist(self, name: str) -> bool:
        if name in self._get_duck_types().keys():
            return True
        return False

    def _is_action_exist(self, action: str) -> bool:
        if action in self._actions.keys():
            return True
        return False

    def _init_actions(self) -> dict[str, Callable]:
        actions: dict[str, Callable] = {
            'fly': self._duck.perform_fly,
            'swim': self._duck.swim,
            'dance': self._duck.perform_dance,
            'quack': self._duck.perform_quack,
            'info': self._duck.display,
        }
        return actions

    def _ducks_to_str(self) -> str:
        return ' '.join([name for name in self._get_duck_types().keys()])

    @staticmethod
    def _get_duck_types() -> dict[str, Callable]:
        ducks: dict[str, Callable] = {
            'mallard': MallardDuck,
            'readhead': ReadHeadDuck,
            'decoy': DecoyDuck,
            'rubber': RubberDuck
        }
        return ducks


def main():
    duck_simulator = DuckSimulatorController()
    while True:
        cmd: str = input('\nEnter a command: ')
        if not duck_simulator.execute_command(cmd):
            break


if __name__ == '__main__':
    main()
