"""
Test codes:

    Id = ''
        Other = ''
        args = cmdLine.split('.', 1)
        if (len(args) == 2):
            #  given class name acquired
            Class = args[0] 
            args = args[1].split('(', 1)
            #  user command acquired
            Cmnd = args[0] 
            if (len(args) == 2):
                args = args[1].split(')', 1)
                if (len(args) == 2):
                    # class id acquired
                    Id = args[0] 
                    # other additional arguments
                    Other = args[1] 
            parsed_cmdL = Cmnd + ' ' + Class + ' ' + Id + ' ' + Other
            print(parsed_cmdL)
            return parsed_cmdL
        else:
            return cmdLine 
"""


class my:

    n = 100

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def to_dict(self):
        dic = self.__dict__.copy()
        return (dic)

m1 = my("Any", "20")

print(m1.to_dict())
