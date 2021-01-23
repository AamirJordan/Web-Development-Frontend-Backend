import React from 'react';
import logo from './logo.svg';
import './App.css';
import LogIn from './components/if_else'
import TernaryCond from './components/ternary_conditional_operator'
import ShortCircuit from './components/short_circuit_method'

function App() {
  return (
    <div className="App">
      <LogIn />
      <TernaryCond />
      <ShortCircuit />
    </div>
  );
}

export default App;
