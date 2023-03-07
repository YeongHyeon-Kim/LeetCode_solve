## 13_Roman_to_Integer 풀이

___
### 내 풀이
풀이 시간 - 약 20분
27ms

문제를 풀다보니 예외처리로 인해서 상당히 복잡해짐.

```python3
open_list = ["(", "[", "{"]
pair = {"(": ")", "{": "}", "[": "]"}
```
3가지 일일이 확인하기 귀찮? 으니까 list의 in으로 구별
알맞는 pari인지는 key-value (시간 복잡도 1)로 구별

False
- 길이가 홀수
- 시작이 close일때
- open 나오기 전에 close가 먼저 나올때
- 알맞는 close가 아닐때
- 닫히지 않고 input이 끝났을때

모두 통과하면 True


### 인터넷 최단시간 풀이 - 11ms
```python3
lst = []
if s[0] not in ['(', '[', '{']:
    return False
for bracket in s:
    if bracket in ['(', '[', '{']:
        lst.append(bracket)
    elif len(lst) == 0:
        return False                
    else:
        opening = lst.pop()
        if (opening == '(' and bracket == ')') or (opening == '[' and bracket == ']') or (opening == '{' and bracket == '}'):
            continue
        else:
            return False
if len(lst) == 0:
    return True
return False
```
나와 차이는 
```python3
if len(input_list)==0:
    return False
```
체크를 if문 하나의 밖에서 했다는 점과
dict 형태를 쓰지 않았다는점.

이게 이렇게까지 차이가 날 문제인지??