# 以下实例演示了狗的年龄计算判断：
age = int(input("Age of the dog: "))
print()
if age < 0:  
    print("This can hardly be true!") 
elif age == 1:  
    print("about 14 human years") 
elif age == 2:  
    print("about 22 human years") 
elif age > 2:
    human = 22 + (age -2)*5
    print("Human years: ", human)

### 
input('press Return>')