def edit_distance(str1, str2, m, n):

    if m == 0:
         return n

    if n == 0:
        return m

    if str1[m-1] == str2[n-1]:
        return edit_distance(str1, str2, m-1, n-1)

    return 1 + min(edit_distance(str1, str2, m, n-1),    # Insert
                   edit_distance(str1, str2, m-1, n),    # Remove
                   edit_distance(str1, str2, m-1, n-1)    # Replace
                   )

def main():
    str1 = input("Enter the first string: ")
    str2 = input("Enter the second string: ")

    print(edit_distance(str1, str2, len(str1), len(str2)))

if __name__ == "__main__":
    main()