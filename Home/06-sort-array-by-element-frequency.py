'''
Sort the given iterable so that its elements end up in the decreasing frequency order, that is, the number of times they appear in elements. 
If two elements have the same frequency, they should end up in the same order as the first appearance in the iterable.

Input: Iterable
Output: Iterable
'''
def frequency_sort(items):
    d = {}
    values = []
    
    for i in items:
        if i not in d:
            d[i] = items.count(i)       
        items = [value for value in items if value != i]
        
    sorted_d = sorted(d.items(), key=lambda kv: kv[1], reverse=True)
    
    for j in sorted_d:
        for i in range(j[1]):
            values.append(j[0])
    
    return values


if __name__ == '__main__':
    print("Example:")
    print(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4]))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert list(frequency_sort([4, 6, 2, 2, 6, 4, 4, 4])) == [4, 4, 4, 4, 6, 6, 2, 2]
    assert list(frequency_sort(['bob', 'bob', 'carl', 'alex', 'bob'])) == ['bob', 'bob', 'bob', 'carl', 'alex']
    assert list(frequency_sort([17, 99, 42])) == [17, 99, 42]
    assert list(frequency_sort([])) == []
    assert list(frequency_sort([1])) == [1]
    print("Coding complete? Click 'Check' to earn cool rewards!")