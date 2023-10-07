let CountrySelected = $('#id_default_country').val();
if (!CountrySelected) {
    $('#id_default_country').css('color', '#aab7c4');
}
$('#id_default_country').change(function () {
    CountrySelected = $(this).val();
    if (!CountrySelected) {
        $(this).css('color', '#aab7c4');
    } else {
        $(this).css('color', '#000');
    }
});