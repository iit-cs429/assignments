## Assignment 0: Indexing (50 points) 
*Expected time: 4-6 hours*



1. Get started with git and python by following the instructions at [Setup.md](Setup.md)

2. Complete the coding part of the homework by completing `boolean_search.py`.
  - Once again, you will edit the copy of `boolean_search.py` in *your* private repository under assignment0.
  - Be sure to push your modifications to GitHub.
  - Check that all tests pass and that the output matches the expected output.
    - The code has [doctests](http://docs.python.org/2/library/doctest.html), which you can run with `python -m doctest boolean_search.py -v`
	- These tests are not comprehensive. Passing these doctests does not ensure full credit!

3. For help submitting, see the checklist [here](../README.md).


The expected output of running the tests is:

```
python -m doctest boolean_search.py -v

Trying:
    index = create_index([['a', 'b'], ['a', 'c']])
Expecting nothing
ok
Trying:
    sorted(index.keys())
Expecting:
    ['a', 'b', 'c']
ok
Trying:
    index['a']
Expecting:
    [0, 1]
ok
Trying:
    index['b']
Expecting:
    [0]
ok
Trying:
    index['c']
Expecting:
    [1]
ok
Trying:
    intersect([1, 3, 5], [3, 4, 5, 10])
Expecting:
    [3, 5]
ok
Trying:
    intersect([1, 2], [3, 4])
Expecting:
    []
ok
Trying:
    search({'a': [0, 1], 'b': [1, 2, 3], 'c': [4]}, 'a b')
Expecting:
    [1]
ok
Trying:
    sort_by_num_postings(['a', 'b', 'c'], {'a': [0, 1], 'b': [1, 2, 3], 'c': [4]})
Expecting:
    ['c', 'a', 'b']
ok
Trying:
    tokenize("Hi  there. What's going on?")
Expecting:
    ['hi', 'there', 'what', 's', 'going', 'on']
ok
2 items had no tests:
    boolean_search
    boolean_search.main
5 items passed all tests:
   5 tests in boolean_search.create_index
   2 tests in boolean_search.intersect
   1 tests in boolean_search.search
   1 tests in boolean_search.sort_by_num_postings
   1 tests in boolean_search.tokenize
10 tests in 7 items.
10 passed and 0 failed.
Test passed.
```

The expected output of running the script on the provided data is:
```
python boolean_search.py



QUERY:lion

RESULTS:
How do you keep a lion from charging?     Take away its credit cards.



QUERY:What has

RESULTS:
What has four legs and goes booo?     A cow with a cold

What has 10 letters and starts with gas?     An automobile.



QUERY:why because

RESULTS:
Why did the elephant decide not to move?     Because he couldn't lift his trunk.

Why did the strawberry cross the road?     Because his mother was in a jam.

Why is the little duck always so sad?     Because he always sees a bill in front of his face.

Why did they bury the battery?     Because it was dead.

Why don't lobsters share?     Because they are shellfish.

Why does the man wish he could be a guitar player in a room full of beautiful girls?     Because if he was a guitar player, he would have his pick!

Why did the ghost float across the road?     Because he couldn't walk.



QUERY:why because HE

RESULTS:
Why did the elephant decide not to move?     Because he couldn't lift his trunk.

Why is the little duck always so sad?     Because he always sees a bill in front of his face.

Why does the man wish he could be a guitar player in a room full of beautiful girls?     Because if he was a guitar player, he would have his pick!

Why did the ghost float across the road?     Because he couldn't walk.

```
