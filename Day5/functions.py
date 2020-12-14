def divEtImp(string, c_low, c_high):
    i = len(string)
    if i>0:
        c = string[0]
        if c == c_low:
            lolim = 0
        elif c == c_high:
            lolim = ((2 ** len(string))/2)
        else:
            raise Exception("Letter " + c + " does not match input parameters " + c_low + " or " + c_high)

        string = string[1:len(string)]
        return lolim + divEtImp(string, c_low, c_high)
    else:
        return 0