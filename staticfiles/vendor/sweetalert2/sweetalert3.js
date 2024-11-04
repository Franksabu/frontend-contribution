
    const deleteButtons = document.querySelectorAll('.delete-button');

    deleteButtons.forEach(function(button) {
        button.onclick = function() {
            Swal.fire({
                title: 'Êtes-vous sûr de vouloir supprimer ?',
                text: 'Vous ne pourrez pas récupérer cette Colonnen imaginaire !',
                icon: 'warning',
                showCancelButton: true,
                confirmButtonText: 'Supprimer',
                cancelButtonText: 'Annuler',
                reverseButtons: true
            }).then(function(result) {
                if (result.isConfirmed) {
                    // Logique pour supprimer l'élément
                    Swal.fire('Colonne supprimée !', '', 'success');
                } else if (result.isDismissed) {
                    Swal.fire('Colonne non supprimé !');
                }
            });
        };
    });


