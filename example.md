This cli tool helps you write docs with AI. The program automatically detects which files have been changed since the last commit. You have the ability as a user to accept changes to each file individually. 

Example from the interactive terminal:
```
items = ["apple", "banana", "orange"]                         | new_items = ["apple", "banana", "orange"]
for i in items:                                                 for i in items:
    print(i)                                                        print(i)
    for j in items:                                                 for j in items:
        print(j)                                                        print(j)
                                                              \         
                                                              > print("Success")

Accept these changes in folder/file2.py? [y/N]: y
Changed folder/file2.py
```

Program flow:
1) Run ```git diff --name-only``` to get the file paths of the uncommited files.
2) Filter which files you wish not to be rewriteen by autodocs.
3) Run ```diff``` between you current file and one created automatically by autodocs.
4) You have the option to accept or not the changes. The confirmation is required file by file. You also have the option to allow all modifications using the ```-a``` or ```--all-files``` flags.
5) Use the ```-v``` or ```verbose``` flag for more informative output.

If successful, the tool can be implemented in github workflows.
