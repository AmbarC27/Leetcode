class FileSystem:

    def __init__(self):
        self.paths = {"":-1} ## empty string is the root path, and
        ## we give it a dummy value

    def createPath(self, path: str, value: int) -> bool:
        if path in self.paths or path[:path.rfind("/")] not in self.paths:
            ## Note for the second condition above, path.rfind("/") can
            ## also be "", and we have taken care of that during initialization
            return False
        self.paths[path] = value
        return True

    def get(self, path: str) -> int:
        return self.paths.get(path,-1)


# Your FileSystem object will be instantiated and called as such:
# obj = FileSystem()
# param_1 = obj.createPath(path,value)
# param_2 = obj.get(path)