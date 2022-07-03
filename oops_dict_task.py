import logging
logging.basicConfig(filename="logs/oopslog.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')
class Dict_op:
    logging.info("sucessfully entered into class")
    try:
        logging.info("sucessfully entered into try block")
        def __init__(self,l):
            self.l = dict(l)

        def dt_type(self):
            try:
                logging.info("this is type op")
                a = type(self.l)
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def dt_index(self):
            try:
                logging.info("this is key index op")
                s = input("enter a key value : ")
                a = self.l[s]
                return a
            except Exception as e:
                logging.error("some error is occured",e)
        def dt_index_val(self):
            try:
                logging.info("this is key base list index op")
                s = str(input("enter a key value : "))
                p = int(input("enter postion which one you want : "))
                a = self.l[s][p]
                return a
            except Exception as e:
                logging.error("some error is occured",e)
        def dt_index_val1(self):
            try:
                logging.info("this is key base list index exist or not op")
                s = str(input("enter a key value : "))
                p = (input("enter value which one you want : "))
                a = p in self.l[s]
                return a
            except Exception as e:
                logging.error("some error is occured",e)

        def dt_key(self):
            try:
                logging.info("this is key base list ikeyop")
                a = self.l.keys()
                return a
            except Exception as e:
                logging.error("some error is occured",e)

        def dt_value(self):
            try:
                logging.info("this is key base list baaed on key op")
                a = self.l.values()
                return a
            except Exception as e:
                logging.error("some error is occured",e)
        def dt_fromkeys(self):
            try:
                logging.info("this is from keys op")
                s = str(input("enter a from key value : "))
                a = self.l.fromkeys(s)
                return a
            except Exception as e:
                logging.error("some error is occured",e)

        def dt_get(self):
            try:
                logging.info("this is get keys op")
                s = str(input("enter a get key value : "))
                a = self.l.get(s)
                return a
            except Exception as e:
                logging.error("some error is occured",e)


        def dt_pop(self):
            try:
                logging.info("this is pop keys op")
                s = str(input("enter a pop key value : "))
                a = self.l.pop(s)
                return a
            except Exception as e:
                logging.error("some error is occured",e)

        def dt_popitem(self):
            try:
                logging.info("this is popitem keys op")
                a = self.l.popitem()
                return a
            except Exception as e:
                logging.error("some error is occured",e)
        def dt_setdefault(self):
            try:
                logging.info("this is setdefault keys op")
                key = str(input("enter key for setdefault : "))
                a = self.l.setdefault(key)
                return a
            except Exception as e:
                logging.error("some error is occured",e)

        def dt_setdefault1(self):
            try:
                logging.info("this is setdefault key, value op")
                key = str(input("enter key for setdefault : "))
                val = str(input("enter value for setdefault : "))
                a = self.l.setdefault(key,val)
                return a
            except Exception as e:
                logging.error("some error is occured",e)
        def dt_update(self):  ####### dought
            try:
                logging.info("this is update key, value op")
                key = str(input("enter key for update : "))
                val = int(input("enter value for update : "))
                a = self.l.update({key: val})
                return self.l
            except Exception as e:
                logging.error("some error is occured",e)


        def dt_key_tuple(self):  ######## dought
            try:
                logging.info("this is key base list index exist or not op")
                s = (1,2,3)
                a = self.l[s]
                return a
            except Exception as e:
                logging.error("some error is occured", e)

    except Exception as e:
        logging.error(" class is failed, need to pass string as a perameter")


list1 = Dict_op({"name":"pratyu","id":62,"email":"pratyu@gmail.com","dob":1991,"contact":123456})
list2 = Dict_op({"name":"pratyu","id":62,"email":"pratyu@gmail.com","dob":1991,"contact":123456,"tech":["python","API","ML","DL","NLP"]})
list3 = Dict_op({(1,2,3):"abc"})
logging.info(list1.dt_type())
logging.info(list1.dt_index())
logging.info(list2.dt_index())
logging.info(list2.dt_index_val())
logging.info(list2.dt_index_val1())
logging.info(list3.dt_key())
logging.info(list3.dt_value())
logging.info(list1.dt_fromkeys())
logging.info(list1.dt_get())
logging.info(list2.dt_pop())
logging.info(list1.dt_popitem())
logging.info(list1.dt_setdefault())
logging.info(list1.dt_setdefault1())
logging.info(list1.dt_update())
logging.info(list3.dt_key_tuple())


