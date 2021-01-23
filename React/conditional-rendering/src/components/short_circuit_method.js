import React, {Component} from 'react'


class ShortCircuit extends Component {

  constructor(){
    super()
    this.state = {
      isLoggedIn : true
    }
  }




  render(){
    return this.state.isLoggedIn && <div>If the condition is true this will get executed otherwise if the condition is false nothing will get displayed. </div>
  }
}

export default ShortCircuit
