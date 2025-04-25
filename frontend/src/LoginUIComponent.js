
import 'LoginPageCSS';

const LoginUI = () =>{
    return(
<body>
    <div class= "wrapper">
        <form action="">
            <h1>Login</h1>
            <div class="input-box">
                <input type="text" placeholder="Username"
                required/>
            </div>
            <div class="input-box">
                <input type="password"
                placeholder="Password" required/>
            </div>

            <div class="remember-forgot">
                <label><input type="checkbox"/>Remember me</label>
                <a href="#">Forgot Password?</a>
            </div>

            <button type="submit" class="btn">Login</button>

            <div class="register-link"></div>
                <p>Don't Have an acoount?<a
                href="#">Sign Up!</a></p>
        </form>
    </div>
</body>
    );
};

export default LoginUI;