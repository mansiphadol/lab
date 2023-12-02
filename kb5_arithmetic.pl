% Rules for arithmetic operations
add(X, Y, Z) :- Z is X + Y.
subtract(X, Y, Z) :- Z is X - Y.
multiply(X, Y, Z) :- Z is X * Y.
divide(X, Y, Z) :- Y \= 0, Z is X / Y.
