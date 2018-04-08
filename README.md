# powerful-dice

A simple, brute-force solution to a “powerful dice” problem. 

## background

I found this video from Numberphile on HackerNews: “[The Most Powerful Dice](https://www.youtube.com/watch?v=zzKGnuvX6IQ).”

This video breaks down ways of organizing numbers on dice so that, when rolled against each other, the expected “wins” can be compared.

However, I take issue with the way that these dice are built.  Take a normal d6; the sum of its faces is:

`1 + 2 + 3 + 4 + 5 + 6 = 21`

However, [two of the examples we are shown](https://youtu.be/zzKGnuvX6IQ?t=1m25s) seem to assign the total amount possible in an unpredictable way:

`3 + 3 + 3 + 3 + 3 + 3 = 18`

`4 + 4 + 4 + 4 + 0 + 0 = 16`

Thus I made the arbitrary decision to only permit dice whose sums add up to 21. 

## implementation

The script here will iterate over all possible dice with faces from 0 to 6, evaluate whether or not the sum of that die is 21, and avoid duplicates.

Then each die is played against all dice in the set a number of times.  The die with the most “wins” — that is, where the resulting number is higher than its opponent’s result — gains one point.  

## results

The results here are inconclusive.  As demonstrated in the results file, there are two dice that emerge as the frontrunners, yet the difference between the two of them (.4% in the 50000 tries run) is not large enough to dismiss the randomness of the results.

```[0, 0, 5, 5, 5, 6], 1194435 wins
[0, 0, 3, 6, 6, 6], 1195087 wins```

It also could very well be that the random number generator built into the `random` module gives an edge to some dice over others!

## future implementations

In the future, I’m considering permitting each face to go up to 21; I’ll also modify the code to use a more reliable random number generator (though this would likely significantly slow down the script).  I would also like to expand my knowledge of mathematics to be able to determine, for certain, which die will have the highest probability of winning.
