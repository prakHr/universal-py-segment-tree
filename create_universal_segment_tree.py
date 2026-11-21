# python >= 3.12

from segee import GenericSegmentTree
def gcd(a,b):
    if a==0:
        return b
    if b==0:
        return a
    if a<b:
        a,b = b,a
    return gcd(b,a%b)

def create_tree(list_of_values, fn_type):
    def generic_function(a,b):
        if fn_type=="sum":
            return a+b
        elif fn_type=="gcd":
            def gcd(a,b):
                if a==0:
                    return b
                if b==0:
                    return a
                if a<b:
                    a,b = b,a
                return gcd(b,a%b)
            return gcd(a,b)
        elif fn_type=="max":
            return max(a,b)
        elif fn_type=="min":
            return min(a,b)
        elif fn_type=="str":
            return str(a)+str(b)
        elif fn_type=="xor":
            return a^b

    if fn_type=="sum":
        initial_state = 0
    elif fn_type=="gcd":
        initial_state = 0
    elif fn_type=="max":
        initial_state = min(list_of_values)
    elif fn_type=="min":
        initial_state = max(list_of_values)
    elif fn_type=="str":
        initial_state = ""
    elif fn_type=="xor":
        initial_state = 0
    elif fn_type=="evenIndexOddIndexAlternatingDiff":
        initial_state = 0
    else:
        return 'Use from this list of fn types:- ["sum","gcd","max","min","str","xor","evenIndexOddIndexAlternatingDiff"]'


    l = len(list_of_values)
    tree = GenericSegmentTree(size = l, identity = initial_state, operation = generic_function)
    i = 0
    for value in list_of_values:
        tree.set(i,value)
        i+=1
    return tree

def update_tree(tree, index, value_at_index):
    if tree == 'Use from this list of fn types:- ["sum","gcd","max","min","str","xor","evenIndexOddIndexAlternatingDiff"]':
        return tree
    tree.set(index,value_at_index)
    return tree

def get_range_update_in_the_tree(tree, fn_type, start_index, end_index):

    if tree == 'Use from this list of fn types:- ["sum","gcd","max","min","str","xor","evenIndexOddIndexAlternatingDiff"]':
        return tree
    if fn_type == "gcd":
        rv = 0
        list_of_a_tree = list(tree)
        for idx in range(start_index,end_index+1):
            rv = gcd(rv,list_of_a_tree[idx])
        return rv
    elif fn_type == "str":
        rv = ""
        list_of_a_tree = list(tree)
        for idx in range(start_index,end_index+1):
            rv += str(list_of_a_tree[idx])
        return rv
    elif fn_type == "xor":
        rv = 0
        list_of_a_tree = list(tree)
        for idx in range(start_index,end_index+1):
            rv ^= list_of_a_tree[idx]
        return rv
    elif fn_type == "evenIndexOddIndexAlternatingDiff":
        rv = 0
        list_of_a_tree = list(tree)
        for idx in range(start_index,end_index+1):
            if idx%2==0:
                rv += list_of_a_tree[idx]
            else:
                rv -= list_of_a_tree[idx]
        return rv
    else:
        string = f"{fn_type}({list(tree)}[{start_index}:{end_index+1}])"
        rv = eval(string)
        return rv

if __name__=="__main__":
    list_of_values = [1,1,1,1,1]
    fn_type = "xor"
    tree = create_tree(list_of_values,fn_type)
    print(tree)

    index = 0
    value_at_index = 10
    tree = update_tree(tree,index,value_at_index)
    print(tree)

    start_index = len(list_of_values)-2
    end_index = len(list_of_values)-1
    rv = get_range_update_in_the_tree(tree,fn_type,start_index,end_index)
    print(rv)
