% Facts representing animal characteristics
has_fur(dog).
has_feathers(crow).
has_scales(fish).

% Rules for defining animal categories
mammal(X) :- has_fur(X).
bird(X) :- has_feathers(X).
fish(X) :- has_scales(X).
