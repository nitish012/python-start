


class Role(object):
    NORMAL = 'NORM'
    CLASSTEACHER = 'CLST'

    CHOICES = [
        (NORMAL, 'normal'),
        (CLASSTEACHER, 'classteacher'),
    ]

class Branches(object):
    COMPUTER = 'CS'
    ELECTRONIC = 'ELEC'

    CHOICES = [
        (COMPUTER,'computer'),
        (ELECTRONIC,'electronic'),
    ]

class Grades(object):
    FIRST = 'A'
    SECOND = 'B'
    THIRD = 'C'

    CHOICES = [
        (FIRST,'a'),
        (SECOND, 'b'),
        (THIRD, 'c')
    ]    

