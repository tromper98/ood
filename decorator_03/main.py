from impl import *

latte = Latte(CoffeePortion.DOUBLE)

ic_latte = IceCubes(latte, 2, IceCubeType.WATER)
c_ic_latte = Cinnamon(ic_latte)
cf_c_ic_latte = CoconutFlakes(c_ic_latte, 10)
s_cf_c_ic_latte = Syrup(cf_c_ic_latte, SyrupType.CHOCOLATE)
cf_s_cf_c_ic_latte = ChocolateCrumbs(s_cf_c_ic_latte, 5)

print(cf_c_ic_latte.get_description())
print(cf_c_ic_latte.get_cost())

print(s_cf_c_ic_latte.get_description())
print(s_cf_c_ic_latte.get_cost())

print(cf_s_cf_c_ic_latte.get_description())
print(cf_s_cf_c_ic_latte.get_cost())
