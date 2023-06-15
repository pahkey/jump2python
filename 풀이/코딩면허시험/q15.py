def chk_dup_numbers(s):
    result = []
    for num in s:
        if num not in result:
            result.append(num)
        else:
            return False
    return len(result) == 10

print(chk_dup_numbers("0123456789"))      # True 리턴
print(chk_dup_numbers("01234"))           # False 리턴
print(chk_dup_numbers("01234567890"))     # False 리턴
print(chk_dup_numbers("6789012345"))      # True 리턴
print(chk_dup_numbers("012322456789"))    # False 리턴
