from .get_attribute import get_attribute as getattr


def create_property(get_attribute, set_attribute=None):

    # get function
    get = lambda self: getattr(self, get_attribute)()

    # set function
    set = None
    if set_attribute is not None:
        set = lambda self, value: getattr(self, set_attribute)(value)

    # create property
    return property(get, set)


def create_property_for_text(attribute):
    get = f'{attribute}.text'
    set = f'{attribute}.setText'
    return create_property(get, set)


def create_property_for_checked(attribute):
    get = f'{attribute}.isChecked'
    set = f'{attribute}.setChecked'
    return create_property(get, set)


def create_property_for_attribute(attribute, read_only=False):
    # get
    get = lambda self: getattr(self, attribute)

    if read_only:
        # do not need set
        return property(get)

    # set

    base_attr, name = pop_last_attribute(attribute)

    def set(self, value):
        base_obj = getattr(self, base_attr)
        setattr(base_obj, name, value)

    return property(get, set)


# helpers

def pop_last_attribute(attribute):
    attr_list = attribute.split('.')
    attr = attr_list.pop()
    base = '.'.join(attr_list)
    return base, attr
