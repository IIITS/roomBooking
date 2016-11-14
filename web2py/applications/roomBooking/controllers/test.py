from gluon.validators import is_empty
from gluon.validators import Validator


class IS_NOT_EMPTY_IF_OTHER(Validator):

    def __init__(self, other,
                 error_message='must be filled because other value '
                               'is present'):
        self.other = other
        self.error_message = error_message

    def __call__(self, value):
        if isinstance(self.other, (list, tuple)):
            others = self.other
        else:
            others = [self.other]

        has_other = False
        for other in others:
            other, empty = is_empty(other)
            if not empty:
                has_other = True
                break
        value, empty = is_empty(value)
        if empty and has_other:
            return (value, T(self.error_message))
        else:
            return (value, None)
