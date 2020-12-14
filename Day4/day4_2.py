import numpy as np

passport_type = np.dtype([('byr','U10'),('iyr','U10'),('eyr','U10'),('hgt','U10'),('hcl','U10'),('ecl','U10'),('pid','U10'),('cid','U10')])

field = ['byr','iyr','eyr','hgt','hcl','ecl','pid','cid']
ecls = ['amb','blu','brn','gry','grn','hzl','oth']

with open ("Day4/input.txt") as f: 
    input = f.readlines()

passport = []
tmp_passport = ""
tmp_val = 0
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
            
            if f == 'byr':
                if len(passport_test[i][f]) == 4 and int(passport_test[i][f]) >= 1920 and int(passport_test[i][f]) <= 2002:
                    tmp_val += 1
                continue
            if f == 'iyr':
                if len(passport_test[i][f]) == 4 and int(passport_test[i][f]) >= 2010 and int(passport_test[i][f]) <= 2020:
                    tmp_val += 1
                continue
            if f == 'eyr':
                if len(passport_test[i][f]) == 4 and int(passport_test[i][f]) >= 2020 and int(passport_test[i][f]) <= 2030  :
                    tmp_val += 1
                continue
            if f == 'hgt':
                x = passport_test[i][f].find('in')
                y = passport_test[i][f].find('cm')
                if x != -1 and int(passport_test[i][f][0:x]) >= 59 and int(passport_test[i][f][0:x]) <= 76:
                    tmp_val += 1
                    continue
                if y != -1 and int(passport_test[i][f][0:y]) >= 150 and int(passport_test[i][f][0:y]) <= 193:
                    tmp_val += 1
                    continue
                continue
            if f == 'hcl':
                if len(passport_test[i][f]) == 7 and passport_test[i][f][0] == '#':
                    if int(passport_test[i][f][1:6],16) >= 0 and int(passport_test[i][f][1:6],16) <= 16777215:
                        tmp_val += 1
                continue
            if f == 'ecl':
                if passport_test[i][f] in ecls:
                    tmp_val += 1
                continue
            if f == 'pid':
                if len(passport_test[i][f]) == 9 and int(passport_test[i][f]) >= 0:
                    tmp_val += 1
                continue

        except:
            if f != 'cid':
                invalid = 1
    if invalid or tmp_val < 7:
        invalid = 0
    else:
        valid += 1

    tmp_val = 0
        
print('Number of valid passports: ' + str(valid))        
            

