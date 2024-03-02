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
    $('.sub2').click(function (event) {
        event.preventDefault();
        var name = document.querySelector('.name').value;
        var sclass_id = document.querySelector('.sclass_id').value;

        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/teachers`,
            contentType: 'application/json',
            data: JSON.stringify({ name: name, sclass_id: sclass_id }),
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    /* $('.sub3').click(function (event) {
        event.preventDefault();
        var name = document.querySelector('.name').value;
        var sclass_id = document.querySelector('.sclass_id').value;

        if (!name || !sclass_id) {
            alert('Please fill out all required fields.');
            return;
        }
        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/teachers`,
            contentType: 'application/json',
            data: JSON.stringify({ name: name, sclass_id: sclass_id }),
        });
    });
    */
});

document.addEventListener('DOMContentLoaded', function () {
    $('.sub4').click(function (event) {
        event.preventDefault();
        var name = document.querySelector('.name2').value;
        var sclass_id = document.querySelector('.sclass_id').value;
        var age = document.querySelector('.age').value
        console.log('Name value:', name);

        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/students`,
            contentType: 'application/json',
            data: JSON.stringify({ name: name, age: age}),
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    $('.sub5').click(function (event) {
        event.preventDefault();
        var num = document.querySelector('.number').value;
        var students = document.querySelectorAll('.student');
        var sclass_id = document.querySelector('.sclass_id').value;
        var s = [];
        var student;
        for (var i = 0; i < students.length; i++) {
            if (num == i + 1){
                student = students[i].value;
            }
        }
        var student_id;
        const parts = student.split("(");
        const idWithParenthesis = parts[1].split(")");
        const id2 = idWithParenthesis[0];
        const id = id2.split(" ");
        student_id = id;
        $.ajax({
            type: 'DELETE',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/students/${id}`,
        });
    })
})