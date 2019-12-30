from .developer import Developer, DeveloperBehavior
from .scrumMaster import ScrumMaster, ScrumMasterBehavior
from .productOwner import ProductOwner, ProductOwnerBehavior

MENU = [
    ['Add employee', 'add'],
    ['Export to file', 'export'],
    ['Import from file', 'load']
]

ADDITION_MENU = [
    ['Add product owner', ProductOwner, ProductOwnerBehavior],
    ['Add scrum master', ScrumMaster, ScrumMasterBehavior],
    ['Add developer', Developer, DeveloperBehavior]
]
