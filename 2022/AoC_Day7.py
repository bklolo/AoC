from treelib import Node, Tree

x = open("AoC7.txt").read().split("\n")

'''process'''
# create_node(tag=None, 
#              identifier=None, 
#              parent=None, 
#              data=None)

def createTree(file, tree):         #### need to go over TreeLib funcs
    parentNode = []

    for line in file:
        cd = line[2:4]
        dir = line[0:3]
        folder = line[5:] if cd == 'cd' else line[4:]
        size = [int(s) for s in line.split() if s.isdigit()]

        if cd == "cd":
            if folder == '..':
                parentNode.pop()
            else:
                if tree.size() == 0:
                    parentNode.append(folder)
                    tree.create_node(folder, folder, None)
                else:
                    parentNode.append(folder)
                    tree.create_node(folder, None, parentNode[-1])

        if dir == "dir":
            tree.create_node(folder, None, parentNode[-1])
        tree.show()

tree = Tree()
createTree(x, tree)
tree.show()
