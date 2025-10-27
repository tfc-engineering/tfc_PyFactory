# tfc_PyFactory - An easy-to-use Factory-Pattern for python

## Quick overview

- Object classes must derive from `TFCObject`
- Object classes must define the static method `getInputParameters`, example:
  ```python
  class ExampleObject(TFCObject):

      @staticmethod
      def getInputParameters() -> InputParameters:
          params = TFCObject.getInputParameters() # Gets parent parameters
  ```
- Object classes must have constructor syntax like this:
  ```python
      def __init__(self, params):
          super().__init__(params)

          self.message_ = params.getParam("message").getStringValue()

          print(self.message_)
  ```
- Parameters can be optional or required.
- Object are created with:
  ```python
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
  ```
