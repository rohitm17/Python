while True:
    try:
        n=int(input("enter your fav num n:"))
        print("20/n=")
        print(20/n)
        break
    except ValueError:
        print("make sure and print the number")
    except ZeroDivisionError:
        print("cannot divide with zero")
    except:
        break
    finally:
        print("loop completed")
