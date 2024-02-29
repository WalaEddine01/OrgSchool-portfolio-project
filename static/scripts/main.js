document.addEventListener('DOMContentLoaded', function () {
    $('.submit').click(function () {
        // Check if all required fields are filled out
        var schoolNameInput = document.querySelector('.school_name input');
        var emailInput = document.querySelector('.email input');
        var passwordInput = document.querySelector('.password input');
        var confirmPasswordInput = document.querySelector('.confirm_password input');
        
        if (schoolNameInput.value && emailInput.value && passwordInput.value && confirmPasswordInput.value) {
            const admin_infos = [
                schoolNameInput.value,
                emailInput.value,
                passwordInput.value,
                confirmPasswordInput.value
            ];
            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:5000/api/v1/admins',
                contentType: 'application/json',
                data: JSON.stringify({ school_name: admin_infos[0], email: admin_infos[1], password: admin_infos[2]}),
            });
        } else {
            alert('Please fill out all required fields.');
        }
    });
});
document.addEventListener('DOMContentLoaded', function () {
    $('.submit').click(function () {
        // Check if all required fields are filled out
        var schoolNameInput = document.querySelector('.school_name input');
        var emailInput = document.querySelector('.email input');
        var passwordInput = document.querySelector('.password input');
        var confirmPasswordInput = document.querySelector('.confirm_password input');
        
        if (schoolNameInput.value && emailInput.value && passwordInput.value && confirmPasswordInput.value) {
            const admin_infos = [
                schoolNameInput.value,
                emailInput.value,
                passwordInput.value,
                confirmPasswordInput.value
            ];
            $.ajax({
                type: 'POST',
                url: 'http://127.0.0.1:5000/api/v1/admins',
                contentType: 'application/json',
                data: JSON.stringify({ school_name: admin_infos[0], email: admin_infos[1], password: admin_infos[2]}),
            });
        } else {
            alert('Please fill out all required fields.');
        }
    });
});