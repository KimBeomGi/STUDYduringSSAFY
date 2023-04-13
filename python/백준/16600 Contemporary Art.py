# 문제
# At the Van Abbemuseum of modern and contemporary art in Eindhoven, we always look to present our muses in the most interesting way possible. Sometimes we have our work cut out for us.

# Today we are exploring whether we can modify one of our perfectly-square picture frames (such as the one shown in Figure C.1) to include an electrical filament. The purpose of this filament is so that the image can set itself alight at some opportune and hilarious moment—for example, in the middle of a sale by auction.

# You will be responsible for buying the filament to run around the entire perimeter of the artwork. How many centimetres will you need to obtain?

# 입력
# The input consists of:

# One line with an integer a (1 ≤ a ≤ 1018), the area of the image in square centimetres.
# 출력
# Output the total length of filament needed for the frame, in centimetres. Your answer should have an absolute or relative error of at most 10−6.


N = int(input())
value = N**(0.5)
print(round(value*4,8))