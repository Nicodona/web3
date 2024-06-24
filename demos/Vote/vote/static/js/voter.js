document.addEventListener('DOMContentLoaded', function () {
    const messageBox = document.getElementById('message');
    const submitButton = document.getElementById('submit-button');
    const options = document.querySelectorAll('.option');

    options.forEach(option => {
        option.addEventListener('mouseover', () => {
            messageBox.textContent = 'Scanning...';
        });

        option.addEventListener('mouseout', () => {
            messageBox.textContent = 'Please scan your finger on any of the sensor to vote';
        });

        option.addEventListener('click', () => {
            messageBox.textContent = 'Verifying...';
            submitButton.disabled = false;
            submitButton.classList.add('enabled');
        });
    });
});


document.getElementById('form1').addEventListener('click', function () {
    const inputValue = document.getElementById('input1').value
        ;
    document.getElementById('binput').value = inputValue;
    document.getElementById('winput').value = inputValue;
    document.getElementById('yinput').value = inputValue;


})
