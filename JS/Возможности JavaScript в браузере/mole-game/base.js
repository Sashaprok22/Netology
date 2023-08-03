(() => {
    let playing = true,
        activeHole = 1;

    const stop = () => playing = true,
        getHole = index => document.getElementById(`hole${index}`),
        deactivateHole = index =>
            getHole( index ).className = 'hole',
        activateHole = index =>
            getHole( index ).className = 'hole hole_has-mole',
        next = () => setTimeout(() => {
            if ( !playing ) {
                return;
            }
            deactivateHole( activeHole );
            activeHole = Math.floor( 1 + Math.random() * 9 );
            activateHole( activeHole );
            next();
        }, 800 );

    next();

    let totalHits = 0;
    let totalMisses = 0;

    const hitsSpan = document.getElementById("dead");
    const missesSpan = document.getElementById("lost");

    for (let i = 1; i <= 9; i++) {
        getHole(i).onclick = function () {
            if (this.classList.contains("hole_has-mole")) {
                totalHits++;
                if (totalHits >= 10) {
                    totalHits = 0;
                    totalMisses = 0;
                    alert("Вы победили!");
                }
            } else {
                totalMisses++;
                if (totalMisses >= 5) {
                    totalHits = 0;
                    totalMisses = 0;
                    alert("Вы проиграли!");
                }
            }

            hitsSpan.textContent = totalHits;
            missesSpan.textContent = totalMisses;
        }
    }
})();