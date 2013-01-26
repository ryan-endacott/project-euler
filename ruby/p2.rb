
def doIterFib(max)
    num1 = 0
    num2 = 1
    total = 0
    while num2 < max
        temp = num2
        num2 = num2 + num1
        num1 = temp
        if num2 % 2 == 0
            total += num2
        end
    end
    return total
end

print doIterFib(4000000)

