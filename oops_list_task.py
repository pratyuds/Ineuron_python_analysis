import logging
logging.basicConfig(filename="logs/oopslog.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')
class List_op:
    logging.info("sucessfully entered into class")
    try:
        logging.info("sucessfully entered into try block")
        def __init__(self,l):
            self.l = list(l)

        def lt_op1(self):
            try:
                logging.info("this is first index op")
                a = self.l[0]
                b = self.l[5]
            except Exception as e:
                logging.error("some error is occured",e)
            return a,b
        def lt_op2(self):
            try:
                logging.info("this is negative indexing op")
                a = self.l[-1]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_op3(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[0:5]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_op4(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[:-5]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_op5(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[-5:-1]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_op6(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[-5:-1]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_op7(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[0:10:2]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_type(self):
            try:
                logging.info("this is type indexing op")
                a = type(self.l)
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def lt_len(self):
            try:
                logging.info("this is length op")
                a = len(self.l)
            except Exception as e:
                logging.error("some error is occured",e)
            return a

        def lt_add(self):
            try:
                logging.info("this is add value op")
                a = self.l + ['ineuron']
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def lt_in(self):
            try:
                logging.info("this is in check op")
                a = 'ineuron' in self.l
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def lt_max(self):
            try:
                logging.info("this is max op")
                a = max(self.l)
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def lt_min(self):
            try:
                logging.info("this is min op")
                a = min(self.l)
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def lt_append(self):   ### dought 1
            try:
                logging.info("this is append op")
                # s = list(input("enter lt_append list : "))
                s = [11,22,33]
                a = self.l.append(s)
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)
        def lt_pop(self):
            try:
                logging.info("this is pop op")
                a = self.l.pop(4)
                b = self.l.pop()
            except Exception as e:
                logging.error("some error is occured", e)
            return a,b
        def lt_reverse(self): ########   dought 2
            try:
                logging.info("this is reverse op")
                a = list(reversed(self.l))
                b = self.l[::-1]
            except Exception as e:
                logging.error("some error is occured", e)
            return a,b
        def lt_sort(self):   #### dought
            try:
                logging.info("this is sort op")
                a = self.l.sort()
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)
        def lt_3(self):
            try:
                logging.info("this is append 3 lists op")
                l1 = list(input("enter first list : "))
                l2 = list(input("enter second list : "))
                l3 = list(input("enter third list : "))
                l4 =[l1,l2,l3]
                a = l4
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def lt_4(self):
            try:
                logging.info("this is extract value from nested list op")
                a = self.l[2][1]
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def lt_count(self):
            try:
                logging.info("this is count repeated value op")
                a = self.l.count(2)
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def lt_extend_str(self):  ######   dought4
            try:
                logging.info("this is extend with string op")
                a = self.l.extend('datascience')
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

        def lt_extend_lst(self):  ######   dought4
            try:
                logging.info("this is extend with list op")
                s = list(input("eneter new list : "))
                a = self.l.extend(s)
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

        def lt_extend_tup(self):  ######   dought4
            try:
                logging.info("this is extend with tuple op")
                a = self.l.extend((1,2,3))
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

        def lt_extend_set(self):  ######   dought4
            try:
                logging.info("this is extend with set op")
                a = self.l.extend({1,2,3})
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

        def lt_extend_dict(self):  ######   dought4
            try:
                logging.info("this is extend with dictionary op")
                a = self.l.extend({"a":1,"b":2,"c":3})
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

        def lt_index(self):
            try:
                logging.info("this is index position op")
                s = int(input("enter index value from list : "))
                a = self.l.index(s)
                return a
            except Exception as e:
                logging.error("some error is occured", e)

        def lt_insert(self):
            try:
                logging.info("this is insert value with position op")
                a = self.l.insert(1,"machine")
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)
        def lt_remove(self): ##### dought
            try:
                logging.info("this is remove op")
                # s = input("enter value list : ")
                a = self.l.remove(1)
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

    except Exception as e:
        logging.error(" class is failed, need to pass string as a perameter")

list1 = List_op([1,2,2,2,3,4,5,"pratyu",23.76,True])
list2 = List_op([7,4,1,2,3,4,5])
list3 = List_op([[1,2,3],[4,5,6],[7,8,9]])

logging.info(list1.lt_op1())
logging.info(list1.lt_op2())
logging.info(list1.lt_op3())
logging.info(list1.lt_op4())
logging.info(list1.lt_op5())
logging.info(list1.lt_op6())
logging.info(list1.lt_op7())
logging.info(list1.lt_type())
logging.info(list1.lt_len())
logging.info(list1.lt_add())
logging.info(list1.lt_in())
logging.info(list2.lt_max())
logging.info(list2.lt_min())
logging.info(list2.lt_append())
logging.info(list2.lt_pop())
logging.info(list2.lt_reverse())
logging.info(list2.lt_sort())
logging.info(list2.lt_3())
logging.info(list3.lt_4())
logging.info(list1.lt_count())
logging.info(list1.lt_extend_str())
logging.info(list1.lt_extend_lst())
logging.info(list1.lt_extend_tup())
logging.info(list1.lt_extend_set())
logging.info(list1.lt_extend_dict())
logging.info(list1.lt_index())
logging.info(list1.lt_insert())
logging.info(list1.lt_remove())





