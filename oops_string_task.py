import logging
logging.basicConfig(filename="logs/oopslog.log",level=logging.DEBUG,format ='%(levelname)s %(asctime)s %(name)s %(message)s')
class String_op:
    logging.info("sucessfully entered into class")
    try:
        logging.info("sucessfully entered into try block")
        def __init__(self,s):
            self.s = s

        def st_op1(self):
            try:
                logging.info("this is first op")
                a = self.s[0]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op2(self):
            try:
                logging.info("this is second op")
                a = self.s[6]
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_op3(self):
            try:
                logging.info("this is third op")
                a = self.s[-3]
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_op4(self):
            try:
                logging.info("this is fourth op")
                a = self.s[2:10]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op5(self):
            try:
                logging.info("this is fifth op")
                a = self.s[2:10:2]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op6(self):
            try:
                logging.info("this is sixth op")
                a = self.s[8:0:-1]
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op7(self):
            try:
                logging.info("this is seventh op")
                a = self.s+"   hello"
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op8(self):
            try:
                logging.info("this is eighth op")
                a = self.s.count('a')
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op9(self):
            try:
                logging.info("this is ninth op")
                a = self.s.split('t')
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op10(self):
            try:
                logging.info("this is upper op")
                a = self.s.upper()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op11(self):
            try:
                logging.info("this is lower op")
                a = self.s.lower()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_op12(self):
            try:
                logging.info("this is title op")
                a = self.s.title()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_cap(self):
            try:
                logging.info("this is capital op")
                a = self.s.capitalize()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_swap(self):
            try:
                logging.info("this is swapcase op")
                a = self.s.swapcase()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_reverse(self):
            try:
                logging.info("this is reverse op")
                a = ''.join(reversed(self.s))
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_strip(self):
            try:
                logging.info("this is strip op")
                a = self.s.strip()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_lstrip(self):
            try:
                logging.info("this is left strip op")
                a = self.s.lstrip()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_rstrip(self):
            try:
                logging.info("this is right strip op")
                a = self.s.rstrip()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_center(self):
            try:
                logging.info("this is center op")
                a = self.s.center(20,'#')
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_isalnum(self):
            try:
                logging.info("this is alnum op")
                a = self.s.isalnum()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_isalpha(self):
            try:
                logging.info("this is alpha op")
                a = self.s.isalpha()
            except Exception as e:
                logging.error("some error is occured",e)
            return a
        def st_isascii(self):
            try:
                logging.info("this is isascii op")
                a = self.s.isascii()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isdecimal(self):
            try:
                logging.info("this is isdecimal op")
                a = self.s.isdecimal()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isdigit(self):
            try:
                logging.info("this is isdigit op")
                a = self.s.isdigit()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isidentifier(self):
            try:
                logging.info("this is isidentifier op")
                a = self.s.isidentifier()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_islower(self):
            try:
                logging.info("this is islower op")
                a = self.s.islower()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isnumeric(self):
            try:
                logging.info("this is isnumeric op")
                a = self.s.isnumeric()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isprintable(self):
            try:
                logging.info("this is isprintable op")
                a = self.s.isprintable()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isspace(self):
            try:
                logging.info("this is ispace op")
                a = self.s.isspace()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_istitle(self):
            try:
                logging.info("this is istitle op")
                a = self.s.istitle()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_isupper(self):
            try:
                logging.info("this is isupper op")
                a = self.s.isupper()
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_startswith(self):
            try:
                logging.info("this is startswith op")
                a = self.s.startswith('u',5,7)
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_endswith(self):
            try:
                logging.info("this is endswith op")
                a = self.s.endswith('u',0,6)
            except Exception as e:
                logging.error("some error is occured", e)
            return a
        def st_expandtabs(self):
            try:
                logging.info("this is expandtabs op")
                a = self.s.expandtabs()
            except Exception as e:
                logging.error("some error is occured", e)
            return a

    except Exception as e:
        logging.error(" class is failed, need to pass string as a perameter")

strg = String_op("praTYusha")
strg1 = String_op("     Hai   Hello     ")
num = String_op("123")
strg2 = String_op("Pratyusha\t\tineuron")
logging.info(strg.st_op1())
logging.info(strg.st_op2())
logging.info(strg.st_op3())
logging.info(strg.st_op4())
logging.info(strg.st_op5())
logging.info(strg.st_op6())
logging.info(strg.st_op7())
logging.info(strg.st_op8())
logging.info(strg.st_op9())
logging.info(strg.st_op10())
logging.info(strg.st_op11())
logging.info(strg.st_op12())
logging.info(strg.st_cap())
logging.info(strg.st_swap())
logging.info(strg.st_reverse())
logging.info(strg1.st_strip())
logging.info(strg1.st_lstrip())
logging.info(strg1.st_rstrip())
logging.info(strg.st_center())
logging.info(strg.st_isalnum())
logging.info(strg.st_isalpha())
logging.info(strg.st_isascii())
logging.info(num.st_isdecimal())
logging.info(num.st_isdigit())
logging.info(num.st_isidentifier())
logging.info(num.st_islower())
logging.info(num.st_isnumeric())
logging.info(strg.st_isprintable())
logging.info(strg1.st_isspace())
logging.info(strg1.st_istitle())
logging.info(strg.st_isupper())
logging.info(strg.st_startswith())
logging.info(strg.st_endswith())
logging.info(strg2.st_expandtabs())









