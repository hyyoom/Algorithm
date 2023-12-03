#괄호 검사

T = int(input())
for tc in range(1,T+1):
    arr = input().strip()
    
    st = []
    flag = 0
    for i in arr:
        if i == "(" or i == "{":
            st.append(i)
        elif i == ")" or i == "}":
            if len(st) == 0:
                flag = 1
                break
            else:
                tmp = st.pop()
                if tmp == "(":
                    if i != ")":
                        flag = 1
                elif tmp == "{":
                    if i != "}":
                        flag = 1
    
    if len(st) > 0 or flag == 1:
        print(f"#{tc} 0")
    else :
        print(f"#{tc} 1")
