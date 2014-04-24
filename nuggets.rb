a, b, c, streak = 0, 0, 0, 0 # Three variables & a streak counter
saved_ns = [] # This holds the values of n that do not have a solution

for n in 1..50
  # Iterate each n, presume there's no solution
  solution_exists = false
  for a in 0..(n/6 + 1)
    for b in 0..(n/9 + 1)
      for c in 0..(n/20 + 1)
        # If there is, mark it; don't worry about streak yet.
        solution_exists = true if (6*a + 9*b + 20*c == n)
      end
    end
  end
  # Now we've covered all values of a, b, and c.
  if solution_exists
    streak += 1
  else
    streak = 0
    saved_ns << n
  end
  print "Largest number of nuggets that cannot be bought in exact quantity: #{saved_ns.last}\n" if streak == 6
end