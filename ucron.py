class UCron:
    MD = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    DAY = 24*60*60
    HOUR = 60*60
    MIN = 60


    def __init__(self, line):
        self.__line = line
        self.hours = None
        self.minutes = None
        self.days = None
        self.months = None
        self.weekdays = None
        self.years = None
        self.__parse()


    def next(self, now):
        y = self.__ne(self.years, now[0])
        o = self.__ne(self.months, now[1]-1)
        d = self.__ne(self.days, now[2]-1)
        h = self.__ne(self.hours, now[3])
        m = self.__ne(self.minutes, now[4])
        return self.__sb((y,o,d,m,h, -1,-1), now)

    def __ne(self, data, min):
        res = min
        for x in data:
            if x>=min:
                res = x
                break
        return res

    def __sb(self, n, c):
        d = self.MIN * (n[5]-c[5])
        d += self.HOUR * (n[4]-c[4])
        d +=self.DAY * (n[3]-c[3])
        return d

    def __parse_group(self, group, _max=60):
        try:
            if group.index("/") >=0:
                [a,b] = group.split("/")
                if a != "*":
                    a,b = int(a), int(b)
                    return [x % _max for x in range(a % _max, (a+_max), b)]
                else:
                    b = int(b)
                    return [x % _max for x in range(0, _max, b)]
        except ValueError:
            pass
        
        try:    
            if group.index("-") >=0:
                [a,b] = [int(x) for x in group.split("-")]
                return [x for x in range(a, b)]
        except ValueError:
            pass

        if group == "*":
            return [x for x in range(_max)]

        return int(group)


    def __parse_elem(self, elem, _max):
        groups =[self.__parse_group(x.strip(), _max) for x in elem.split(",")]
        result = []
        for group in groups:
            if type(group) == list:
                result.extend(group)
            else:
                result.append(group)
        return sorted(result)


    def __parse(self):
        elems = self.__line.split(" ")
        #parse minutes
        self.minutes = self.__parse_elem(elems[0], 60)
        #parse hours
        self.hours = self.__parse_elem(elems[1], 24)
        #parse days
        self.days = self.__parse_elem(elems[2], 31)
        #parse months
        self.months = self.__parse_elem(elems[3], 12)
        #parse weekdays
        self.weekdays = self.__parse_elem(elems[0], 7)
        #generate years:
        self.years = range(1970, 2170)[:]
        

ct = UCron("1/10,22,40-48 */2 */3 */4 */5")
n = ct.next((2018, 12, 8, 19, 59, 22, 5, 349))
print(n)
n = ct.next((2019, 0, 0, 0, 0, 0, -1, -1))
print(n)