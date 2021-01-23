import React, {Component} from 'react'


  class Forms extends Component {
    render(){
    return(
      <form action="https://www.facebook.com" method="get">
        <div>
          <label>Username</label>
          <input type='text'/>

          <label>TextArea</label>
          <input type='text area' />

          <label>Topic</label>
          <select>
            <option value='react'>React</option>
            <option value='javascript'>Javascript</option>
            <option value='bootstrap'>Bootstrap</option>
          </select>
        </div>
        <button>Submit</button>
      </form>
    )
  }
  }

  export default Forms
