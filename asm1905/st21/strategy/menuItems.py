from .developer import Developer, DeveloperBehavior
from .scrumMaster import ScrumMaster, ScrumMasterBehavior
from .productOwner import ProductOwner, ProductOwnerBehavior

MENU = [
    ['See list of employees', 'show_scrum_team'],
    ['Add employee', 'add_employee'],
    ['Listen to employee', 'listen_personal'],
    ['Edit employee', 'edit_employee'],
    ['Fire employee', 'remove_employee'],
    ['Export to file', 'save_to_file'],
    ['Import from file', 'load_from_file']
]

ADDITION_MENU = [
    ['Add product owner', ProductOwner, ProductOwnerBehavior],
    ['Add scrum master', ScrumMaster, ScrumMasterBehavior],
    ['Add developer', Developer, DeveloperBehavior]
]
