# def main():
#     print("Hello from python!")


# if __name__ == "__main__":
#     main()

# partitions
# 5 < 99    -   0 discount
# 100 < max -   20% discount

# test case values  - 50 , 500 
# boundary values   - 5 , 99 , 100
# test case values  - 5, 6,     98, 99,     100, 101    9999 , 10000
# all values - 5,6,50,98,99,100,101,9999,10000 

def discountCalculation(input):
    

    if(input <= 99 and input >= 5):
        return (0) # no discount
    
    elif(input >= 100):
        return (0.2)  # 20% discount
    
    return 0
    
    