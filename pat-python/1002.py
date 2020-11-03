"""A + B for Polynomials
"""
# TODO  这道题还有2分没通过，有人知道的话请留个言
from collections import Counter
def get_info(str):
    """get the exponent & coefficient 
    """
    answer_dict = {}
    list_info = str.split(" ")
    if list_info[0] == "0":
        return
    
    for (exponent, coefficient) in [list_info[1:][i:i+2] for i in range(0, len(list_info[1:]), 2)]:
        answer_dict[int(exponent)] = float(coefficient)
    
    return answer_dict

if __name__ == "__main__":
    # get input
    a = input().strip("\n")
    b = input().strip("\n")

    # analysis info 
    a_dict = get_info(a)
    b_dict = get_info(b)

    # merge two info dict
    X,Y = Counter(a_dict),Counter(b_dict)
    sum_dict = dict(Counter(X+Y))
    # if the value of coefficient is zero , do not output
    sum_dict = {k:v for k,v in sum_dict.items() if v!=0 }
    
    # output the answer
    sum_dict = sorted(sum_dict.items(),  reverse=True)
    K = len(sum_dict)

    answer = [K] + [elem for temp in sum_dict for elem in temp ]
    print(answer)
    
    