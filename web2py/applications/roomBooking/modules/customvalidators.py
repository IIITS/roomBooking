from gluon.validators import is_empty
from gluon.validators import Validator


class IS_IIITS(Validator):
        def __init__(self, mail_addr, error_message="Invalid Domain"):
            self.mail_addr = mail_addr
            self.error_message = error_message

        def __call__(self, value):
            error = None
            value = value.strip()
            print value,"aaaaa"
            if  value.endswith("iiits.in"):
                print "abcdefg"
                return (value, None)

            else:
                print "qqqqq"
                error = self.error_message
                return (value, error)
