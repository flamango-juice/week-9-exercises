from math import prod
def rev_tuple(my_tuple):
    return tuple(list(reversed(my_tuple)))

def rev_tuple_v2(my_tuple):
    return my_tuple[::-1]

def rev_tuple_v3(my_tuple):
    t_list = list(my_tuple)
    if len(t_list) == 1:
        return t_list
    result = rev_tuple_v3(t_list[1:])
    result.append(my_tuple[0])
    return result

def get_a_dict(p_list,v_list):
    return dict(zip(p_list,v_list))

def get_product(*args):
    result = 1
    for p in args:
        result *= p
    return result, len(args)
def get_product_v2(*args):
    return prod(args), len(args)
if __name__ == "__main__":
    favorite_foods = ("sikwate (hot chocolate)", "puso", "shawarma", "gyros", "fried chicken", "pan de sal", "sausage", "fried calamari", "isaw (grilled chicken intestine)")
    print(rev_tuple(favorite_foods))
    print(rev_tuple_v2(favorite_foods))
    print(rev_tuple_v3(favorite_foods))
    list_a = ["a","b","c"]
    list_b = [1234] * len(list_a )
    print(get_a_dict(list_a,list_b))
    print(dict(zip(list_a,list_b)))
    to_print = get_product(2, 3, 4)
    to_print_2 = get_product_v2(2, 3, 4)
    print(to_print, to_print_2)