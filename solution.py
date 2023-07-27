def edit_distance(str1, str2, m, n):

    if m == 0:
         return n

    if n == 0:
        return m