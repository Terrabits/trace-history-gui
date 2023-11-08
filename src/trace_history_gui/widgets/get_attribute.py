def get_attribute(obj, attribute):
    attr_list = attribute.split('.')
    return get_attribute_tail_recursive(obj, attr_list)


def get_attribute_tail_recursive(obj, attr_list):
    if not attr_list:
        # done processing attributes
        return obj

    # has next attribute?
    attr = attr_list.pop(0)
    if not hasattr(obj, attr):
        raise AttributeError(f"object '{obj}' has no attribute '{attr}'")

    # obj.attr becomes new object
    new_obj = getattr(obj, attr)

    # process remaining attributes
    return get_attribute_tail_recursive(new_obj, attr_list)
