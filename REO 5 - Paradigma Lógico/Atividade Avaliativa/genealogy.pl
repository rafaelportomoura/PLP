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

father(jafe). 
father(gomer).
father(javan).
father(cao).
father(cuxe).
father(misraim).
father(raama).

/* 

son(gomer).
son(magoge).
son(madai).
son(javan).
son(tubal).
son(meseque).
son(tiras).
son(asquenaz).
son(rifate).
son(togarma).
son(eliza).
son(tarsis).
son(quitim).
son(dodaim).
son(misraim).
son(pute).
son(canaa).
son(ninrode).
son(seba).
son(havila).
son(sabta).
son(raama).
son(sabteca).
son(ludim).
son(leabim).
son(naftum).
son(patrusim).
son(causulim).
son(deda). 



all_ancestor(X) :- 
    son(X),
    father(Y),
    parent(Y,X),
    Y \== X,
    write(Y),
    nl,
    all_ancestor(Y). */


all_ancestor(X) :- 
    parent(Y,X),
    write(Y),
    nl,
    all_ancestor(Y).
