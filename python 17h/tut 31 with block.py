# question of the day above program will works or not.Yes or NO?
# soln:Yes.
f=open("tut 26.txt")
# print(f.readline())
f.close()
""""""
#with block lagaoge to file ko close karne ki zarrurat ni hai.
with open("tut 26.txt") as f:
    a=f.read(4)
    print(a)
    # print(f.readline())
    print(f.readlines()) #(f.readlines()) function ke baad  (a=f.read(4)) function chalega but (f.readline()) function ni.
    # print(f.readline()) #iskke hone ya na hone se koi fark ni padhega reason is in line 12.
""""""
# question of the day below program will works or not.Yes or NO?
# soln:Yes.
f=open("tut 26.txt")
# print(f.readline())
f.close()