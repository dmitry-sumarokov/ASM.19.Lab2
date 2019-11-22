if __name__ == '__main__':
    from houses import materialType
else:
    from .houses import materialType

class stoneType(materialType):
    def do_algorithm(self):
        print("House type is STONE")
    
class woodType(materialType):
    def do_algorithm(self):
        print("House type is WOOD")
