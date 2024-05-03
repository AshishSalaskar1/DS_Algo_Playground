
def check_if_possible(arr, max_pages_held, n_students):
	# check if you can distribute books among n_students such max pages held by any student is <= max_pages_held
    n = 1
    cpages = 0
    for x in arr:
        if cpages+x <= max_pages_held:
            cpages += x
        else:
            cpages = x
            n += 1
        print(f"{x} => {n},{cpages}")

    print(n)
    if n == n_students:
        return True
    
    return False



print(check_if_possible([25,46,28,49,24], 71, 4))