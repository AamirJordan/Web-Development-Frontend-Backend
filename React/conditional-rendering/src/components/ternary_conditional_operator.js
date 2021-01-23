import React, {Component} from 'react'


class TernaryCond extends Component {

  constructor(){
    super()
    this.state = {
      isLoggedIn : true
    }
  }




  render(){
    return (
      this.state.isLoggedIn ?
      <div> Ternary Condition is true </div> :
      <div> Ternary Condition is false </div>
    )
  }
}
export default TernaryCond
