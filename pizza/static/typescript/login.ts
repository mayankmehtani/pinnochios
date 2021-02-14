Vue.component('user-login', {
    data: function () {
      return {
        title: "Welcome to Pinnochio's",
      }
    },
    methods: {
        setUsernameValidityMessage: function(event: any) {
            event.target.setCustomValidity("");
        },
        setPasswordValidityMessage: function(event: any) {
            event.target.setCustomValidity("");
        },
        checkLoginFields: function(event: any) {
            let username:string = this.$refs.username.value.trim();
            let password:string = this.$refs.password.value;

            if (!Boolean(username)) {
                this.$refs.username.setCustomValidity("Username cannot be empty");
                this.$refs.username.reportValidity();
                event.preventDefault();
            }
            else if (!Boolean(password)) {
                this.$refs.password.setCustomValidity("Password cannot be empty");
                this.$refs.password.reportValidity();
                event.preventDefault();
            }

            return Boolean(username) && Boolean(password);
        }
    },
    template: `
        <div>
            <img src="https://cdn.clipart.email/e0538c3a15f0b0940682455074ba9c4c_italy-pizza-clipart_2000-1761.png" height = "105" width = "122"/>
            <h1>
                <center>
                    {{ title }}
                </center>
            </h1>

            <div>
                <center>
                    <form action="{% url 'login' %}" method="post" @submit='checkLoginFields'>
                        <input ref="username" placeholder="username" type="text" v-on:input="setUsernameValidityMessage"/>
                        <input ref="password" placeholder="password" type="password" v-on:input="setPasswordValidityMessage"/>
                        <input type="submit" value="Login"/>
                    </form>
                    <p> New User? Sign Up - <a href="signup">Here!</a></p>
                </center>
            </div>
        </div>
        `
})

const main = new Vue({
    delimiters : ['[[',']]'],
    el: '#main',
})
