""" ハジメの一歩会
* Copyright (c) 2022, Tech Lovers. All rights reserved
* Project Name    : 2022.10.10の宿題
* contents        : https://twitter.com/_0447222690292/status/1579473831831691264
* Creation Date   : 2022.10.10
* Programming language used: Python
* Author          : DEmodoriGatsuO https://github.com/DEmodoriGatsuO
* Twitter         : https://twitter.com/DemodoriGatsuo Follow Me!
* Sorry           : I like English. But I can't use English.

"""

def main():
    school_year = [1,2,3]
    school_A =[[30,28,29],[28,28,30],[31,30,30]]
    school_B =[[34,33],[35,35,36],[38,37,37]]
    school_C =[[32,31,32],[35,34,35],[38,39]]

    for year, sum_A, sum_B, sum_C in zip(school_year,school_A,school_B,school_C):
        result_str = str(year) + "年\t"\
                    + " A中学校\t" + str(sum(sum_A)) + "\t"\
                    + " B中学校\t" + str(sum(sum_B)) + "\t"\
                    + " C中学校\t" + str(sum(sum_C))
        print(result_str)
    return

if __name__ == "__main__":
    main()
