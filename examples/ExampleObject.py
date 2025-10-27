# =============================================== Connecting to the factory
import pathlib
script_path = str(pathlib.Path(__file__).parent.resolve()) + "/"

import sys
sys.path.append(script_path + "../../")

from tfc_PyFactory import *

# =============================================== Defining the class
class ExampleObject(TFCObject):

    @staticmethod
    def getInputParameters() -> InputParameters:
        params = TFCObject.getInputParameters() # Gets parent parameters

        # Optional parameters always have the same pattern of arguments
        # - name of the parameter.
        # - default value.
        # - a doc-string. Describing what the parameter does.
        #
        # Usage:
        params.addOptionalParam("message",      # name of the parameter
                                "Hello world!", # Default value
                                "DocString What this parameter is for")

        return params

    def __init__(self, params):
        super().__init__(params)

        self.message_ = params.getParam("message").getStringValue()

        print(self.message_)

# =============================================== Registering the class
PyFactory.register(ExampleObject, "ExampleObject")

