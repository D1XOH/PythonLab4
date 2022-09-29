import mmap



class Sorting:
    # def init(self, mm):
    #     self.mm = mm


    i = 0
    k = 0
    j = 0



    sort_choice = {'day': [1,9,11], 'hour': [1,9,14], 'minute': [1,9,17] }

    def read(self, i, k, j):
        file_from = open('events.txt', mode='r', encoding='utf8')
        mm = mmap.mmap(file_from.fileno(), length=0, access=mmap.ACCESS_READ, offset=0)
        str = mm.readline().decode()
        count = 0
        prestr = "[2018-05-14 19:37:47.873687] OK"
        while str:
            str = mm.readline().decode()

            if str[k:j] == prestr[k:j]:
                if prestr[29] == "N":
                    count += 1
            elif (str[k:j] != prestr[k:j]) and (prestr[29] == "N"):
                count += 1
                print("<", prestr[k:j], ">", count)
                count = 0
            else:
                print("<", prestr[k:j], ">", count)
                count = 0

            prestr = str

    def menu(self):
        print('enter: 1 for sort by day, 2 by hour, 3 by minute')
        value = input()
        if value == "1":
            self.i = self.sort_choice['day'][0]
            self.k = self.sort_choice['day'][1]
            self.j = self.sort_choice['day'][2]
            Sorting.read(self, self.i, self.k, self.j)
        elif value == "2":
            self.i = self.sort_choice['hour'][0]
            self.k = self.sort_choice['hour'][1]
            self.j = self.sort_choice['hour'][2]
            Sorting.read(self, self.i,self.k,self.j)
        elif value == "3":
            self.i = self.sort_choice['minute'][0]
            self.k = self.sort_choice['minute'][1]
            self.j = self.sort_choice['minute'][2]
            Sorting.read(self, self.i,self.k,self.j)
        else:
            print('error value')
            Sorting.menu(self)




s = Sorting()
s.menu()