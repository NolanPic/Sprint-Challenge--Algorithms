#### Please add your answers to the **_Analysis of Algorithms_** exercises here.

## Exercise I

a)
This is O(n). We have to count up to n*n*n in our loop, which might make one think this is O(n*n*n), or O(n^3). However, each iteration counts up by n*n, so you can think of n*n cancelling out two of the multiplications, and leaving us only iterating through n times instead of n^3 times.

b)
This is O(n log n). First, we loop through n, which is O(n). Then, for each iteration of n, we count up to n from one--except we double our count each time, so each iteration of n is O(log n). Therefore, it is O(n\*log(n)) or O(n log n).

c)
This is O(n). Since it recursively calls itself, but decrements n by 1 each iteration, it is just going to recurse through n and then stop.

## Exercise II

### O(n) Solution

In this solution, only one egg would be broken. However, many eggs could be dropped without being broken.

```
n = number of stories
f = current floor (start at floor 1)
broken_from_floor = unknown

while f <= n:
	drop_egg()
	if egg is broken:
		broken_from_floor = f
        break
	f = next floor up
```

The above pseudocode runs in O(n), where n is the number of stories. We move up towards n from the first floor, and thus in the very worst case we would be going all the way up to n (the top floor).

### O(log n) Solution

In this solution, more than one egg can be broken, but the number of dropped eggs could be much smaller than the O(n) solution if this is a really tall building.

```
bottom = the first floor
top = the top floor (or n)

while bottom <= top:
    # get the middle floor
    mid_floor = (bottom+top) // 2

    if egg_breaks_from_floor(mid_floor):
        # too high, go lower
        top = mid_floor-1

    else:
        # the egg did not break.
        # the floor above might be the correct floor,
        # or we could still be too low. Drop an egg
        # from one floor above THIS one

        if egg_breaks_from_floor(mid_floor+1):
            # the egg broke from the floor above, but not
            # THIS floor (mid_floor)--we found the correct floor!
            # return the floor above this one since that is
            # what we want,

            return mid_floor+1
        else:
            # we are still too low--try higher
            bottom = mid_floor+1

    return None # <-- could not find a floor from which an egg did not break


```

The above pseudocode runs in O(log n). It is basically performing a binary search, but it performs a check where if an egg is not broken on a given floor, it checks the floor above it to see if it breaks on that floor (which is itself an O(1) operation). If it breaks from the above floor, the above floor is the answer. If it doesn't, the search cuts the results in half and applies the same thing. Each iteration whittles the floors, or n, down by half.
