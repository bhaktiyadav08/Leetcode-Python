digits="23"
curr=""
def letterCombinations(digits):
    ans=[]
    map=["","","abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
    def solve(index,digits,curr):
        if index==len(digits):
            ans.append(curr)
            return
        digit=int(digits[index])
        letters=map[digit]
        for i in range (len(letters)):
            solve(index+1,digits,curr+letters[i])
    if len(digits)==0:
        return ans
    solve(0,digits,curr)
    return ans
print(letterCombinations(digits))
    