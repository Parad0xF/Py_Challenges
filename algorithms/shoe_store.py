from collections import Counter

def total_money_earned(lst):
    shoes_size = lst[1].split()
    custmr_wish = []
    total = 0
    
    while("" in shoes_size):
        shoes_size.remove("")
    
    for i in range(3, len(lst)):
        custmr_wish.append(lst[i].split())
    try:    
        for i, x in custmr_wish:
            if i in shoes_size:
                shoes_size.remove(i)
                total += int(x)
    except ValueError:
        pass
    
    print(total)

if __name__ == "__main__":
    
    shoes= int(input())
    sizes=list(map(int, input().split())) 
    customers = int(input())
    total_earned=0
 
    for i in range(customers): 
     size, money= map(int, input().split()) 
     if size in sizes: 
         total_earned+=money 
         sizes.remove(size) 
         print(total_earned)
    
