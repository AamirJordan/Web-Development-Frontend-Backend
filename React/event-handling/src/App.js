import React from 'react';
import logo from './logo.svg';
import './App.css';
import FunctionClick from './components/functionClick'
import ClassClick from  './components/classClick'

function App() {
  return (
    <div className="App">
      <FunctionClick />
      <ClassClick />
    </div>
  );
}

export default App;
