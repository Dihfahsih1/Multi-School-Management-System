
import React from 'react';
import {Link} from 'react-router-dom';
//import LoginForm from "../forms/LoginForm";
const AboutPage = () =>(
   <div>
    <Link to="/LoginPage">Login</Link>|
    <Link to="/">Home</Link>
    <h1>About Page</h1>
    </div>
);
export default AboutPage;
