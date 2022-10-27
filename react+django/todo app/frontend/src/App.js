import React, { Component } from "react";
import { CustomModal, DeleteModel } from "./components/Modal";
import { Login } from "./components/Login";
import { Signup } from "./components/Signup";
import { Hello } from "./components/Hello";

import { Switch, Route, Link, BrowserRouter } from "react-router-dom";

//import axios from "axios";
import {Button, Input } from "reactstrap";
import axiosInstance from "./axiosApi";

class App extends Component {
  constructor(props) {
    super(props);
    this.state = {
      displayResult: false,
      query: "",
      viewCompleted: false,
      todoList: [],
      changeEditModal: false,
      deleteModal: false,
      activeItem: {
        title: "",
        description: "",
        completed: false,
      },
    };
  }

  componentDidMount() {
    this.refreshList();
  }

  refreshList = () => {
    if (this.state.query === ""){
      axiosInstance
        .get("/todos/")
        .then((res) => this.setState({ todoList: res.data }))
        .catch(error => {
          console.log(error);
          throw error;
        })
    }
  };

  toggle = () => {
    this.setState({ changeEditModal: !this.state.changeEditModal });
  };

  toggleDelete = () => {
    this.setState({ deleteModal: false });
  }

  handleSearch = (e) => {
    let {value} = e.target;

    this.setState({ query: value })
  }

  resetSearch = () => {
    this.setState({ query: "", displayResult: false }, this.refreshList);
  }

  handleError = (string) => {
    console.log(string);
  }

  handleSearchSubmit = () => {
    axiosInstance
      .get(`/todos/1/search/?search=${this.state.query}`)
      .then((res) => this.setState({ todoList: res.data , displayResult: true}))
  }

  handleSubmit = (item) => {
    this.toggle();

    if (item.id) {
      axiosInstance
        .put(`/todos/${item.id}/`, item)
        .then((res) => this.refreshList());
      return;
    }
    axiosInstance
      .post("/todos/", item)
      .then((res) => this.refreshList());
  };

  handleDelete = (item) => {
    axiosInstance
      .delete(`/todos/${item.id}/`)
      .then((res) => this.refreshList());
  };

  handleLogout() {
    axiosInstance.post('/blacklist/', {
      "refresh_token": localStorage.getItem("refresh_token")
    }).then( 
      () => {
        localStorage.removeItem('access_token');
        localStorage.removeItem('refresh_token');
        axiosInstance.defaults.headers['Authorization'] = null;
        window.location.reload(false);
      }
    ).catch ( error => {
      console.log(error);
    })
  }

  deleteItem = (item) => {
    this.setState({ activeItem: item, deleteModal: true });
  }

  createItem = () => {
    const item = { title: "", description: "", completed: false };

    this.setState({ activeItem: item, changeEditModal: !this.state.changeEditModal });
  };

  editItem = (item) => {
    this.setState({ activeItem: item, changeEditModal: !this.state.changeEditModal });
  };

  displayCompleted = (status) => {
    if (status) {
      return this.setState({ viewCompleted: true });
    }

    return this.setState({ viewCompleted: false });
  };
 
  renderTabList = () => {
    return (
      <div className="nav nav-tabs">
        <span>
          <button
            className={this.state.viewCompleted ? "nav-link active" : "nav-link"}
            onClick={() => this.displayCompleted(true)}
          >
            Complete
          </button>
        </span>
        <span>
          <button
            className={this.state.viewCompleted ? "nav-link" : "nav-link active"}
            onClick={() => this.displayCompleted(false)}
          >  
            Incomplete
          </button>
        </span>
      </div>
    );
  };

  renderItems = () => {
    const { viewCompleted } = this.state;
    const newItems = this.state.todoList.filter(
      (item) => item.completed === viewCompleted
    );

    return newItems.map((item) => (
      <li
        key={item.id}
        className="list-group-item d-flex justify-content-between align-items-center"
      >
        <span
          className={`todo-title mr-2 ${
            this.state.viewCompleted ? "completed-todo" : ""
          }`}
          title={item.description}
        >
          {item.title}
        </span>
        <span>
          <button
            className="btn btn-secondary mr-2"
            onClick={() => this.editItem(item)}
          >
            Edit
          </button>
          <button
            className="btn btn-danger"
            onClick={() => this.deleteItem(item)}
          >
            Delete
          </button>
        </span>
      </li>
    ));
  };

  render() {
    return (
      <main className="container">
        <h1 className="text-black text-uppercase text-center my-4" onClick = {this.resetSearch}>Todo app</h1>
        <div className="row">
          <div className="col-md-6 col-sm-10 mx-auto p-0">
            <div className="card p-3">
              <div className="mb-4">
                <button
                  className="btn btn-primary"
                  onClick={this.createItem}
                >
                  Add task
                </button>
                <span>
                  <Input
                    type = 'text'
                    name = 'query'
                    placeholder = 'Search todo...'
                    method = 'get'
                    value = {this.state.query}
                    onChange = {this.handleSearch}
                  >
                  </Input>
                </span>
                <span>
                  <Button
                    id = 'searchButton'
                    onClick = {() => {
                      this.handleSearchSubmit();
                      }
                    }
                    color = "success"
                  >
                  Search
                  </Button>
                </span>
                <span>
                  { this.state.displayResult ? (
                    <p>Results for: {this.state.query}</p>
                  ) : null }
                </span>
              </div>
              
              {this.renderTabList()}
              <ul className="list-group list-group-flush border-top-0">
                {this.renderItems()}
              </ul>
            </div>
          </div>
        </div>
        {this.state.changeEditModal ? (
          <CustomModal
            activeItem={this.state.activeItem}
            toggle={this.toggle}
            onSave={this.handleSubmit}
          />
        ) : null}

        {this.state.deleteModal ? (
          <DeleteModel
            activeItem = {this.state.activeItem}
            toggle = {this.toggleDelete}
            onDelete = {this.handleDelete}
          />
        ) : null}
        <h1>Ahhh after 10,000 years I'm free. Time to conquer the Earth!</h1>
        <BrowserRouter>
        <nav>
          <Link className={"nav-link"} to={"/"}>Home</Link>
          <Link className={"nav-link"} to={"/login/"}>Login</Link>
          <Link className={"nav-link"} to={"/hello/"}>Hello</Link>          
          <Link className={"nav-link"} to={"/signup/"}>Signup</Link>
          <button onClick={this.handleLogout}>Logout</button>
        </nav>
          <Switch>
              <Route exact path={"/login/"} component={ Login }/>
              <Route exact path={"/hello/"} component={Hello}/>
              <Route exact path={"/signup/"} component={ Signup }/>
              <Route path={"/"} render={() => <div>Home again</div>}/>
          </Switch>
        </BrowserRouter>
      </main>
    );
  }
}

export default App;