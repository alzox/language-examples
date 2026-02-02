"""
Imports are interesting because they aren't code, rather for the run-time environment or build tools to allow you to reference other files as code.
"""
# import [library]
# import [library] as [name]
import numpy as np 

# library.method
print(np.round(1.5))

# from [library] import [method/class]
# from .../../.[module/package] import * or [method/class/module] -> so forth
# imports are relative to sys.path usually set by a framework entry-point or running locally with an if main
# instead of dual imports run it with python -m package.[some py file] 
# __init__.py defines a package and requires you to "export packages"
import imports # see imports folder for example

imports.a_func()
imports.b.b_print()
imports.c.c_print()


