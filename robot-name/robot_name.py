import random
import string

class Robot(object):
    # static fields 
    upperLetters = string.ascii_uppercase[:26]
    names = set() # to ensure all names are unique

    # generate a random unique name
    def _generateName(self): 
        result = ''
        for i in range(5):
            if i < 2:
                result += Robot.upperLetters[random.randint(0, 25)]
            else: 
                result += str(random.randint(0, 9))

        # if the name has been generated before, try another one.                
        while result in Robot.names:
            result = self._generateName()

        Robot.names.add(result) # add the new unique name to the set
        return result


    def __init__(self):
        self.name = self._generateName()

    def reset(self):
        random.seed(self) # reset the seed to make sure it won't generate the same name
        self.name = self._generateName()
       
        