#import module_name
import printing_functions

unprinted_design = ['phone case', 'robot pandent', 'dodecahedron']
completed_models = []

printing_functions.print_models(unprinted_design, completed_models)
printing_functions.show_completed_models(completed_models)

# from module_name import function_name
from printing_functions import print_models, show_completed_models
unprinted_design = ['phone case', 'robot pandent', 'dodecahedron']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)

# import module_name as mn
import printing_functions as pf

unprinted_design = ['phone case', 'robot pandent', 'dodecahedron']
completed_models = []

pf.print_models(unprinted_design, completed_models)
pf.show_completed_models(completed_models)

# from module_name import function_name as fn
from printing_functions import print_models as pm
from printing_functions import show_completed_models as scm
unprinted_design = ['phone case', 'robot pandent', 'dodecahedron']
completed_models = []

pm(unprinted_design, completed_models)
scm(completed_models)

#from module_name import *

from  printing_functions import *
unprinted_design = ['phone case', 'robot pandent', 'dodecahedron']
completed_models = []

print_models(unprinted_design, completed_models)
show_completed_models(completed_models)