import React, {Component} from 'react'

class EventBind extends Component {


  constructor(){
    super()
    this.state = {
      message : 'Hew!'
    }

    this.ClickHandler = this.ClickHandler.bind(this)
  }



  ClickHandler() {
    this.setState({
      message: 'Goodbye'
    })
  }

  // ------------OR------------
  // ClickHandler = () => {
  //   this.setState({
  //     message: 'Goodbye'
  //   })
  // }



  render(){
    return(
      <div>
        <div>{this.state.message}</div>
        <button onClick = {this.ClickHandler}> Click </button>
      </div>
    )
  }
}

export default EventBind
