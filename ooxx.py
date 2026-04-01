'''
o_*ooo_  *是什么？

'''
all_comb = set()
for i in ['o', 'x', '_']:
    for j in ['o', 'x', '_']:
        for k in ['o', 'x', '_']:
            for l in ['o', 'x', '_']:
                for m in ['o', 'x', '_']:
                    for n in ['o', 'x', '_']:
                        for o in ['o', 'x', '_']:
                            all_comb.add(i+j+k+l+m+n+o)

all_known = set()

five = set()

for comb in all_comb:
    if "ooooo" in comb:
        five.add(comb)
        all_known.add(comb)

live_four = set()

for comb in all_comb:
    if comb not in all_known and "_oooo_" in comb:
        live_four.add(comb)
        all_known.add(comb)

dead_four = set()

for comb in all_comb:
    if comb not in all_known and ("oooo_" in comb or "_oooo" in comb or "oo_oo" in comb or "o_ooo" in comb or "ooo_o" in comb):
        dead_four.add(comb)
        all_known.add(comb)

live_three = set()

for comb in all_comb:
    if comb not in all_known and ("__ooo_" in comb or "_ooo__" in comb or "_oo_o_" in comb or "_o_oo_" in comb):
        live_three.add(comb)
        all_known.add(comb)

dead_three = set()

for comb in all_comb:
    if comb not in all_known and ("ooo__" in comb or "__ooo" in comb or "_ooo_" in comb or "_oo_o" in comb or "_o_oo" in comb or "o_o_o" in comb):
        dead_three.add(comb)
        all_known.add(comb)

live_two = set()

for comb in all_comb:
    if comb not in all_known and ("__oo__" in comb or "_oo___" in comb or "___oo_" in comb or
"_o_o__" in comb or "__o_o_" in comb or
"_o__o_" in comb):
        live_two.add(comb)
        all_known.add(comb)

dead_two = set()

for comb in all_comb:
    if comb not in all_known and ("oo___" in comb or "_oo__" in comb or "__oo_" in comb or "___oo" in comb or
"o_o__" in comb or "_o_o_" in comb or "__o_o" in comb or
"o__o_" in comb or "_o__o" in comb):
        dead_two.add(comb)
        all_known.add(comb)

live_one = set()

for comb in all_comb:
    if comb not in all_known and ("_o____" in comb or "__o___" in comb or "___o__" in comb or "____o_" in comb):
        live_one.add(comb)
        all_known.add(comb)

dead_one = set()

for comb in all_comb:
    if comb not in all_known and ("o____" in comb or "_o___" in comb or "__o__" in comb or "___o_" in comb or "____o" in comb):
        dead_one.add(comb)
        all_known.add(comb)

live_zero = set()

for comb in all_comb:
    if comb not in all_known and ("______" in comb):
        live_zero.add(comb)
        all_known.add(comb)

dead_zero = set()

for comb in all_comb:
    if comb not in all_known and ("_____" in comb):
        dead_zero.add(comb)
        all_known.add(comb)

blocked = set()

import re

def myin(comb, s):
    # 只要 text 里包含符合 x[o_]x 模式的内容，就返回 True
    result = bool(re.search(s, comb))
    return result

for comb in all_comb:
    if comb not in all_known and (
myin(comb, "xxx") or
myin(comb, "x[o_]x") or
myin(comb, "xx[o_]") or
myin(comb, "[o_]xx") or
myin(comb, "[o_]x[o_]") or
myin(comb, "[o_][o_]x") or
myin(comb, "x[o_][o_]") or
myin(comb, "x[o_][o_]x") or
myin(comb, "x[o_][o_][o_]x") or
myin(comb, "x[o_][o_][o_][o_]x") or
myin(comb, "x[o_][o_][o_][o_][o_]x")):
        blocked.add(comb)
        all_known.add(comb)

print(len(all_known), "/", len(all_comb))

for comb in all_comb:
    if comb not in all_known:
        print(comb)

mydict={}

for comb in all_comb:
    for i,j in enumerate(comb):
        if j == '_':
            new_comb = comb[:i] + 'o' + comb[i+1:]
            if(comb == "xoo__oo"):
                print(new_comb)
            if comb not in five and new_comb in five:
                mydict[(comb, i)] = "FIVE"
            elif comb not in live_four and new_comb in live_four:
                mydict[(comb, i)] = "LIVE_FOUR"
            elif comb not in dead_four and new_comb in dead_four:
                mydict[(comb, i)] = "DEAD_FOUR"
            elif comb not in live_three and new_comb in live_three:
                mydict[(comb, i)] = "LIVE_THREE"
            elif comb not in dead_three and new_comb in dead_three:
                mydict[(comb, i)] = "DEAD_THREE"
            elif comb not in live_two and new_comb in live_two:
                mydict[(comb, i)] = "LIVE_TWO"
            elif comb not in dead_two and new_comb in dead_two:
                mydict[(comb, i)] = "DEAD_TWO"
            elif comb not in live_one and new_comb in live_one:
                mydict[(comb, i)] = "LIVE_ONE"
            elif comb not in dead_one and new_comb in dead_one:
                mydict[(comb, i)] = "DEAD_ONE"
            elif comb not in live_zero and new_comb in live_zero:
                mydict[(comb, i)] = "LIVE_ZERO"
            elif comb not in dead_zero and new_comb in dead_zero:
                mydict[(comb, i)] = "DEAD_ZERO"
            else:
                mydict[(comb, i)] = "NOTHING"
        else:
            mydict[(comb, i)] = "INVALID"

for comb in all_comb:
    print(comb, end=' ')
    for i in range(7):
        print(mydict[(comb, i)] + ', ', end='')
    print("")