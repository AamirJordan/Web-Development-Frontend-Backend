import React from 'react'


  const heading = {
    fontSize : '50px',
    color : 'red',
    background : 'lightgreen'
  }


  function InlineCSS() {
    return(
      <div>
        <h1 style={heading} > Inline Method Styling </h1>
      </div>
    )
  }


  export default InlineCSS
