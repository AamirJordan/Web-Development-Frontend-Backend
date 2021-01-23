import name_main_one
print("TOP LEVEL TWO.PY")
name_main_one.func()

if __name__ == '__main__':
    print("two.py is being run directly")

else:
    print("two.py is imported")
