import React, {Component} from 'react'
import ChildComponent from './components/childcomponent'


class ParentComponent extends Component {

  constructor(){
    super()
    this.state = {
      parentname : 'parent'
    }

    this.greetParent = this.greetParent.bind(this)
  }



  greetParent(){
    alert("Hello" + this.state.parentname)
  }


  render(){
    return(
      <div>
        <ChildComponent/>
      </div>
    )
  }
}

export default ParentComponent
