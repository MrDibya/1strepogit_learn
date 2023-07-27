while True:
    a=int(input('enter a value for a:'))
    b=int(input('enter a value for b:'))
    try:
        c=a/b
        print(c)
    except:
        print("zero is not divisiable")
        continue
        ext=0
    else:
        print('you have the value',c)
    finally:
        print("thank for using my app, visit again")
        
        
