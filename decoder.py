def decompress(compressed):
    """Decompress a list of output ks to a string."""
    from io import StringIO

    # Build the dictionary.
    dict_size = 256
    dictionary = dict((i, chr(i)) for i in range(dict_size))
    # in Python 3: dictionary = {i: chr(i) for i in range(dict_size)}
    compressed = [int(res, 2) for res in compressed]
    # use StringIO, otherwise this becomes O(N^2)
    # due to string concatenation in a loop
    result = StringIO()
    w = chr(compressed.pop(0))
    result.write(w)
    for k in compressed:
        if k in dictionary:
            entry = dictionary[k]
        elif k == dict_size:
            entry = w + w[0]
        else:
            raise ValueError('Bad compressed k: %s' % k)
        result.write(entry)

        # Add w+entry[0] to the dictionary.
        dictionary[dict_size] = w + entry[0]
        dict_size += 1

        w = entry
    return result.getvalue()



def decompress_bwt(len_bwt, bwt, num):
    table = [""] * len_bwt  # Make empty table

    for i in range(len(bwt)):
        table = [bwt[i] + table[i] for i in range(len(bwt))]  # Add a column of r
        print('unsorted = ', table)
        table = sorted(table)
        print('sorted    =', table)

    return table[num-1]

compressed = 

num_line = 

decompressed = decompress(compressed)
print (decompressed)
print(decompress_bwt(len(decompressed), decompressed, num_line))
