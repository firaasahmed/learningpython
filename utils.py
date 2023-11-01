class Utils:

    def maximum(listed):
        find_max=listed[0]
        for x in listed:
            if x>find_max:
                find_max=x
        return find_max

print(Utils.maximum([15,20,2,343,12,11]))
