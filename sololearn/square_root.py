# find the square root of a number
# using the babylonian method
# https://www.google.com/url?sa=t&source=web&rct=j&url=https://www.quora.com/What-is-an-example-of-using-Babylonian-method-to-find-a-square-root-of-a-number&ved=2ahUKEwibuajjsfriAhUfRxUIHZGPAmcQjjgwAHoECAMQAQ&usg=AOvVaw376aZiZWYkE8jl3EMmBxJ4


def rt1(n):
    
    x = n
    y = 1
    e = 0.000001

    while x - y > e:
        x = (x + y) / 2
        y = n / x

    return x


def rt2(n):
    
    g = n

    while g - (n / g) > 0.000001:
        g = (g + (n / g)) / 2
        
    return g

n = 22/7

print("rt1: {} -> {}".format(n, rt1(n)))
print("rt2: {} -> {}".format(n, rt2(n)))

