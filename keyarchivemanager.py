class kam:

    def knm(key):
        key = str(key)
        key = '[' + key + ']'
        return key

    def conknmint(key):
        unwanted = '[]'
        for x in unwanted:
            key = key.replace(x, "")
        key = int(key)
        return key
