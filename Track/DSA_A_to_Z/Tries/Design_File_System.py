"""
=> Description
- In this problem, you need to design a file system that can create a new path and bind a value.
- Each of these paths begins with a separator /, and there must be several lowercase letters after each separator.
  - For example, /lint and /lint/code are valid paths, while an empty string and / are not.

You need to implement the following method:
1. bool createPath(string path, int value)
- Creates a new path and associates it with the given value.
    1. Returns true if the path was created successfully.
    2. Returns false if:
        - The path already exists, or
        - The parent path does not exist ( every folder before the newFolder must be already created )

    Note: A path is a string that starts with / and consists of one or more directory names separated by /.
    For example: /a, /a/b, /a/b/c

2. int get(string path)
- Returns the value associated with the given path.
- Returns -1 if the path does not exist.


Note: Paths cannot be recreated to modify bound values

The premise of creating a path is that the preceding paths have been created in advance. For example, the initial path is /lint, which can be created, but /lint/code cannot because we must create /lint first.

=> EXAMPLES
Example 1
createPath("/a", 1) -> True
createPath("/a", 10) -> False ( No path recreating/re-assignment allowed)
createPath("/a/b", 2) -> True
get("/a") -> 1
get("/a/b") -> 2

Example 2
createPath("/a", 1) -> True
createPath("/a/b/c", 2) -> False (You need to have /a/b created but you dont)
get("/a") -> 1
get("/a/b") -> -1


"""


class TrieNode:
    def __init__(self, val: int = -1):
        self.value = val
        self.childs = {}


class FileSystemTrie:
    def __init__(self):
        self.root = TrieNode()
    
    def createPath(self, path: str, val: int) -> bool:
        paths = path.split("/")[1:]

        parent_folders = paths[:-1]
        new_folder = paths[-1]
        cur = self.root

        for folder in parent_folders:
            if folder not in cur.childs: # IF any parent folders dont exist
                return False
            cur = cur.childs[folder]
        
        if new_folder in cur.childs: # ALREADY EXISTS
            return False
        
        cur.childs[new_folder] = TrieNode(val)
        return True
    
    def getPath(self, path: str) -> int:
        paths = path.split("/")[1:]
        parent_folders = paths[:-1]
        dest_folder = paths[-1]
        cur = self.root    

        for folder in parent_folders:
            if folder not in cur.childs: # The parent path only does exist
                return -1
            cur = cur.childs[folder]
            
        # check if final folder exists or not
        return cur.childs[dest_folder].value if dest_folder in cur.childs else -1


# Example 1
fileSystem = FileSystemTrie()
print(fileSystem.createPath("/a", 1)) # -> True
print(fileSystem.createPath("/a", 10)) # -> False ( No path recreating/re-assignment allowed)
print(fileSystem.createPath("/a/b", 2) ) # -> True
print(fileSystem.getPath("/a")) # -> 1
print(fileSystem.getPath("/a/b"))  # -> 2


# Example 2
print("===="*10)
fileSystem = FileSystemTrie()
print(fileSystem.createPath("/a", 1)) # -> True
print(fileSystem.createPath("/a/b/c", 2))  #-> False (You need to have /a/b created but you dont)
print(fileSystem.getPath("/a"))  # -> 1
print(fileSystem.getPath("/a/b") ) # -> -1