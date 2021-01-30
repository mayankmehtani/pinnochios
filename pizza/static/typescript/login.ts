const main = new Vue({
    delimiters : ['[[',']]'],
    el: '#main',
    methods: {
        setUsernameValidity: function() {
            document.querySelector('input[name=username]').setCustomValidity("");
        },
        setPasswordValidity: function() {
            document.querySelector('input[name=password]').setCustomValidity("");
        }
    },
    data: {
        title: "Welcome to Pinnochio's!"
    }
})

function checkLoginFields(): boolean {
    let username:string = document.querySelector('input[name=username]').value.trim();
    let password:string = document.querySelector('input[name=password]').value;

    if (!Boolean(username)) {
        document.querySelector('input[name=username]').setCustomValidity("Username cannot be empty");
        document.querySelector('input[name=username]').reportValidity();
    }
    else if (!Boolean(password)) {
        document.querySelector('input[name=password]').setCustomValidity("Password cannot be empty");
        document.querySelector('input[name=password]').reportValidity();
    }

    return Boolean(username) && Boolean(password);
}
