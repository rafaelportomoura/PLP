parent(tardeli, jafe).

parent(jafe, gomer).
parent(jafe, magoge).
parent(jafe, madai).
parent(jafe, javan).
parent(jafe, tubal).
parent(jafe, meseque).
parent(jafe, tiras).
parent(gomer, asquenaz).
parent(gomer, rifate).
parent(gomer, togarma).
parent(javan, eliza).
parent(javan, tarsis).
parent(javan, quitim).
parent(javan, dodaim).
parent(cao, cuxe).
parent(cao, misraim).
parent(cao, pute).
parent(cao, canaa).
parent(cuxe, ninrode).
parent(cuxe, seba).
parent(cuxe, havila).
parent(cuxe, sabta).
parent(cuxe, raama).
parent(cuxe, sabteca).
parent(misraim, ludim).
parent(misraim, anaquim).
parent(misraim, leabim).
parent(misraim, naftum).
parent(misraim, patrusim).
parent(misraim, causulim).
parent(raama, seba).
parent(raama, deda).

/* all_son(X) :-
    parent(X,Y),
    write(X),
    nl,
    all_son(Y). */



all_ancestors(X) :-
    \+ parent(_,X),
    !.

    
    

all_ancestors(X) :- 
    parent(Y,X),
    all_ancestors(Y),
    write(Y),
    nl.
