"""The rgb function is incomplete. Complete it so that passing in RGB decimal values will result in a hexadecimal representation being returned. Valid decimal values for RGB are 0 - 255. Any values that fall out of that range must be rounded to the closest valid value.

Note: Your answer should always be 6 characters long, the shorthand with 3 will not work here.

Examples (input --> output):
255, 255, 255 --> "FFFFFF"
255, 255, 300 --> "FFFFFF"
0, 0, 0       --> "000000"
148, 0, 211   --> "9400D3"""

r, g, b = 13, 2, 3

if r < 0:
    r = 0
if r > 255:
    r = 255
if g < 0:
    g = 0
if g > 255:
    g = 255
if b < 0:
    b = 0
if b > 255:
    b = 255
hex_r = format(r, "x")
hex_b = format(b, "x")
hex_g = format(g, "x")

if r < 16:
    hex_r = "0" + format(r, "x")
if b < 16:
    hex_b = "0" + format(b, "x")
if g < 16:
    hex_g = "0" + format(g, "x")
if hex_r == "0":
    hex_r = "00"
if hex_b == "0":
    hex_b = "00"
if hex_g == "0":
    hex_g = "00"

for_correct = (hex_r + hex_g + hex_b).upper()
# answer = for_correct.replace("0","00")


print(for_correct)
