
# -*- coding: UTF-8 -*-

'''
時間複雜度議題:

1.試著讓自己用幾句話回答什麼是時間複雜度。
時間複雜度是用來判斷程式效能的一個觀點，另一個相對的判斷觀點是空間複雜度。
而在時間複雜度方面，主要去看在最壞的狀況下，程式需要做多少的操作，來判斷這個演算法(也就是這個程式的操作流程)的好壞，白話來說這個概念有一個溝通記號為Big O。
再來，Big O主要是看，當處理的資料非常大量的時候，這個程式需要操作的次數的成長趨勢，當資料量非常大時，常數的影響力就微乎其微，可以被化簡掉，這些也呈現在我接下來的分析中。

2.分析一下你自己寫的程式，每一題解法的時間複雜度若以 Big-O Notation 來表達，時間複雜度是？
(1).作業第一題
Python:迴圈走的次數n次，n為(max-min+1)/step。每一次迴圈中主要做三個動作:1.x加上step, 2.sum+x, 3.把sum+x的值存到sum中。而迴圈外做了一個賦值和一個印訊息的動作。
因此程式的主要操作次數總共2+3*n，為O(2+3n)=O(3n)=O(n)，因為當n為一個超大數目時，2就顯得沒甚麼影響力，因此可以去掉。而3n與n的成長趨勢是一樣的，所以可以把3也簡化掉。
Javascript:迴圈走的次數n次，n為(max-min+1)/step。每一次迴圈中主要做三個動作:1.x加上step, 2.sum+x, 3.把sum+x的值存到sum中。而迴圈外做了一個賦值和一個印訊息的動作。
因此程式的主要操作次數總共2+3*n，為O(2+3n)=O(3n)=O(n)，因為當n為一個超大數目時，2就顯得沒甚麼影響力，因此可以去掉。而3n與n的成長趨勢是一樣的，所以可以把3也簡化掉。

(2).作業第二題
Python:迴圈外面主要做了三個賦值的動作、一個判斷的動作和兩個印訊息的動作。。而迴圈走的次數n次，n為(amountEmployees-1-min+1)/1。每一次迴圈中主要做6個動作，比如加法、if判斷、把值設定到變數中的這些動作。
因此程式的主要操作次數總共6+6*n，為O(6+6n)=O(6n)=O(n)，因為當n為一個超大數目時，6就顯得沒甚麼影響力，因此可以去掉。而6n與n的成長趨勢是一樣的，所以可以把6也簡化掉。
Javascript:迴圈外面主要做了三個賦值的動作、一個判斷的動作和兩個印訊息的動作。
而迴圈走的次數n次，n為(amountEmployees-1-0+1)/1。每一次迴圈中主要做6個動作，比如加法、if判斷、把值設定到變數中的這些動作。
因此程式的主要操作次數總共6+6*n，為O(6+6n)=O(6n)=O(n)，因為當n為一個超大數目時，6就顯得沒甚麼影響力，因此可以去掉。而6n與n的成長趨勢是一樣的，所以可以把6也簡化掉。

(3).作業第三題
Python:主要做的動作是a+(num1*num2)，一個乘法和加法動作，再加上印訊息的動作，因此O(3)=O(1)，常數時間所以可以看成O(1)。
Javascript:主要做的動作是a+(num1*num2)，一個乘法和加法動作，再加上印訊息的動作，因此O(3)=O(1)，常數時間所以可以看成O(1)。

(4).作業第四題
Python:外層迴圈走的次數n次，n為(len(nums)-1-1-0+1)/1。內層迴圈走的次數m次，m為(len(nums)-1-(idx1+1)+1)/1，內層迴圈內主要做了4個動作，其中包括賦值、乘法、判斷。
所以到此為止的動作計算為n*4m。
迴圈外主要有5個動作，其中包括賦值、乘法、判斷、印訊息。
因此總共的動作評估有5+n*4m，O(5+n*4m)=O(n*4m)=O(n*m)，因為當n和m為超大數目時，5這個常數就顯得沒甚麼影響力，因此可以去掉。而4m與m的成長趨勢是一樣的，所以可以把4也簡化掉。
Javascript:迴圈外主要有5個動作，其中包括賦值、乘法、判斷、印訊息。
外層迴圈走的次數n次，n為(nums.length-1-1-0+1)/1。內層迴圈走的次數m次，m為(nums.length-1-(idx1+1)+1)/1，內層迴圈內主要做了4個動作，其中包括賦值、乘法、判斷。
因此總共的動作評估有5+n*4m，O(5+n*4m)=O(n*4m)=O(n*m)，因為當n和m為超大數目時，5這個常數就顯得沒甚麼影響力，因此可以去掉。而4m與m的成長趨勢是一樣的，所以可以把4也簡化掉。

(5).作業第五題
Python:外層迴圈走的次數n次，n為(len(nums)-1-1-0+1)/1。內層迴圈走的次數m次，m為(len(nums)-1-(idx1+1)+1)/1，內層迴圈內主要做了4個動作，其中包括加法、if判斷、回傳值。
所以到此為止的動作計算為n*4m。
因此總共的動作評估有n*4m，O(n*4m)=O(n*m)，因為2m與m的成長趨勢是一樣的，所以可以把4也簡化掉。
Javascript:外層迴圈走的次數n次，n為(nums.length-1-1-0+1)/1。內層迴圈走的次數m次，m為(nums.length-1-(idx1+1)+1)/1，內層迴圈內主要做了4個動作，其中包括加法、if判斷、回傳值。
所以到此為止的動作計算為n*2m。
因此總共的動作評估有n*4m，O(n*4m)=O(n*m)，因為2m與m的成長趨勢是一樣的，所以可以把4也簡化掉。

(6).作業第六題
Python:先分析迴圈外主要有3個賦值動作和1個印訊息的動作。
再來分析第一個迴圈走的次數n次，n為(len(nums)-1-0+1)/1，迴圈內主要做了9個動作，其中包括賦值、減法、加法、if判斷、呼叫函數，因此這一個迴圈主要做了9n個動作。
接著分析第二個迴圈走的次數m次，m為(len(maxLength)-1-0+1)/1，迴圈內主要做了2個動作，其中包括賦值、if判斷，因此這一個迴圈主要做了2m個動作。
因此總共的動作評估有4+9n+2m，O(4+9n+2m)=O(9n+2m)=O(n+m)，，因為當n和m為超大數目時，4這個常數就顯得沒甚麼影響力，因此可以去掉。而9n與n的成長趨勢是一樣的，所以可以把n也簡化掉，2m化簡為m也是同樣理由。
Javascript:先分析迴圈外主要有3個賦值動作和1個印訊息的動作。
再來分析第一個迴圈走的次數n次，n為(nums.length-1-0+1)/1，迴圈內主要做了9個動作，其中包括賦值、減法、加法、if判斷、呼叫函數，因此這一個迴圈主要做了9n個動作。
接著分析第二個迴圈走的次數m次，m為(maxLength.length-1-0+1)/1，迴圈內主要做了2個動作，其中包括賦值、if判斷，因此這一個迴圈主要做了2m個動作。
因此總共的動作評估有4+9n+2m，O(4+9n+2m)=O(9n+2m)=O(n+m)，，因為當n和m為超大數目時，4這個常數就顯得沒甚麼影響力，因此可以去掉。而9n與n的成長趨勢是一樣的，所以可以把n也簡化掉，2m化簡為m也是同樣理由。

'''

'''
要求一：函式與流程控制
完成以下函式，在函式中使用迴圈計算最小值到最大值之間，固定間隔的整數總和。其中你可
以假設 max 一定大於 min 且為整數，step 為正整數。
'''
def calculate(min, max, step):
    # 請用你的程式補完這個函式的區塊
    sum=0
    for x in range(min,max+1,step):
        sum=sum+x
        
    print(sum)

calculate(1, 3, 1) # 你的程式要能夠計算 1+2+3，最後印出 6
calculate(4, 8, 2) # 你的程式要能夠計算 4+6+8，最後印出 18
calculate(-1, 2, 2) # 你的程式要能夠計算 -1+1，最後印出 0

#============================================================
'''
要求二: Python 字典與列表、JavaScript 物件與陣列
完成以下函式，正確計算出非 manager 的員工平均薪資，所謂非 manager 就是在資料中
manager 欄位標註為 False (Python) 或 false (JavaScript) 的員工，程式需考慮員工資料數量
不定的情況。
'''

def avg(data):
    # 請用你的程式補完這個函式的區塊
    amountEmployees=len(data["employees"])
    sumSalary=0
    numberOfNonManager=0
    for idx in range(0,amountEmployees,1):
        if data["employees"][idx]["manager"]==False:
            numberOfNonManager=numberOfNonManager+1
            sumSalary=sumSalary+data["employees"][idx]["salary"]
    if numberOfNonManager==0:
        print("Maybe somthing is wrong.")
    else:
        print(sumSalary/numberOfNonManager)

avg({
        "employees":[
            {
                "name":"John",
                "salary":30000,
                "manager":False
            },
            {
                "name":"Bob",
                "salary":60000,
                "manager":True
            },
            {
                "name":"Jenny",
                "salary":50000,
                "manager":False
            },
            {
                "name":"Tony",
                "salary":40000,
                "manager":False
            }
        ]
    }
) # 呼叫 avg 函式

#============================================================
'''
要求三：完成以下函式，最後能印出程式中註解所描述的結果。
'''
def func(a):
    # 請用你的程式補完這個函式的區塊
    def multiply(num1,num2):
        print(a+(num1*num2))
    return multiply

func(2)(3, 4) # 你補完的函式能印出 2+(3*4) 的結果 14
func(5)(1, -5) # 你補完的函式能印出 5+(1*-5) 的結果 0
func(-3)(2, 9) # 你補完的函式能印出 -3+(2*9) 的結果 15
# 一般形式為 func(a)(b, c) 要印出 a+(b*c) 的結果

#============================================================
'''
要求四：找出至少包含兩筆整數的列表 (Python) 或陣列 (JavaScript) 中，兩兩數字相乘後的最大值。
'''

def maxProduct(nums):
    # 請用你的程式補完這個函式的區塊
    max=0
    if len(nums)==2:
        max=nums[0]*nums[1]
    else:
        for idx1 in range(0,len(nums)-1):
            for idx2 in range(idx1+1,len(nums)):
                multipyResult=nums[idx1]*nums[idx2]
                if multipyResult>max:
                    max=multipyResult
    print(max)

maxProduct([5, 20, 2, 6]) # 得到 120
maxProduct([10, -20, 0, 3]) # 得到 30
maxProduct([10, -20, 0, -3]) # 得到 60
maxProduct([-1, 2]) # 得到 -2
maxProduct([-1, 0, 2]) # 得到 0
maxProduct([5,-1, -2, 0]) # 得到 2
maxProduct([-5, -2]) # 得到 10
#============================================================
'''
要求五: Given an array of integers, show indices of the two numbers such that they add up to a
specific target. You can assume that each input would have exactly one solution, and you
can not use the same element twice.
'''
def twoSum(nums, target):
    # your code here
    for idx1 in range(0,len(nums)-1):
        for idx2 in range(idx1+1,len(nums)):
            if nums[idx1]+nums[idx2]==target:
                return [idx1,idx2]
result=twoSum([2, 11, 7, 15], 9)
print(result) # show [0, 2] because nums[0]+nums[2] is 9

#============================================================
'''
要求六 (Optional):
給定只會包含 0 或 1 兩種數字的列表 (Python) 或陣列 (JavaScript)，計算連續出現 0 的最大
長度。
'''

def maxZeros(nums):
    # 請用你的程式補完這個函式的區塊
    maxLength=[]
    zeroLength=0
    for idx in range(0,len(nums)):
        if nums[idx]==1:
            maxLength.append(zeroLength)
            zeroLength=0
        elif nums[idx]==0:
            zeroLength=zeroLength+1
            if idx==len(nums)-1:
                maxLength.append(zeroLength)
    max=0
    for idx in range(0,len(maxLength)):
        if maxLength[idx]>max:
            max=maxLength[idx]
    print (max)
     
maxZeros([0, 1, 0, 0]) # 得到 2
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0]) # 得到 4
maxZeros([1, 1, 1, 1, 1]) # 得到 0
maxZeros([0, 0, 0, 1, 1]) # 得到 3