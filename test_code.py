def square_even_numbers(numbers):
    # 짝수만 제곱한 값을 반환
    result = []
    for n in numbers:
        if n % 2 == 0:  # 짝수 확인
            result.append(n ** 2)
    return result

# 테스트
numbers = [1, 2, 3, 4]  # 리스트로 수정
print(square_even_numbers(numbers))
