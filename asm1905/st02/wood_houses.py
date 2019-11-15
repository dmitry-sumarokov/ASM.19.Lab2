if __name__ == '__main__':
    from houses import house
    from material_types import woodType
else:
    from .houses import house
    from .material_types import woodType


class wood_house(house):
    def __init__(self, owner_name='', square=0):
        super().__init__(woodType(), owner_name, square)
