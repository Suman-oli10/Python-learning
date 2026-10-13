def main():
    try:
        a=int(input("Hey! Enter a number: "))
        print(a)

    except Exception as e:
        print(e)

    finally:
        print("This block will always run, whether an exception is raised or not")

main()