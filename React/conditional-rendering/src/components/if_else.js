import React, {Component} from 'react'


class LogIn extends Component {

  constructor(){
    super()
    this.state = {
      isLoggedIn : false
    }
  }




  render(){
    if (this.state.isLoggedIn){
      return(
        <div>
          if-else condition is true
        </div>
      )
    }
    else {
      return(
        <div>
          if-else condition is false
        </div>
      )
    }
  }
}

export default LogIn
