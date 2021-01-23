import React from 'react'
import './mystyle.css'


  function DemoCSS2(props) {
      let className = props.primary ? 'primary' : ''
    return(
      <div>
        <h1 className={className}> CSS-Stylesheet </h1>
      </div>
    )
  }

  export default DemoCSS2
