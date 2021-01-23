import React from 'react'


const Hello = () => {

  //------------------------  WITH JSX  ----------------------------------------    ##### THIS SHOULD BE FOLLOWED
//     return (
//       <div className = 'dummyclass'>
//         <h1> Jsx says Hello! </h1>
//       </div>
//       )
// }

//--------------------------- WITHOUT Jsx --------------------------------------


return React.createElement(
  'div',
  {id:'hello',className:'dummyclass'},
  React.createElement('h1',null,'Without JSX says Hello')
)
}


export default Hello
