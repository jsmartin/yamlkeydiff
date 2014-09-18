Compares keys in 2 yaml files

```
usage: yamlkeydiff.py [-h] new_vars_file old_vars_file

positional arguments:
  new_vars_file
  old_vars_file

optional arguments:
  -h, --help     show this help message and exit
```


Example:


	./yamlkeydiff.py new_vars old_vars
	--- old_vars
	
	+++ ./new_vars
	
	@@ -1,4 +1,3 @@
	
	 a
	-b
	-c
	 d
	+z
