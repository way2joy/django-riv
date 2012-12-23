def traverse_dict(d, keys, return_parent=False):
    if isinstance(d, dict):
        if return_parent and len(keys) == 1:
            return d
        if d.has_key(keys[0]):
            return traverse_dict(d[keys[0]], keys[1:], return_parent)
        else:
            raise KeyError("Traversing the dictionary failed on key: %s" % keys[0])
    else:
        # if "keys" is specified the user requested to further traverse
        # the dictionary. This fails so we return None. In any other
        # case we arrived and return the value. 
        if keys:
            raise KeyError("Traversing the dictionary failed on key: %s" % keys[0])
        else:
            return d

def create_tree_with_val(d, keys, val):
    if not keys:
        return
    if len(keys) == 1:
        d[keys[0]] = val
    if not d.has_key(keys[0]):
        d[keys[0]] = {}
    create_tree_with_val(d[keys[0]], keys[1:], val)
