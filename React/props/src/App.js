import React from 'react';
import logo from './logo.svg';
import './App.css';
import Hii from './components/props_using_function_component'
import Welcome from './components/props_using_class_component'

function App() {
  return (
    <div className="App">
      <Hii name = 'Bruce' heroname = 'Batman'/>
      <b> Do You Bleed </b>
      <Hii name = 'Clark' heroname = 'Superman'/>
      <button>Krypton</button>
      <Hii name = 'Diana' heroname = 'Wonder Woman'/>


      <Welcome name= 'Bruce' heroname = 'Batman'/>
      <Welcome name = 'Clark' heroname = 'Superman'/>
      <Welcome name = 'Diana' heroname = 'Wonder Woman'/>
    </div>
  );
}

export default App;
