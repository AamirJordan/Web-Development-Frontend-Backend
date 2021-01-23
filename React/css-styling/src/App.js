import React from 'react';
import logo from './logo.svg';
import './App.css';
import DemoCSS1 from './components/method1'
import DemoCSS2 from './components/method2'
import InlineCSS from './components/inline_method'
import './appstyle.css'
import styles from './components/appstyle.module.css'

function App() {
  return (
    <div className="App">
      <DemoCSS1 />
      <DemoCSS2 primary = {true} />
      <InlineCSS />
      <h1 className='error'>Error</h1>
      <h1 className='success'>Success</h1>
    </div>
  );
}

export default App;
