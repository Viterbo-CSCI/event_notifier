import 'RegisterForm.css';

const RegisterForm = () =>{
    return(

        <section class="container">
        <header>Register</header>
        <form action="#" class="form">
            <div class="input-box">
                <label> Name </label>
                <input type="text" placeholder="Enter Name" required/>
            </div>
            <div class="input-box">
                <label> Email </label>
                <input type="text" placeholder="Enter Email" required/>
            </div>

        <div class="column">
            <div class="input-box">
                <label> Phone Number </label>
                <input type="text" placeholder="Enter Phone Number" required/>
            </div>

            <div class="input-box">
                <label> Birth Date</label>
                <input type="text" placeholder="Enter Birth Date mm/dd/yyyy" required/>
            </div>
        </div>
        <div class="input-box">
            <label> Address </label>
            <input type="text" placeholder="Enter Street Address" required/>
            <input type="text" placeholder="Enter City" required/>
            <input type="text" placeholder="Enter State" required/>
        </div>

        <button> Submit </button>

        </form>
    </section>

    );
};

export default RegisterForm;