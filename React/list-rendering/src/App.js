import React from 'react';
import logo from './logo.svg';
import './App.css';
import NameList from './components/namelist'
import PersonList from './components/namelist'

function App() {
  return (
    <div className="App">
      <NameList />
      <PersonList />
    </div>
  );
}

export default App;
