
class path:
    def __init__(self,currentpath):
        self.currentpath=currentpath
        
    def cd(self,newPath):
        if newPath=='/':
            self.currentpath='/'
            return
        while len(newPath)>0:
            if len(newPath) >1:
                print(newPath[0:2])
                if newPath[0:2]=='..':
                    if len(self.currentpath)!=0:
                        self.currentpath=self.currentpath.rsplit('/',1)[0]
                        if len(self.currentpath) == 0:
                            self.currentpath='/'
                        newPath=newPath[2:]
                        continue
            try:
                if (newPath[0] == '/'):
                    newPath=newPath[1:]
                    if newPath[0] == '.':
                        continue
            except:
                raise Exception("invalid path")
            if(self.currentpath[-1]!='/'):
                self.currentpath+='/'
            nextpath=newPath.find('/')
            if nextpath==-1:
                self.currentpath+=newPath
                newPath=''
            else:
                self.currentpath+=newPath[0:nextpath]
                newPath=newPath[nextpath:]
        
        return self.currentpath

path1=path('/a/b/c/d')
path1.cd('../x')
print(path1.currentpath)