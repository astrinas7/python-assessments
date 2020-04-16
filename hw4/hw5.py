from clock import *

#-------------------- Askisi 1 ----------------------------
class RomanCascadeCounter(CascadeCounter):
    """Metritis CascadeCounter me endei3eis me rwmaikous ari8mous."""
    def __str__(self):
        tens = self.value // 10
        units = self.value % 10
        tens_s = 'L' if tens == 5 else tens*'X'
        if units < 5:
            units_s = units*'I'
        else:
            units_s = 'V' + (units-5)*'I'

        sz = len(tens_s + units_s)
        return '-'*(9-sz) + tens_s + units_s


class RomanClock(Clock):
    """Roloi me endei3eis me rwmaika noumera.

    >>> c = RomanClock(23, 59, 58)
    >>> str(c)
    '----XXIII:---LVIIII:----LVIII'
    >>> c.advance()
    >>> print(c)
    ----XXIII:---LVIIII:---LVIIII
    >>> c.advance()
    >>> print(c)
    ---------:---------:---------
    >>> c.advance()
    >>> print(c)
    ---------:---------:--------I
    >>> c.advance()
    >>> print(c)
    ---------:---------:-------II
    """
    def __init__(self, h, m, s):
        self._h = RomanCascadeCounter(None, 24, h)
        self._m = RomanCascadeCounter(self._h,60 ,m)
        self._s = RomanCascadeCounter(self._m, 60, s)


#-------------------- Askisi 2 ----------------------------
class DayCounter(CyclicCounter):
    """Metritis hmeras.

    Paradeigmata:
    >>> d = DayCounter()
    >>> str(d)
    'Sunday'
    >>> d.advance()
    >>> print(d)
    Monday
    >>> d2 = DayCounter('Saturday')
    >>> str(d2)
    'Saturday'
    >>> d2.advance()
    >>> str(d2)
    'Sunday'
    >>> d2.advance()
    >>> str(d2)
    'Monday'
    """
    _days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday',\
            'Thursday', 'Friday', 'Saturday']
    def __init__(self, day = 'Sunday'):
        CyclicCounter.__init__(self, 7, self._days.index(day))

    def __str__(self):
        return self._days[int(CyclicCounter.__str__(self))]


# #-------------------- Askisi 3 ----------------------------
class DayClock(Clock):
    """Roloi me endei3h hmeras.

    >>> c = DayClock(23, 59, 58, 'Sunday')
    >>> str(c)
    '23:59:58 Sunday'
    >>> c.advance()
    >>> str(c)
    '23:59:59 Sunday'
    >>> c.advance()
    >>> str(c)
    '00:00:00 Monday'
    >>> c.advance()
    >>> str(c)
    '00:00:01 Monday'

    An paralhf8ei to onoma imeras (teleytaio orisma ston kataskeyasti)
    tote pairnei timi 'Sunday', px.:
    >>> c = DayClock(6, 35, 0)
    >>> print(c)
    06:35:00 Sunday
    """
    def __init__(self, h = 0, m = 0, s = 0, day = 'Sunday'):
        self._d = DayCounter(day)
        Clock.__init__(self, h, m, s)

    def advance(self):
        Clock.advance(self)
        if Clock.__str__(self) == '00:00:00':
            self._d.advance()

    def __str__(self):
        return Clock.__str__(self) + ' ' + self._d.__str__()


#-------------------- Askisi 4 ----------------------------
class Timer(Clock):
    """Antistrofos xronometritis.

    >>> c = Timer(0, 0, 2)
    >>> str(c)
    '00:00:02'
    >>> c.advance()
    >>> str(c)
    '00:00:01'
    >>> c.advance()
    >>> str(c)
    '00:00:00'
    >>> c.advance()
    >>> str(c)
    'TI DI DI DI'
    >>> c.advance()
    >>> str(c)
    'TI DI DI DI'
    """
    """GRAPSTE TON KWDIKA SAS APO KATW."""

    def __init__(self, h, m, s):
        Clock.__init__(self, 0, 0, 0)
        self.h = h
        self.m = m
        self.s = s

    def advance(self):
        if '{0:02d}:{1:02d}:{2:02d}'.format(self.h, self.m, self.s) != '00:00:00':
            Clock.advance(self)
            self.s -= 1
            if self.s < 0:
                self.s = 60
                self.m -= 1
                if self.m < 0:
                    self.m = 60
                    self.h -= 1

    def __str__(self):
        if '{0:02d}:{1:02d}:{2:02d}'.format(self.h, self.m, self.s) == '00:00:00':
            return 'TI DI DI DI'
        return '{0:02d}:{1:02d}:{2:02d}'.format(self.h, self.m, self.s)



