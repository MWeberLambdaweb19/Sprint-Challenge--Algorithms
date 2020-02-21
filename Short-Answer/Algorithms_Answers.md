#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) The runtime is O(n^2):
In this snippet, `a = 0` is known as O(1), as a will _always_ be zero. So we move onto the `while` loop, and though the `while` loop is `(a < n^3)`, we skip over this. It is like O(C), as we are checking to see if `a` meets that loop requirement. What matters is the next line, `a = a + n ^ 2` (since n * n == n^2). To be explicitly clear, _for every time that `a` is less than `n^3`_, a will be set to the value of `a + n^2`. 

Since we are only looking at _that_ `for` loop, and that value is O(n^2), we can compute our Big O:
O(1) [a = 0] + (O(1) * O(n^2)) [a = a + n * n] == O(n^2), as 1 * 1 == 1 and 1 * O(n^2) is O(n^2). 


b) The runtime is O(n log n):
This range is a little more different, as we have a `while` loop inside of a `for` loop. As always, `sum = 0` will be O(1), as it is constant. We must calculate the length of time to execute that first `for` loop. As it is only looking for `range(n)`, we can assume that that line is O(n). We skip the next line since it will be constant, and we move to the `while` loop. For every time that `j < n`, we execute the function of j *= 2, which happens with logarithmic growth. So that line is O(log n). We then multiply the `for` loop by the result of the `while` loop, as the `while` loop is _nested_ within the `for` loop.

To show our results per line:
O(1) [sum = 0] + (O(n) [for i in range(n)] * O(log n) [j *= 2]) == O(n log n)


c) The runtime is O(n):
(please view `bunnies` as `n` for this problem)
This is the fastest and simplist algorithm. Our first line of code is O(1), as it will be a _constant_ check against the value `bunnies` against 0. The next line is skipped, as it will only execute once that if statement is `True`. The `return` statement outside of the if statement will be `n - 1` + 2, recursively. As it is recursive, the speed of that line will be O(n), and will continue to execute as long as `n != 0`. How large `n` is, is the sole depending factor in the length of time it takes to run this function.

To break it down line by line:
O(1) [the if statement] + O(n) [the return outside of the if statement] == O(n).

## Exercise II

There are two ways to do this, through linear and binary search. 

Linear!
I have an `n` story building, the building is called Wayside. I am dropping eggs off of floor `f`, and if the egg _does_ break, I would go _down_ a floor to check that next floor to see if the egg breaks, and I would do that until eggs stop breaking.

So, for every floor `f`, starting at the top floor, in the range of the length of `n`,  I would drop an egg until that egg breaks is `false`, starting at the highest floor.

This would look like
```
def eggs(n, f)
for f in range(-1, len(n) -1):
    if f is True:
        f -= 1
        eggs(n, f)
    else:
        return f
```
This runtime is factorial, which is O(n!), which is _very_ slow.

Binary!

With the same variables, instead of starting at the top floor, I would start in the middle of the building. When dropped, if the egg broke, I would cancel out the entire upper half of the building and would search for a new middle in the center of our current middle. I would repeat that until the egg did not break, and then I would cancel out lower half of that middle, and then I would search the upper half of that middle.

This can be confusing in words, so here's a visual example:
```
def eggs_binary(n, f)
    f = len(n) // 2 # I am using f instead of middle ## BIG O is O(1)
    cracked = False ## Skip for Big O
    while cracked is True:
        if n[f] == True:
            f == (len(n[f-1:]))
            eggs_binary(n, f)
        else: 
            f == (len(n[:f+1]))
            eggs_binary(n, f)
```

This is log(n), as we are shortening the length of `n` through the variable `f` in half.

