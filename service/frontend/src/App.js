import React from 'react';
import logo from './logo.svg';
import './App.css';
import UserList from './components/User.js'


class App extends React.Component {

  constructor(props) {
    super(props);
    this.state = {
      'users': []
    }
  }

  componentDidMount() {
    const users = [
      {
        'user_name': "username1",
        'first_name': "first1",
        'last_name': "last",
        'email': "mail1@mail.ru"
      },
      {
        'user_name': "username2",
        'first_name': "first2",
        'last_name': "last2",
        'email': "mail2@mail.ru"
      }
    ]
    this.setState(
      {
        'users': users
      }
    )
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
