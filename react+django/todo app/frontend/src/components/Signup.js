import React, { Component } from "react";
import axiosInstance from "../axiosApi";

export class Signup extends Component{
    constructor(props){
        super(props);
        this.state = {
            username: "",
            password: "",
            email:""
        };

        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }

    handleChange(event) {
        this.setState({[event.target.name]: event.target.value});
    }

    handleSubmit(event) {
        event.preventDefault();
        axiosInstance.post('/user/create/', {
            username: this.state.username,
            email: this.state.email,
            password: this.state.password
        }).then( result => result)
        .catch(error => {
            console.log(error.stack);
            this.setState({
                errors:error.response.data
            });
        })
    }

    render() {
        return (
            <div>
                Signup
                <form onSubmit={this.handleSubmit}>
                    <label>
                        Username:
                        <input name="username" type="text" value={this.state.username} onChange={this.handleChange}/>
                        {/* { this.state.errors ? this.state.errors.username : null} */}
                    </label>
                    <label>
                        Email:
                        <input name="email" type="email" value={this.state.email} onChange={this.handleChange}/>
                        {/* { this.state.errors ? this.state.errors.email : null} */}
                    </label>
                    <label>
                        Password:
                        <input name="password" type="password" value={this.state.password} onChange={this.handleChange}/>
                        { this.state.errors ? this.state.errors.password : null}
                    </label>
                    <input type="submit" value="Submit"/>
                </form>
            </div>
        )
    }
}