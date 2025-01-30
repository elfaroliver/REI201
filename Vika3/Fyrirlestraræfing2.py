
class Skil(object):
    """fyrirlestradaemi 2 f. REI
    """
    def f2(self,text):
        #alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
        '''for stak in text:
            if (stak1 fyrr í ascii):
                place í fyrra stak í print
            else:
                place í seinna stak'''
        
        '''for [] in text:
            if ([] )'''
        
        '''mylist = text
        mylist.sort()
        print(mylist)'''

        ls = []
        for i in sorted(set(text)):
            ls.append(text.count(i))

        return ls
