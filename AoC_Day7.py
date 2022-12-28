from treelib import Node, Tree

x = open("AoC7.txt").read().split("\n")

'''process'''
# if "cd ", rest of line is node name
# if "ls", next lines up to "cd " are nodes
# if dir, create new node
# if number, current dir size += int(number)

# 

def createTree(file, tree):         #### need to go over TreeLib funcs
    currentNode = ""                   ### putting in too much work?
    parentNode = ""
    depth = 0

    for line in file:
        if depth == 0:
            # Create parent node
            parentNode = line[5]
            tree.create_node(parentNode, parentNode, parent=None)
        # Attach nodes
        if line[2:4] == "cd" and depth > 0:
            if line[5] == ".": # step out of folder
                currentNode = parentNode
                
                depth -= 1
            else: # step into folder
                currentNode = line[5:]
                tree.create_node(currentNode, parent=parentNode)
                parentNode = currentNode
                depth += 1
            # Create child
        '''elif line[0:3] == "dir":
            currentNode = line[4:]
            tree.create_node(currentNode, parent=parentNode)'''
        if depth == 0:
            depth += 1

tree = Tree()
createTree(x, tree)
tree.show()


'''
tree.create_node("Harry", "harry")  # root node
tree.create_node("Jane", "jane", parent="harry")
tree.create_node("Bill", "bill", parent="harry")
tree.create_node("Diane", "diane", parent="jane")
tree.create_node("Mary", "mary", parent="diane")
tree.create_node("Mark", "mark", parent="jane")
tree.show()
'''