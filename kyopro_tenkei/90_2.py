# コメントアウトのソースコードだとTLEになる
# def judge(target):
#     dep = 0
#     for i in range(len(target)):
#         if target[i] == "(":
#             dep += 1
#         if target[i] == ")":
#             dep -= 1
#         if dep < 0:
#             return False
#     if dep == 0:
#         return True
#     return False

# if __name__ == "__main__":
#     N = int(input())
#     if (N % 2 == 0):
#         # 規定の数だけビット演算を行う
#         for i in range(1 << N):
#             candidate = ""
#             # ビット演算で"("か")"を足す
#             for j in range(N-1, -1, -1):
#                 if (i & (1<<j)) == 0:
#                     candidate += "("
#                 else:
#                     candidate += ")"
#             if judge(candidate) == True:
#                 print(candidate)
def br(a,b,s):
  if a:
    br(a-1,b,s+"(")
  if a<b:
    br(a,b-1,s+")")
  if a+b==0:
    print(s)
n=int(input())
if n&1==0:
  br(n//2,n//2,"")