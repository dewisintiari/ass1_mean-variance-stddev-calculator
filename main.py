# This entrypoint file to be used in development. Start by reading README.md
import mean_var_std
from unittest import main

x = mean_var_std.calculate([9,1,5,3,3,3,2,9,0])
print(x)

# Run unit tests automatically
main(module='test_module', exit=False)