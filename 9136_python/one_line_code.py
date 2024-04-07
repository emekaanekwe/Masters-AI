# concerns "list comprehension"

# example
# Your solution goes here
user_input = int(input())
def check_credit_card(card_num) -> list:
    # lecure
    if len(card_num) not in range(14,20) or not user_input.isdigit():
        return False
    num = 0
    card_num.pop()
    # card_num[-2::-2] to drop last and reverse
    card_num.reverse()
    #if i % 2 == 0:# wrong
    #lecture
    card_num = [num * 2 if idx % 2 == 0 else num for idx, num in enumerate(card_num)]
    #lecture
    #card_num [num- - 0 if num > 9 else num for num in card_num]
    
    
    
    
    # from greeksforgeeks
    #card_num[len(card_num)-1] += remainder
    #print(total % 10 == 0)

