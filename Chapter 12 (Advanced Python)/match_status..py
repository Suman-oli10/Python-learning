def http_status(status):
    match status:
        case 400:   
            return "Bad Request"
        case 401:   
            return "Unauthorized"
        case 403:
            return "Forbidden"
        case _:
            return "Unknown Status"
        
print(http_status(400))  # Output: Bad Request
print(http_status(401))  # Output: Unauthorized
print(http_status(403))  # Output: Forbidden
print(http_status(500))  # Output: Unknown Status