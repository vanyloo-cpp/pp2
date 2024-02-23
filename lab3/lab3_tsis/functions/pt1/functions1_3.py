def solve(numheads, numlegs):
    chicken = 2*numheads - (numlegs/2)
    rat = numheads - chicken
    return chicken, rat
