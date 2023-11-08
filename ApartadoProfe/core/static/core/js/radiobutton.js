$(document).ready(function() {
    $('button').click(function() {
        if ($("input[type=radio][name=asistencia]:checked").is(':checked')) {
            
        }
    })
});

function marcarAusente() {
    var checkboxes = document.querySelectorAll('input[type="checkbox"]');
    checkboxes.forEach(function(checkbox) {
        if (checkbox.value === '2') {
            checkbox.checked = true;
        } else {
            checkbox.checked = false;
        }
    });
    }

    window.onload = function() {
        marcarAusente();
    };