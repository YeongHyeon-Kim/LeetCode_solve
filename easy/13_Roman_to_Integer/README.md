## 13_Roman_to_Integer 풀이

___
### 내 풀이
```python
symbol = {"M": 1000, "D": 500, "C": 100,
                  "L": 50, "X": 10, "V": 5, "I": 1} 
````
당연히 symbol의 개수가 적고 값이 지정되어 있기 때문에 dict를 쓰는게 맞다고 생각함

```python
check = {"I": ["V", "X"], "X": ["L", "C"], "C": ["D", "M"]}
check_keys = list(check.keys())
````
특정 symbol에 대한 조건이 있기 때문에 미리 지정하여 간편하게 체크할 수 있도록 함

```python
result = 0
for ind, s_ in enumerate(s):
    if ind != len(s)-1 and s_ in check_keys and s[ind+1] in check[s_]:
        result -= symbol[s_]
    else:
        result += symbol[s_]
return result
```
마지막 인덱스가 아니고, 현재 s_값이 check의 key에 들어가 있고, 다음 값이 check[s]의 value 즉 list 안에 들어있다면 - 해주고
그 외의 모든 경우는 + 해서 결과 출력

### 인터넷 최단시간 풀이
```python
prevValue = symbolToIntDict["M"]
totalValue = 0
for c in s:
    currentValue = symbolToIntDict[c]
    if prevValue < currentValue:
        totalValue -= prevValue * 2
    totalValue += currentValue
    prevValue = currentValue
```
항상 큰 값이 앞에 오기 때문에 만약 현재값이 앞의 값보다 크다면 당연히 - 해줘야 한다는 것을 알아차리지 못함.
```python
if prevValue < currentValue:
    totalValue -= prevValue * 2
totalValue += currentValue
```
prevValue * 2 값을 빼줌으로 써 else문을 쓰지 않고 항상 현재 값을 결과에 더하는 식으로 진행함