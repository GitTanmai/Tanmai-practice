def merge_the_tools(s,k):

    i = 0
    map2, to_print = {}, ""
    while i < len(s):
        if i % k == 0 and i != 0:
            print(to_print)
            map2, to_print = {}, ""
        if s[i] not in map2.keys():
            #print(s[i])
            map2[s[i]] = 0
            to_print += s[i]
        i += 1
    print(to_print)
if __name__ == '__main__':
    string, k = input(), int(input())
    merge_the_tools(string, k)