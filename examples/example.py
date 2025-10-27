# =============================================== Connecting to the factory
import pathlib
script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

import sys
sys.path.append(script_path + "../../")

from tfc_PyFactory import *
import ExampleObject

# =============================================== Make the object
# Making simple parameters. Normally you would build
# dictionaries from something like yaml files.
object1_params = Parameter("", {"type": "ExampleObject"})
object2_params = Parameter("", {"type": "ExampleObject",
                                "message": "Hi me"})

# Here we make the objects
# Arguments to PyFactory.makeObject
# - name for the object
# - parameters
object1 = PyFactory.makeObject("First object", object1_params)
object2 = PyFactory.makeObject("Second object", object2_params)




