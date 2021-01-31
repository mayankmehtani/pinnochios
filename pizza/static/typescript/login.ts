const main = new Vue({
    delimiters : ['[[',']]'],
    el: '#main',
    methods: {
        setUsernameValidityMessage: function(event) {
            event.target.setCustomValidity("");
        },
        setPasswordValidityMessage: function(event) {
            event.target.setCustomValidity("");
        }
    },
    data: {
        title: "Welcome to Pinnochio's!"
    }
})

function checkLoginFields(event): boolean {
    let username:string = document.querySelector('input[name=username]').value.trim();
    let password:string = document.querySelector('input[name=password]').value;

    if (!Boolean(username)) {
        document.querySelector('input[name=username]').setCustomValidity("Username cannot be empty");
        document.querySelector('input[name=username]').reportValidity();
        event.preventDefault();
    }
    else if (!Boolean(password)) {
        document.querySelector('input[name=password]').setCustomValidity("Password cannot be empty");
        document.querySelector('input[name=password]').reportValidity();
        event.preventDefault();
    }

    return Boolean(username) && Boolean(password);
}
