function updateQuantityValue(val) {
    document.getElementById('quantity-input').value = val;
}

function updateSliderValue(val) {
    document.getElementById('quantity-slider').value = val;
}

function selectOption(optionId) {
    var option = document.getElementById(optionId);
    option.checked = true;
    toggleSubOperations();
}

function toggleSubOperations() {
    var mainElement = document.querySelector('input[name="operation"]:checked');
    var standardSubOptions = document.getElementById('sub-options-standard');
    var bestSubOptions = document.getElementById('sub-options-best');
    var newFieldElement = document.querySelector('input[name="invito_boolean"]:checked');
    var newSubField = document.getElementById('new-sub-field');

    if (!mainElement) {
        standardSubOptions.classList.add('hidden');
        bestSubOptions.classList.add('hidden');
    } else if (mainElement.value === 'standard') {
        standardSubOptions.classList.remove('hidden');
        bestSubOptions.classList.add('hidden');
    } else if (mainElement.value === 'best_option0') {
        bestSubOptions.classList.remove('hidden');
        standardSubOptions.classList.add('hidden');
    } else {
        standardSubOptions.classList.add('hidden');
        bestSubOptions.classList.add('hidden');
    }

    if (newFieldElement && newFieldElement.value === 'best_option') {
        newSubField.classList.remove('hidden');
    } else {
        newSubField.classList.add('hidden');
    }
}

document.addEventListener('DOMContentLoaded', toggleSubOperations);