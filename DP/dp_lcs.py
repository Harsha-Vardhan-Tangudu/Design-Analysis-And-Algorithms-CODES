# Function to find the Longest Common Subsequence (LCS)
def lcs_algo(S1, S2, m, n):
    # Initialize a matrix to store the lengths of LCS of substrings
    L = [[0 for x in range(n + 1)] for x in range(m + 1)]

    # Building the matrix in a bottom-up way
    for i in range(m + 1):
        for j in range(n + 1):
            # Base case: if either of the strings is empty, LCS is 0
            if i == 0 or j == 0:
                L[i][j] = 0

            # If characters match, extend the LCS by 1
            elif S1[i - 1] == S2[j - 1]:
                L[i][j] = L[i - 1][j - 1] + 1
                
            # If characters do not match, take the maximum of LCS without one character
            else:
                L[i][j] = max(L[i - 1][j], L[i][j - 1])

    # Length of the Longest Common Subsequence
    index = L[m][n]

    # Initialize an array to store the LCS
    lcs_algo = [""] * (index + 1)
    lcs_algo[index] = ""

    i = m
    j = n

    # Reconstruct the LCS from the matrix
    while i > 0 and j > 0:
        if S1[i - 1] == S2[j - 1]:
            # If characters match, add the character to the LCS
            lcs_algo[index - 1] = S1[i - 1]
            i -= 1
            j -= 1
            index -= 1
        elif L[i - 1][j] > L[i][j - 1]:
            # If the value above is greater, move upwards
            i -= 1
        else:
            # If the value on the left is greater, move leftwards
            j -= 1

    # Printing the input sequences and the Longest Common Subsequence
    print("S1 : " + S1 + "\nS2 : " + S2)
    print("LCS: " + "".join(lcs_algo))


# Example usage
S1 = "ACADB"
S2 = "CBDA"
m = len(S1)
n = len(S2)
lcs_algo(S1, S2, m, n)