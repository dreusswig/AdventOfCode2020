import numpy as np

passport_type = np.dtype([('byr','U10'),('iyr','U10'),('eyr','U10'),('hgt','U10'),('hcl','U10'),('ecl','U10'),('pid','U10'),('cid','U10')])

field = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']

with open ("Day4/input.txt") as f: 
    input = f.readlines()

passport = []
tmp_passport = ""
valid = 0
invalid = 0

for i, line in enumerate(input):
    if len(line) <= 1:
        passport.append(tmp_passport.split(":"))
        tmp_passport = ""
    else:
        tmp_passport = tmp_passport + line.replace("\n", " ").replace(" ", ":")

passport.append(tmp_passport.split(":"))



passport_test = np.zeros(len(passport),dtype=passport_type)

for i, num in enumerate(passport):
    for f in field:
        try:
            passport_test[i][f] = passport[i][passport[i].index(f)+1]
        except:
            if f != 'cid':
                invalid = 1
    if invalid:
        invalid = 0
    else:
        valid += 1
        
print('Number of valid passports: ' + str(valid))        
            


