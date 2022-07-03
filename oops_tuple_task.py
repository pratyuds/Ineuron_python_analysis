import logging
logging.basicConfig(filename="logs/oopslog.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')
class Tuple_op:
    logging.info("sucessfully entered into class")
    try:
        logging.info("sucessfully entered into try block")
        def __init__(self,l):
            self.l = tuple(l)

        def tp_op1(self):
            try:
                logging.info("this is first index op")
                a = self.l[0]
                b = self.l[5]
            except Exception as e:
                logging.error("some error is occured",e)
            return a,b

        def tp_op2(self):
            try:
                logging.info("this is negative indexing op")
                a = self.l[-1]
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def tp_op3(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[0:5]
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def tp_op4(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[:-5]
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def tp_op5(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[-5:-1]
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def tp_op6(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[-5:-1]
            except Exception as e:
                logging.error("some error is occured", e)
            return a

        def tp_op7(self):
            try:
                logging.info("this is range indexing op")
                a = self.l[0:10:2]
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def tp_type(self):
            try:
                logging.info("this is type indexing op")
                a = type(self.l)
            except Exception as e:
                logging.error("some error is occured",e)
            return a

        def tp_len(self):
            try:
                logging.info("this is length op")
                a = len(self.l)
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def tp_add(self):
            try:
                logging.info("this is add tuple op")
                s = tuple(input("enter tuple : "))
                a = self.l +s
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def tp_index(self):
            try:
                logging.info("this is index from tuple op")
                s = input("enter index postion : ")
                a = self.l.index(3)
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def tp_add1(self):  ######### dought
            try:
                logging.info("this is add1 from tuple op")
                s = ("data","NLP")
                a = self.l + s
                return a
            except Exception as e:
                logging.error("some error is occured", e)
        def tp_typecast(self):
            try:
                logging.info("this is typecast from tuple op")
                a = list(self.l)
                b = str(self.l)
            except Exception as e:
                logging.error("some error is occured", e)
            return a,b

    except Exception as e:
        logging.error(" class is failed, need to pass string as a perameter")


list1 = Tuple_op((1,2,2,2,3,4,5,"pratyu",23.76,True))
list2 = Tuple_op((1,2,3,4,5,23.76))
list3 = Tuple_op(("pratyu","ineuron"))

logging.info(list1.tp_op1())
logging.info(list1.tp_op2())
logging.info(list1.tp_op3())
logging.info(list1.tp_op4())
logging.info(list1.tp_op5())
logging.info(list1.tp_op6())
logging.info(list1.tp_op7())
logging.info(list1.tp_type())
logging.info(list1.tp_len())
logging.info(list1.tp_add())
logging.info(list1.tp_index())
logging.info(list3.tp_add1())
logging.info(list1.tp_typecast())
