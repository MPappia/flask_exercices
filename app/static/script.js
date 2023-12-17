document.addEventListener('DOMContentLoaded', function () {
    function afficherInfoPays(nomPays) {
        alert("Petit boite de dialogue qui dit le nom du pays. Hop tu as cliqué sur " + nomPays);
    }

    var liensPays = document.querySelectorAll('.info-pays');

    liensPays.forEach(function (lien) {
        lien.addEventListener('click', function (event) {
            event.preventDefault(); 
            var nomPays = this.innerText;
            afficherInfoPays(nomPays);
        });
    });
});
