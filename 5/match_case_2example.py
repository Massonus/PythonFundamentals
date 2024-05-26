# from distutils.log import error


status_code = int(input("Enter status code from server: "))

match status_code:
    case 400:
        print("Bad request")
    case 401 | 403 as error:
        print(f'{error} is authentication error')
    case 404:
        print("Page not found")
    case _:
        print("Other error")

