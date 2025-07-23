try:
    a=int('hi')
    b=20
    c=a+b

except ValueError:

        print("value error")
except TypeError:
        print("type error")
except Exception:
        print("executed")
else:
        print("finally")
finally:
  print("exceted succesfully")