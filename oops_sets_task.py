import logging
logging.basicConfig(filename="logs/oopslog.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')
class Set_op:
    logging.info("sucessfully entered into class")
    try:
        logging.info("sucessfully entered into try block")
        def __init__(self,l):
            self.l = set(l)

        def set_type(self):
            try:
                logging.info("this is type op")
                a = type(self.l)
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def set_index(self):
            try:
                logging.info("this is key index op")
                s = int(input("enter a key value : "))
                a = list(self.l)[s]
                b = tuple(self.l)[s]
                return a,b
            except Exception as e:
                logging.error("some error is occured",e)

        def set_typecast(self):
            try:
                logging.info("this is key index op")
                a = list(self.l)
                b = tuple(self.l)
                return a,b
            except Exception as e:
                logging.error("some error is occured",e)

        def set_add(self):   ########## doubt
            try:
                logging.info("this is adding value op")
                s = int(input("enter a  value to add : "))
                a = self.l.add(s)
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)
        def set_remove(self):   ########## doubt
            try:
                logging.info("this is remove value op")
                s = int(input("enter a  value to remove : "))
                a = self.l.remove(s)
                return self.l
            except Exception as e:
                logging.error("some error is occured", e)

        def set_copy(self):
            try:
                logging.info("this is copy op")
                a = self.l.copy()
                return a
            except Exception as e:
                logging.error("some error is occured", e)
        def set_difference(self):
            try:
                logging.info("this is difference  op")
                s = {1,23,7,8,9,4}
                a = s.difference(self.l)
                return a
            except Exception as e:
                logging.error("some error is occured", e)

        def set_difference_update(self):
            try:
                logging.info("this is difference update  op")
                s = {1,23,7,8,9,4}
                a = s.difference_update(self.l)
                return s
            except Exception as e:
                logging.error("some error is occured", e)
        def set_intersection(self):
            try:
                logging.info("this is intersection   op")
                s = {1,23,7,8,9,4}
                a = s.intersection(self.l)
                return a
            except Exception as e:
                logging.error("some error is occured", e)
        def set_intersection_update(self):
            try:
                logging.info("this is intersection update  op")
                s = {1,23,7,8,9,4}
                a = s.intersection_update(self.l)
                return s
            except Exception as e:
                logging.error("some error is occured", e)
        def set_isdisjoint(self):
            try:
                logging.info("this is disjoint  op")
                s = {1,23,7,8,9,4}
                a = s.isdisjoint(self.l)
                return a
            except Exception as e:
                logging.error("some error is occured", e)
        def set_issubset(self):
            try:
                logging.info("this is subset  op")
                s = {1,23,7,8,9,4}
                a = s.issubset(self.l)
                return a
            except Exception as e:
                logging.error("some error is occured", e)
        def set_issuperset(self):
            try:
                logging.info("this is superset  op")
                s = {1,23,7,8,9,4}
                a = s.issuperset(self.l)
                return a
            except Exception as e:
                logging.error("some error is occured", e)

        def set_symmetric_diff(self):
            try:
                logging.info("this is symmetric_difference  op")
                s = {1, 23, 7, 8, 9, 4}
                a = s.symmetric_difference(self.l)
                return a
            except Exception as e:
                logging.error("some error is occured", e)

        def set_symmetric_diif_update(self):
            try:
                logging.info("this is symmetric_difference update  op")
                s = {1, 23, 7, 8, 9, 4}
                a = s.symmetric_difference_update(self.l)
                return s
            except Exception as e:
                logging.error("some error is occured", e)
        def set_union(self):
            try:
                logging.info("this is union   op")
                s = {1, 23, 7, 8, 9, 4}
                a = s.union(self.l)
                return s
            except Exception as e:
                logging.error("some error is occured", e)
    except Exception as e:
        logging.error(" class is failed, need to pass string as a perameter")


list1 = Set_op({1,2,3,4,2,2,3,5,3,2,4})
list2 = Set_op({1,2,6,6,7,6,8,9})
list3 = Set_op({(1,2,3):"abc"})
logging.info(list1.set_type())
logging.info(list1.set_index())
logging.info(list1.set_typecast())
logging.info(list1.set_add())
logging.info(list1.set_remove())
logging.info(list1.set_copy())
logging.info(list1.set_difference())
logging.info(list1.set_difference_update())
logging.info(list1.set_intersection())
logging.info(list1.set_intersection_update())
logging.info(list1.set_isdisjoint())
logging.info(list1.set_issubset())
logging.info(list1.set_issuperset())
logging.info(list1.set_symmetric_diff())
logging.info(list1.set_symmetric_diif_update())
logging.info(list1.set_union())
