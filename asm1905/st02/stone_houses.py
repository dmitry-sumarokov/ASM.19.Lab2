if __name__ == '__main__':
    from houses import house
    from material_types import stoneType
else:
    from .houses import house
    from .material_types import stoneType

class stone_house(house):
    def __init__(self, owner_name="", square=0):
        super().__init__(stoneType(), owner_name, square)
