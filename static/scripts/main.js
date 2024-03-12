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
    $('.sub2').click(function () {
        var name = document.querySelector('.name').value;
        var sclass_id = document.querySelector('.sclass_id').value;
        var admin_id = document.querySelector('.admin_id').value;

        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/teachers`,
            contentType: 'application/json',
            data: JSON.stringify({ name: name, sclass_id: sclass_id, admin_id: admin_id}),
            success: function() {
                // Initialize reload count if not already set
                if (localStorage.getItem('reloadCount') === null) {
                    localStorage.setItem('reloadCount', '0');
                }

                // Increment the reload count
                var reloadCount = Number(localStorage.getItem('reloadCount'));
                reloadCount++;
                localStorage.setItem('reloadCount', reloadCount.toString());

                // Reload the page if reload count is less than 2
                if (reloadCount < 2) {
                    window.location.reload();
                } else {
                    // Reset the reload count after the second reload
                    localStorage.setItem('reloadCount', '0');
                }
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function () {
    $('.sub3').click(function () {
        var num = document.querySelector('.number').value;
        var teachers = document.querySelectorAll('.teacher');
        var sclass_id = document.querySelector('.sclass_id').value;
        var teacher;
        for (var i = 0; i < teachers.length; i++) {
            if (num == i + 1){
                teacher = teachers[i].value;
                break;
            }
        }
        var teacher_id;
        const parts = teacher.split("(");
        const idWithParenthesis = parts[1].split(")");
        const id2 = idWithParenthesis[0];
        const id = id2.split(" ");
        teacher_id = id[0];
        $.ajax({
            type: 'DELETE',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/teachers/${teacher_id}`,
            success: function() {
                // Initialize reload count if not already set
                if (localStorage.getItem('reloadCount') === null) {
                    localStorage.setItem('reloadCount', '0');
                }

                // Increment the reload count
                var reloadCount = Number(localStorage.getItem('reloadCount'));
                reloadCount++;
                localStorage.setItem('reloadCount', reloadCount.toString());

                // Reload the page if reload count is less than 2
                if (reloadCount < 2) {
                    window.location.reload();
                } else {
                    // Reset the reload count after the second reload
                    localStorage.setItem('reloadCount', '0');
                }
            }
        });
    })
})


document.addEventListener('DOMContentLoaded', function () {
    $('.sub4').click(function () {
        var name = document.querySelector('.name2').value;
        var sclass_id = document.querySelector('.sclass_id').value;
        var age = document.querySelector('.age').value;
        var admin_id = document.querySelector('.admin_id').value;
        
        $.ajax({
            type: 'POST',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/students`,
            contentType: 'application/json',
            data: JSON.stringify({ name: name, age: age, sclass_id: sclass_id, admin_id: admin_id}),
            success: function() {
                // Initialize reload count if not already set
                if (localStorage.getItem('reloadCount') === null) {
                    localStorage.setItem('reloadCount', '0');
                }

                // Increment the reload count
                var reloadCount = Number(localStorage.getItem('reloadCount'));
                reloadCount++;
                localStorage.setItem('reloadCount', reloadCount.toString());

                // Reload the page if reload count is less than 2
                if (reloadCount < 2) {
                    window.location.reload();
                } else {
                    // Reset the reload count after the second reload
                    localStorage.setItem('reloadCount', '0');
                }
            }
        });
        console.log('Student added');
    });
});

document.addEventListener('DOMContentLoaded', function () {
    $('.sub5').click(function () {
        var num = document.querySelector('.number2').value;
        var students = document.querySelectorAll('.student');
        var sclass_id = document.querySelector('.sclass_id').value;
        var student;
        for (var i = 0; i < students.length; i++) {
            if (num == i + 1){
                student = students[i].value;
                break;
            }
        }
        console.log('num:', num);
        console.log('sclass_id:', sclass_id);
        var student_id;
        console.log('Student:', student);
        const parts = student.split("(");
        console.log('Parts:', parts);
        const idWithParenthesis = parts[1].split(")");
        console.log('ID with parenthesis:', idWithParenthesis);
        const id2 = idWithParenthesis[0];
        console.log('ID2:', id2);
        const id = id2.split(" ");
        console.log('ID:', id);
        student_id = id[0];
        console.log('Student ID:', student_id);
        $.ajax({
            type: 'DELETE',
            url: `http://127.0.0.1:5000/api/v1/sclasses/${sclass_id}/students/${student_id}`,
            success: function() {
                // Extract the current reload count from the URL
                var urlParams = new URLSearchParams(window.location.search);
                var reloadCount = urlParams.get('reloadCount') ? Number(urlParams.get('reloadCount')) : 0;

                // Increment the reload count
                reloadCount++;

                // Update the URL with the new reload count
                urlParams.set('reloadCount', reloadCount);
                window.history.replaceState({}, '', '?' + urlParams.toString());

                // Reload the page if reload count is less than 2
                if (reloadCount < 2) {
                    window.location.reload();
                }
            }
        });
    })
})