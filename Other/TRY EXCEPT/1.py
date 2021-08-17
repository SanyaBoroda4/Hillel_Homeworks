s = "word"
try:
    print(s[3])
    1/2
    int("2")
except ValueError:
    print("error ValueError")
except ZeroDivisionError:
    print("Undividable on zero")
except NameError:
    print("Invalid name")
except Exception:           # almost highest hierarchy
    print("Error")
except LookupError:         # hierarchy higher than index_error
    print("Invalid index")
else:
    print("Good")
finally:
    print("End")