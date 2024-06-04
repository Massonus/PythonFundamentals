status_code = int(input("Enter status code from server: "))

match status_code:
    case 400:
        print("Bad request")
    case 401:
        print("Unauthorized")
    case 402:
        print("Forbidden")
    case 404:
        print("Page not found")
    case _:
        print("Other error")
