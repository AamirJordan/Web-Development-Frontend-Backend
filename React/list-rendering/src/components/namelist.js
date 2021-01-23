import React from 'react'


function NameList() {
  const names = ['Bruce','Clark','Diana']
  const individualname =   names.map(name => <h2>{name}</h2>)
  return(
    <div>{individualname}</div>
  )
}

function PersonList() {
  const persons = [
    {
      id:1,
      name:'Smith',
      age:30,
      skill:'React'
    },

    {
      id:2,
      name:'Warner',
      age:33,
      skill:'Angular'
    },
    {
      id:3,
      name:'Maxwell',
      age:28,
      skill:'Python'
    },
  ]

  const indiperson = persons.map(person =>
    <h2>I am {person.name}. I am {person.age} years old. I know {person.skill}</h2>
  )
  return <div>{indiperson}</div>

}



// export default NameList
export default PersonList
