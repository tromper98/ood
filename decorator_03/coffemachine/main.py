from typing import Dict, Type, Optional
from dataclasses import dataclass

from impl import *


@dataclass()
class CoffeeTypes:
    description: str
    cls: Type[Coffee]


class CoffeeMachine:
    _beverages: Dict[str, BeverageInterface]
    _selected_beverage: BeverageInterface

    def main(self):
        user_choice: str = self._select_beverage()

        if user_choice == 'Coffee':
            coffee: Type[Coffee] = self._select_coffee()
            portion: CoffeePortion = self._select_coffee_portion()
            self._selected_beverage = coffee(portion)
            self._select_condiments()

        elif user_choice == 'Tea':
            tea_type: TeaType = self._select_tea()
            self._selected_beverage = Tea(tea_type)
            self._select_condiments()

        else:
            milkshake_portion = self._select_milkshake()
            self._selected_beverage = Milkshake(milkshake_portion)
            pass

        print('Beverage: ', self._selected_beverage.get_description())
        print('Cost: ', self._selected_beverage.get_cost())

    def _select_beverage(self) -> str:
        beverages = self._get_beverages()
        while True:
            print('Select beverage')
            for i, name in beverages.items():
                print(f'{i}: {name}')

            user_input = input('Enter drink number: ').lstrip().rstrip()
            if user_input not in str(beverages.keys()):
                print('Invalid choice')
            else:
                break

        return beverages[int(user_input)]

    def _select_coffee(self) -> Type[Coffee]:
        coffee_types: Dict[int, CoffeeTypes] = self._get_coffee_types()
        while True:
            print('Select Coffee:')
            for num, coffee_type in coffee_types.items():
                print(f'{num}: {coffee_type.description}')

            user_input = input('Enter coffee number: ').lstrip().rstrip()

            if not user_input.isdigit() or int(user_input) not in coffee_types.keys():
                print('Invalid choice')

            else:
                return coffee_types[int(user_input)].cls

    def _select_coffee_portion(self) -> CoffeePortion:
        while True:
            print('Choice portion:')
            print(f'1: {CoffeePortion.SINGLE.value}')
            print(f'2: {CoffeePortion.DOUBLE.value}')

            user_input = input('Enter portion: ').lstrip().rstrip()
            if user_input not in ('1', '2'):
                print('Invalid choice')
            else:
                if user_input == '1':
                    return CoffeePortion.SINGLE
                else:
                    return CoffeePortion.DOUBLE

    def _select_tea(self) -> TeaType:
        tea_types = self._get_tea_types()
        while True:
            print('Select Tea Type')
            for num, tea_type in tea_types.items():
                print(f'{num}: {tea_type.value}')

            user_input = input('Enter type: ').lstrip().rstrip()
            if not user_input.isdigit() or int(user_input) not in tea_types.keys():
                print('Invalid Choice')
            else:
                return tea_types[int(user_input)]

    def _select_milkshake(self) -> MilkshakePortion:
        milkshake_portions = self._get_milkshake_portions()
        print('Select Milkshake Portion')
        for num, portion in milkshake_portions.items():
            print(f'{num}: {portion.value}')

        user_input = input('Enter portion').lstrip().rstrip()
        if not user_input.isdigit() or int(user_input) not in milkshake_portions.keys():
            print('Invalid Choice')
        else:
            return milkshake_portions[int(user_input)]

    def _select_condiments(self) -> None:
        if self._ask_add_cinnamon():
            self._selected_beverage = Cinnamon(self._selected_beverage)

        lemon: int = self._ask_add_lemon()
        if lemon:
            self._selected_beverage = Lemon(self._selected_beverage, lemon)

    @staticmethod
    def _ask_add_cinnamon() -> bool:
        while True:
            print('Add Cinnamon? 1 - Yes, 0 - No')
            user_input = input().lstrip().rstrip()
            if user_input not in ('0', '1'):
                print('Invalid Choice')
            else:
                return bool(int(user_input))

    @staticmethod
    def _ask_add_lemon() -> int:
        while True:
            print('How many Lemon slice add?')
            user_input = input().lstrip().rstrip()
            if not user_input.isdigit() or int(user_input) not in (0, 1, 2):
                print('Must be a number in [0, 2]')
            else:
                break

        return int(user_input)

    def _ask_add_ice_cubes(self) -> (IceCubeType, int):
        selected_ice_cubes: Optional[IceCubeType] = None
        cubes_count: int = 0
        while True:
            print('Add ice?')
            user_input = input('1 - Yes, 0 - No').lstrip().rstrip()
            if user_input not in ('1', '0'):
                print('Invalid Choice')
            else:
                break

        if user_input == '0':
            return

        ice_cube_types = self._get_ice_cubes()
        while True:
            print('Which ice add?')
            for i, ic_type in ice_cube_types.items():
                print(f'{i}: {ic_type.value}')

            user_input = input().lstrip().rstrip()
            if not user_input.isdigit() or int(user_input) not in (ice_cube_types.keys()):
                print('Invalid Choice')
            else:
                selected_ice_cubes = ice_cube_types[int(user_input)]
                break

        while True:
            print('How many ice cubes add?')
            user_input = input().lstrip().rstrip()
            if not user_input.isdigit():
                print('Invalid Choice')
            else:
                cubes_count = int(user_input)
                break

        return selected_ice_cubes, cubes_count

    @staticmethod
    def _get_beverages() -> Dict[int, str]:
        beverages = {
            1: 'Coffee',
            2: 'Tea',
            3: 'Milkshake'
        }
        return beverages

    @staticmethod
    def _get_coffee_types() -> Dict[int, CoffeeTypes]:
        coffees = {
            1: CoffeeTypes('Coffee', Coffee),
            2: CoffeeTypes('Latte', Latte),
            3: CoffeeTypes('Cappuccino', Cappuccino)
        }
        return coffees

    @staticmethod
    def _get_tea_types() -> Dict[int, TeaType]:
        tea_types = {
            1: TeaType.BLACK,
            2: TeaType.GREEN,
            3: TeaType.OOLONG,
            4: TeaType.HERBAL
        }
        return tea_types

    @staticmethod
    def _get_milkshake_portions() -> Dict[int, MilkshakePortion]:
        milkshake_portions = {
            1: MilkshakePortion.SMALL,
            2: MilkshakePortion.MEDIUM,
            3: MilkshakePortion.BIG
        }
        return milkshake_portions

    @staticmethod
    def _get_ice_cubes() -> Dict[int, IceCubeType]:
        ice_cubes_types = {
            1: IceCubeType.WATER,
            2: IceCubeType.DRY
        }
        return ice_cubes_types


#machine = CoffeeMachine()
#machine.main()
#
#
latte = Latte(CoffeePortion.DOUBLE)

condiment_latte = ChocolateCrumbs(Syrup(CoconutFlakes(Cinnamon(IceCubes(latte, 2, IceCubeType.WATER)), 10), SyrupType.CHOCOLATE), 5)
# c_ic_latte = Cinnamon(ic_latte)
# cf_c_ic_latte = CoconutFlakes(c_ic_latte, 10)
# s_cf_c_ic_latte = Syrup(cf_c_ic_latte, SyrupType.CHOCOLATE)
# cf_s_cf_c_ic_latte = ChocolateCrumbs(s_cf_c_ic_latte, 5)

print(condiment_latte.get_description())
print(condiment_latte.get_cost())
