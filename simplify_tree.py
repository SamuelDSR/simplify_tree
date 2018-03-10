from collections import defaultdict

def get_parent_with_n_more_children(path, n):
    parent_children_map = defaultdict(set)
    with open(path, "r") as f:
        for line in f:
            tokens = line.split(" > ")
            for parent, children in zip(tokens[0:-1], tokens[1:]):
                parent_children_map[parent].add(children)
    parent_with_n_more_children = set()
    for parent in parent_children_map:
        if len(parent_children_map[parent]) >= n:
            parent_with_n_more_children.add(parent)
    return parent_with_n_more_children


def takeuntil(predicate, iterable):
    """similar like itertools.takewhile, difference is that it will
    return the first occurence that predicate is false
    """
    for x in iterable:
        if predicate(x):
            yield x
        else:
            yield x
            break

def simplify_tree(input_path, output_path, n):
    """Remove the items that have more than n sibling
    """

    parent_with_n_more_children = get_parent_with_n_more_children(input_path, n)
    #print(parent_with_n_more_children)
    seen_lines = set()
    with open(input_path, "r") as input_file:
        with open(output_path, "w") as output_file:
            for line in input_file:
                line = line.strip()
                tokens = line.split(" > ")
                accepted_tokens = list(takeuntil(lambda x:
                    x not in parent_with_n_more_children, tokens))
                if accepted_tokens:
                    new_line = " > ".join(accepted_tokens)
                    if new_line not in seen_lines:
                        seen_lines.add(new_line)
                        output_file.write(new_line + "\n")


##-------------------------test case----------------------------------
simplify_tree("input.txt", "output.txt", 2)



                
