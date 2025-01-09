from prettytable import PrettyTable  #import prettytable package 

table = PrettyTable() # construct a PrettyTable() Object 

table.add_column("Pokemon Name",["Pikachu","Squirtle", "Charmander"])
table.add_column("Type", ["Electric","Water","Fire"])

table.align = "l"

print(table)