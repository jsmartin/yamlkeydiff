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

```
./yamlkeydiff.py old_vars new_vars
--- new_vars

+++ old_vars

@@ -1,3 +1,4 @@

 a
+b
+c
 d
-z
```
