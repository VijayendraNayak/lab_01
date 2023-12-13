def min_steps_to_palindrome(s):
    n = len(s)
    
    def is_palindrome(sub):
        return sub == sub[::-1]

    dp = [[0] * n for _ in range(n)]
    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1

            if s[i] == s[j] and length == 2:
                dp[i][j] = 0
            elif s[i] == s[j]:
                dp[i][j] = dp[i + 1][j - 1]
            else:
                dp[i][j] = min(dp[i + 1][j], dp[i][j - 1]) + 1

    return dp[0][n - 1]

# Example usage:
n=input("Enter the string:")
result = min_steps_to_palindrome(n)
print(f"Minimum number of steps to make the string palindrome: {result}")
