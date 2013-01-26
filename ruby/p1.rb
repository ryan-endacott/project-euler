#Ruby is cool!  I didn't like it at first, but I'm warming up to it.

sum = 0

(1..999).each do |num|
    sum += num if (num % 3 == 0 || num % 5 == 0)
end
puts sum

