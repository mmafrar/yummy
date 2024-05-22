$(document).ready(function() {
    function updateManagementForm() {
        var totalForms = $('.opening-hour-form').length;
        $('#id_openinghour_set-TOTAL_FORMS').val(totalForms);

        $('.opening-hour-form').each(function(index) {
            $(this).find('input, select').each(function() {
                var name = $(this).attr('name').replace(/-\d+-/, '-' + index + '-');
                var id = $(this).attr('id').replace(/_\d+_/, '_' + index + '_');
                $(this).attr({ 'name': name, 'id': id });
            });
        });
    }

    $('#add-opening-hours-btn').on('click', function() {
        var formCount = $('.opening-hour-form').length;
        var newForm = $('.opening-hour-form:first').clone(false).get(0);

        $(newForm).find('input, select').each(function() {
            var name = $(this).attr('name').replace(/-\d+-/, '-' + formCount + '-');
            var id = $(this).attr('id').replace(/_\d+_/, '_' + formCount + '_');
            $(this).attr({ 'name': name, 'id': id }).val('');

            if ($(this).is(':checkbox')) {
                $(this).prop('checked', false);
            }
        });

        $(newForm).find('.remove-opening-hour-btn').removeClass('d-none');
        $('#update-opening-hours-forms').append(newForm);
        updateManagementForm();
    });

    $(document).on('click', '.remove-opening-hour-btn', function() {
        var form = $(this).closest('.opening-hour-form');
        form.find('input[name$="-DELETE"]').val('on');
        form.hide();
        updateManagementForm();
    });

    updateManagementForm();
});
