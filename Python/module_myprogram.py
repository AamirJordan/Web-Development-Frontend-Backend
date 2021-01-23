import modules_mymodule
modules_mymodule.func_in_module()


#   OR  ------------------------------------------------------------------------

import modules_mymodule as mm
mm.func_in_module()

#   OR  ------------------------------------------------------------------------

from modules_mymodule import func_in_module
func_in_module()

#   OR  ------------------------------------------------------------------------

from modules_mymodule import *
func_in_module()
