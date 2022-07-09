orig_dict = {"Programs" : 100, "Jcls" : 45, "Procs" : 38}
# new_dict = {1 : ["Programs", "Jcl", "Procs"], 2 : [100, 45, 38]}
# convert orig to new.
new_dict = {}
print(len(orig_dict.keys()))
new_dict[1] = orig_dict.keys()
new_dict[2] = orig_dict.values()
print(new_dict[1])
print(new_dict)
print(new_dict.get(1))

