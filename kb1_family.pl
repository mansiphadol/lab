% Facts representing parent-child relationships
parent(john, mary).
parent(john, bob).
parent(jane, mary).
parent(jane, bob).

% Rules for defining sibling relationships
sibling(X, Y) :- parent(P, X), parent(P, Y), X \= Y.
% X\=Y checks that X and Y should not be equal.

% Rules for defining grandparent relationships
grandparent(X, Y) :- parent(X, Z), parent(Z, Y).
%means y is grandparent of x if X is parent of Z and z is parent of Y.
