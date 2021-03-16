import React from 'react';
//import logo from './logo.svg';
import './App.css';
import UserList from './components/ServiceUser.js';
import axios from 'axios';

class App extends React.Component {
    constructor(props) {
        super(props)
        this.state = {'users': []}
    }

    componentDidMount() {
        axios.get('http://localhost:8000/api/users')
        .then(resp => {
            const users = resp.data
            this.setState(
                {'users': users}
            )
        }).catch(err => console.log(err))
    }

    render() {
        return (
            <div>
                <UserList users={this.state.users} />
            </div>
        )
    }
}

export default App;
