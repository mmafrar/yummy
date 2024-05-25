$(document).ready(function() {
    const addOpeningHourBtn = $('#add-opening-hour-btn');
    const openingHoursForms = $('#opening-hours-forms');
    const managementFormTotalForms = $('[name="form-TOTAL_FORMS"]');

    addOpeningHourBtn.on('click', function() {
        const newFormIndex = openingHoursForms.children().length;
        const firstForm = openingHoursForms.children().first();
        const newForm = firstForm.clone();
        
        // Update field names and IDs to ensure uniqueness
        newForm.find('[id]').each(function() {
            const id = $(this).attr('id').replace(/\d+/, newFormIndex);
            $(this).attr('id', id);
        });
        newForm.find('[name]').each(function() {
            const name = $(this).attr('name').replace(/\d+/, newFormIndex);
            $(this).attr('name', name);
        });

        // Reset values in the cloned form if needed
        newForm.find('input[type="text"], select').val('');

        // Add remove button to the new form
        const removeBtn = $('<button type="button" class="remove-btn">Remove</button>');
        removeBtn.on('click', function() {
            newForm.remove();
            updateFormIndex();
        });
        newForm.append(removeBtn);

        openingHoursForms.append(newForm);

        // Update the TOTAL_FORMS value in management form
        managementFormTotalForms.val(newFormIndex + 1);
    });

    // Function to update the form index
    function updateFormIndex() {
        openingHoursForms.children().each(function(index) {
            $(this).find('[id]').each(function() {
                const id = $(this).attr('id').replace(/\d+/, index);
                $(this).attr('id', id);
            });
            $(this).find('[name]').each(function() {
                const name = $(this).attr('name').replace(/\d+/, index);
                $(this).attr('name', name);
            });
        });
        managementFormTotalForms.val(openingHoursForms.children().length);
    }
});
