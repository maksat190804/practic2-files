# a = 6 
# a **= 2
# print(a)

# a = 8 <= 10 and 9 <= 10
# print(a)

# a = 11 > 10 or 2 < 1
# print(a)
# a = 10
# a = not()
# print(a)

# pets = ['dog', 'cat', 'ferret']

# 'cat' in pets 
# print(pets)

# a = 10
# print(a is not "maks")
# a = 10
# b = 10
# print(a is not b)

# class Solution(object):
#     def merge_two_sorted_arrays(A: list[int], m: int, B: list[int], n: int) -> None:
#         a, b, write_index = m-1, n-1, m + n - 1

#         while b >= 0:
#            if a >= 0 and A[a] > B[b]:
#               A[write_index] = A[a]
#               a -= 1
#            else:
#               A[write_index] = B[b]
#               b -= 1

#               write_index -= 1
            
# tom = Solution()
# tom.merge_two_sorted_arrays()

rock = []
country = []

def collect_songs():
    song = "Укажите песню."
    ask = "Введите р (рок) или к (кантри) . Введите X для выхода: "

    while True:
        genre = input(ask)
        if genre == "X":
            break
        if genre == "р":
            rk = input(song)
            rock.append(rk)

        elif genre == ("к"):
            country == input(song)
            country.append(country)
        else:
            print("Неверно")
        print(rock)
        print(country)
collect_songs()