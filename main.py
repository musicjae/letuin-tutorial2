# def myfunction(num:int):
#
#     N = len(str(num))
#     sum = 0
#     for n in range(N):  # 여기서 짧은 for 문이 들어가긴 하지만 짧은거라서 패스.
#         sum += int(str(num)[n])
#     return sum + num
#
# print(myfunction(123))



# ans = [magicfn(x) for x in range(10000)]  # 그런데 여기서 비효율성이 발생하는 것 같다.
# # 굳이 이렇게 10000번을 다 계산해야 했을까
# for i in range(10000):  # 여기서도 모든 값을 검사하기 위해 반복문을 썼다. 음.. n^2..
#
#     if i not in ans:
#         print(i)







