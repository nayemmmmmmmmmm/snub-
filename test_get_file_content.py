from functions.get_file_content import get_file_content

def test():
    result = get_file_content("calculator", "lorem.txt")
    print(f"lorem.txt length: {len(result)}")
    print(f"lorem.txt truncated: {'truncated' in result}")

    result = get_file_content("calculator", "main.py")
    return result

    result = get_file_content("calculator", "pkg/calculator.py")
    return result

    result = get_file_content("calculator", "/bin/cat")
    return result

    result = get_file_content("calculator", "pkg/does_not_exist.py")
    return result

if __name__ == "__main__":
    test()
